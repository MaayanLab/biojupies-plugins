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
import requests
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

def archs4(gse, platform, version='v6', filter_metadata=False):

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

def upload(uid, filter_metadata=False, collapse_duplicates=True):

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

	# Collapse duplicates
	if collapse_duplicates and any(rawcount_dataframe.index.duplicated()):
		try:
			rawcount_dataframe = rawcount_dataframe.fillna(0).reset_index().groupby('index').sum()
		except:
			pass

	data = {'rawdata': rawcount_dataframe, 'sample_metadata': sample_metadata_dataframe, 'dataset_metadata': {'source': 'upload', 'datatype': 'rnaseq', 'qc': json.loads(f['meta']['sequencing']['qc'].value) if f['meta'].get('sequencing') else None, 'reference_genome': f['meta']['sequencing']['reference_genome'].value if f['meta'].get('sequencing') else None}}
	os.unlink(h5)

	# Return
	return data

#############################################
########## 3. GTEx
#############################################

def gtex(samples):
	r = requests.post('http://amp.pharm.mssm.edu/biojupies-gtex', json={"samples": samples})
	data = {key: pd.DataFrame(value) for key, value in json.loads(r.text).items()} # potentially rename columns in sample_metadata
	data['dataset_metadata'] = {'source': 'gtex', 'datatype': 'rnaseq'}
	return data
