#################################################################
#################################################################
############### Load Dataset
#################################################################
#################################################################

#############################################
########## 1. Load libraries
#############################################
##### 1. General support #####
import pandas as pd
import urllib
import json
import gzip
import warnings
import os
with warnings.catch_warnings():
	warnings.simplefilter("ignore")
	import h5py

#######################################################
#######################################################
########## S1. Dataset Loading
#######################################################
#######################################################

#############################################
########## 1. ARCHS4
#############################################

def archs4(gse, platform, version='v5', filter_metadata=False):

	# Load HDF5 File
	h5 = '/download/{gse}-{platform}.h5'.format(**locals())
	with open(h5, 'wb') as openfile:
		openfile.write(urllib.request.urlopen('https://storage.googleapis.com/archs4-packages-{}/'.format(version)+h5.split('/')[-1]).read())
	f = h5py.File(h5, 'r')
		
	# Get data
	rawcount_dataframe = pd.DataFrame(data=f['data']['expression'].value, columns=[x for x in f['meta']['gene']['symbol'].value], index=[x for x in f['meta']['sample']['Sample_geo_accession'].value]).T
	sample_metadata_dataframe = pd.DataFrame({key: [x for x in value.value] if type(value) == h5py._hl.dataset.Dataset else [x for x in [y for y in value.items()][0][1].value] for key, value in f['meta']['sample'].items()}).set_index('Sample_geo_accession').rename(columns={'Sample_title': 'Sample Title'})
		
	# Filter
	if filter_metadata:
		for column in sample_metadata_dataframe.columns:
			unique_vals = list(set(sample_metadata_dataframe[column]))
			if len(unique_vals) == 1 or any([len(x) > 20 for x in unique_vals]):
				sample_metadata_dataframe.drop(column, axis=1, inplace=True)

	# Build data
	data = {'rawdata': rawcount_dataframe, 'sample_metadata': sample_metadata_dataframe, 'dataset_metadata': {'source': 'archs4', 'datatype': 'rnaseq', 'gse': gse, 'platform': platform, 'version': version}}
	os.unlink(h5)
		
	# Return
	return data

#############################################
########## 2. Upload
#############################################

def upload(uid, filter_metadata=False):

	# Load HDF5 File
	h5 = '/download/{uid}.h5'.format(**locals())
	with open(h5, 'wb') as openfile:
		openfile.write(urllib.request.urlopen('https://storage.googleapis.com/jupyter-notebook-generator-user-data/{uid}/{uid}.h5'.format(**locals())).read())
	f = h5py.File(h5, 'r')
	
	# Get data
	rawcount_dataframe = pd.DataFrame(data=f['data']['expression'].value, index=[x for x in f['meta']['gene']['symbol'].value], columns=[x for x in f['meta']['sample']['Sample'].value])
	sample_metadata_dataframe = pd.DataFrame({key: [x for x in value.value] if type(value) == h5py._hl.dataset.Dataset else [x for x in [y for y in value.items()][0][1].value] for key, value in f['meta']['sample'].items()}).set_index('Sample')#, drop=False).rename(columns={'Sample': 'Sample Title'})

	# Filter
	if filter_metadata:
		for column in sample_metadata_dataframe.columns:
			unique_vals = list(set(sample_metadata_dataframe[column]))
			if len(unique_vals) == 1 or any([len(x) > 20 for x in unique_vals]):
				sample_metadata_dataframe.drop(column, axis=1, inplace=True)

	data = {'rawdata': rawcount_dataframe, 'sample_metadata': sample_metadata_dataframe, 'dataset_metadata': {'source': 'upload', 'datatype': 'rnaseq'}}
	os.unlink(h5)

	# Return
	return data
