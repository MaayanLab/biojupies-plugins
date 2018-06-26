#################################################################
#################################################################
############### Generate Signature
#################################################################
#################################################################

#############################################
########## 1. Load libraries
#############################################
##### 1. General support #####
import os
import pandas as pd
import geode
from rpy2.robjects import r, pandas2ri
pandas2ri.activate()

##### 2. R #####
r.source(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'signature.R'))

#######################################################
#######################################################
########## S1. Design Matrix
#######################################################
#######################################################

def make_design_matrix(expression_dataframe, group_A, group_B, data):

	# Sample names
	group_A = [x.replace(':', '.').replace('-', '.') for x in group_A]
	group_B = [x.replace(':', '.').replace('-', '.') for x in group_B]
	expression_dataframe.columns = [x.replace(':', '.').replace('-', '.') for x in expression_dataframe.columns]

	# Collapse duplicate genes
	expression_dataframe = expression_dataframe.reset_index().groupby('index').sum()

	# Get expression dataframe
	if data == 'subset':
		expression_dataframe = expression_dataframe[group_A+group_B]

	# Create design dataframe
	sample_dict = {'A': group_A, 'B': group_B}
	design_dataframe = pd.DataFrame([{'index': x, 'A': int(x in group_A), 'B': int(x in group_B)} for x in expression_dataframe.columns]).set_index('index')

	# Return
	return {'expression': expression_dataframe, 'design': design_dataframe}

#######################################################
#######################################################
########## S2. Signature Generation
#######################################################
#######################################################

#############################################
########## 1. limma
#############################################

def limma(dataset, group_A, group_B, data='subset'):

	# Get design
	processed_data = make_design_matrix(dataset['rawdata'].copy(), group_A, group_B, data)

	# Add
	return pandas2ri.ri2py(r.limma(pandas2ri.py2ri(processed_data['expression']), pandas2ri.py2ri(processed_data['design']))).sort_values('logFC', ascending=False).set_index('gene_symbol')

#############################################
########## 2. CD
#############################################

def cd(dataset, group_A, group_B, log=False):

	# Create sample class
	sampleclass = []
	for sample in dataset['rawdata'].columns:
		if sample in group_A:
			sampleclass.append(1)
		elif sample in group_B:
			sampleclass.append(2)
		else:
			sampleclass.append(0)

	# Log transform
	if log:
		data = np.log10(dataset['rawdata']+1)
	else:
		data = dataset['rawdata']

	# Calculate CD
	cd = geode.chdir(data=data.values, sampleclass=sampleclass, genes=dataset['rawdata'].index)

	# Create dataframe
	cd_dataframe = pd.DataFrame(cd, columns=['CD', 'gene_symbol']).set_index('gene_symbol').sort_values('CD', ascending=False)

	# Return
	return cd_dataframe
