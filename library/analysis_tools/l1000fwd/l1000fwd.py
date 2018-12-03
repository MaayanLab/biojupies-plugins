#################################################################
#################################################################
############### DE 
#################################################################
#################################################################

#############################################
########## 1. Load libraries
#############################################
##### 1. General support #####
import requests
import json
import sys
import os
import pandas as pd
from IPython.display import display, IFrame, Markdown, HTML

##### 2. Other libraries #####
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))), 'core_scripts', 'shared', 'shared.py'))
from shared import *


#######################################################
#######################################################
########## S1. Function
#######################################################
#######################################################

#############################################
########## 1. Run
#############################################

def run(signature, nr_genes=500, signature_label=''):

	# Define results
	l1000fwd_results = {'signature_label': signature_label}

	# Define upperGenes Function
	upperGenes = lambda genes: [gene.upper() for gene in genes]

	# Get Data
	payload = {"up_genes":upperGenes(signature.index[:nr_genes]),"down_genes":upperGenes(signature.index[-nr_genes:])}

	# Get URL
	L1000FWD_URL = 'https://amp.pharm.mssm.edu/L1000FWD/'

	# Get result
	response = requests.post(L1000FWD_URL + 'sig_search', json=payload)
	if 'KeyError' in response.text:
		l1000fwd_results['result_url'] = None
	else:
		# Get ID and URL
		result_id = response.json()['result_id']
		l1000fwd_results['result_url'] = 'https://amp.pharm.mssm.edu/l1000fwd/vanilla/result/'+result_id
		l1000fwd_results['result_id'] = result_id

		# Get Top
		l1000fwd_results['signatures'] = requests.get(L1000FWD_URL + 'result/topn/' + result_id).json()


	# Return
	return l1000fwd_results

#############################################
########## 2. Plot
#############################################

def plot(l1000fwd_results, plot_counter, nr_drugs=7, height=300):
	
	# Check if results
	if l1000fwd_results['result_url']:

		# Display IFrame
		display(IFrame(l1000fwd_results['result_url'], width="1000", height="1000"))

		# Display tables
		for direction, signature_list in l1000fwd_results['signatures'].items():

			# Fix dataframe
			rename_dict = {'sig_id': 'Signature ID', 'pvals': 'P-value', 'qvals': 'FDR', 'zscores': 'Z-score', 'combined_scores': 'Combined Score'}
			signature_dataframe = pd.DataFrame(signature_list)[list(rename_dict.keys())].rename(columns=rename_dict).sort_values('P-value').rename_axis('Rank')
			signature_dataframe.index = [x + 1 for x in range(len(signature_dataframe.index))]
			signature_txt = signature_dataframe.to_csv(sep='\t')

			# Display table
			pd.set_option('max.colwidth', -1)
			signature_dataframe['Signature ID'] = ['<a href="http://amp.pharm.mssm.edu/dmoa/sig/{x}" target="_blank">{x}</a>'.format(**locals()) for x in signature_dataframe['Signature ID']]
			table_html = signature_dataframe.to_html(escape=False, classes='w-100')
			display(Markdown('** {} Signatures: **'.format(direction.title())))
			display(HTML('<style>.w-100{{width: 100% !important;}}</style><div style="max-height: 250px; overflow-y: auto; margin-bottom: 25px;">{}</div>'.format(table_html)))

			# Display download button
			download_button(signature_txt, 'Download {} Signatures'.format(direction.title()), 'L1000FWD {direction} signatures - {signature_label}.txt'.format(**l1000fwd_results, **locals()))

		# Link
		display(HTML('Full results available at: <a href="{result_url}" target="_blank">{result_url}</a>.'.format(**l1000fwd_results)))

	# Display error
	else:
		display(Markdown('### No results were found.\n This is likely due to the fact that the gene identifiers were not recognized by L1000FWD. Please note that L1000FWD currently only supports HGNC gene symbols (https://www.genenames.org/). If your dataset uses other gene identifier systems, such as Ensembl IDs or Entrez IDs, consider converting them to HGNC. Automated gene identifier conversion is currently under development.'))


