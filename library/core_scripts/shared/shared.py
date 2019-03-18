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
import requests
import json
import pandas as pd
import numpy as np
from plotly import tools
from plotly.offline import iplot
import plotly.graph_objs as go
from IPython.display import display, Markdown, HTML
import plotly.plotly as py

#######################################################
#######################################################
########## S1. Generic Plots
#######################################################
#######################################################

#############################################
########## 1. Download Button
#############################################

def download_button(content, label, filename):
	# Add download button
	outname = filename.split('.')[0]
	display(HTML('<textarea id="textbox_{outname}" style="display: none;">{content}</textarea> <button id="create_{outname}">{label}</button> <a download="{filename}" id="downloadlink_{outname}" style="display: none">Download</a>'.format(**locals())))
	display(HTML('<script type="text/javascript">!function(){{var e=null,t=document.getElementById("create_{outname}"),n=document.getElementById("textbox_{outname}");t.addEventListener("click",function(){{var t,l,c=document.getElementById("downloadlink_{outname}");c.href=(t=n.value,l=new Blob([t],{{type:"text/plain"}}),null!==e&&window.URL.revokeObjectURL(e),e=window.URL.createObjectURL(l)),c.click()}},!1)}}();</script>'.format(**locals())))

#############################################
########## 2. Static Plot
#############################################

def static_plot(fig):
	py.sign_in('denis-torre', '1w2EWVWYx2Wjo9MMdKpf')
	py.image.ishow(fig)

#############################################
########## 3. 2D Scatter
#############################################

def plot_2D_scatter(x, y, text='', title='', xlab='', ylab='', hoverinfo='text', color='black', colorscale='Blues', size=8, showscale=False, symmetric_x=False, symmetric_y=False, pad=0.5, hline=False, vline=False, return_trace=False, labels=False, plot_type='interactive', de_type='ma'):
	range_x = [-max(abs(x))-pad, max(abs(x))+pad]if symmetric_x else []
	range_y = [-max(abs(y))-pad, max(abs(y))+pad]if symmetric_y else []
	trace = go.Scattergl(x=x, y=y, mode='markers', text=text, hoverinfo=hoverinfo, marker={'color': color, 'colorscale': colorscale, 'showscale': showscale, 'size': size})
	if return_trace:
		return trace
	else:
		if de_type == 'ma':
			annotations = [
				{'x': 1, 'y': 0.1, 'text':'<span style="color: blue; font-size: 10pt; font-weight: 600;">Down-regulated in '+labels[-1]+'</span>', 'showarrow': False, 'xref': 'paper', 'yref': 'paper', 'xanchor': 'right', 'yanchor': 'top'},
				{'x': 1, 'y': 0.9, 'text':'<span style="color: red; font-size: 10pt; font-weight: 600;">Up-regulated in '+labels[-1]+'</span>', 'showarrow': False, 'xref': 'paper', 'yref': 'paper', 'xanchor': 'right', 'yanchor': 'bottom'}
			] if labels else []
		elif de_type == 'volcano':
			annotations = [
				{'x': 0.25, 'y': 1.07, 'text':'<span style="color: blue; font-size: 10pt; font-weight: 600;">Down-regulated in '+labels[-1]+'</span>', 'showarrow': False, 'xref': 'paper', 'yref': 'paper', 'xanchor': 'center'},
				{'x': 0.75, 'y': 1.07, 'text':'<span style="color: red; font-size: 10pt; font-weight: 600;">Up-regulated in '+labels[-1]+'</span>', 'showarrow': False, 'xref': 'paper', 'yref': 'paper', 'xanchor': 'center'}
			] if labels else []
		layout = go.Layout(title=title, xaxis={'title': xlab, 'range': range_x}, yaxis={'title': ylab, 'range': range_y}, hovermode='closest', annotations=annotations)
		fig = go.Figure(data=[trace], layout=layout)
	
	if plot_type=='interactive':
		iplot(fig)
	else:
		static_plot(fig)

#######################################################
#######################################################
########## S3. Enrichr
#######################################################
#######################################################

#############################################
########## 1. Get Enrichr Results
#############################################

def get_enrichr_results(user_list_id, gene_set_libraries, overlappingGenes=True, geneset=None):
	ENRICHR_URL = 'http://amp.pharm.mssm.edu/Enrichr/enrich'
	query_string = '?userListId=%s&backgroundType=%s'
	results = []
	for gene_set_library, label in gene_set_libraries.items():
		response = requests.get(
                    ENRICHR_URL +
                   	query_string % (user_list_id, gene_set_library)
                )
		if not response.ok:
			raise Exception('Error fetching enrichment results')

		data = json.loads(response.text)
		resultDataframe = pd.DataFrame(data[gene_set_library], columns=[
		                               'rank', 'term_name', 'pvalue', 'zscore', 'combined_score', 'overlapping_genes', 'FDR', 'old_pvalue', 'old_FDR'])
		selectedColumns = ['term_name', 'zscore', 'combined_score', 'pvalue', 'FDR'] if not overlappingGenes else [
			'term_name', 'zscore', 'combined_score', 'FDR', 'pvalue', 'overlapping_genes']
		resultDataframe = resultDataframe.loc[:, selectedColumns]
		resultDataframe['gene_set_library'] = label
		resultDataframe['log10P'] = -np.log10(resultDataframe['pvalue'])
		results.append(resultDataframe)
	concatenatedDataframe = pd.concat(results)
	if geneset:
		concatenatedDataframe['geneset'] = geneset
	return concatenatedDataframe

#############################################
########## 2. Plot Enrichment Barchart
#############################################

def plot_library_barchart(enrichr_results, gene_set_library, signature_label, nr_genesets, height):
	fig = tools.make_subplots(rows=1, cols=2, print_grid=False)
	for i, geneset in enumerate(['upregulated', 'downregulated']):
		# Get dataframe
		enrichment_dataframe = enrichr_results[geneset]
		plot_dataframe = enrichment_dataframe[enrichment_dataframe['gene_set_library'] == gene_set_library].sort_values(
			'pvalue', ascending=True).iloc[:nr_genesets].iloc[::-1]

		# Format
		n = 7
		plot_dataframe['nr_genes'] = [len(genes) for genes in plot_dataframe['overlapping_genes']]
		plot_dataframe['overlapping_genes'] = ['<br>'.join([', '.join(genes[i:i+n]) for i in range(0, len(genes), n)]) for genes in plot_dataframe['overlapping_genes']]

		# Get Bar
		bar = go.Bar(
			x=plot_dataframe['log10P'],
			y=plot_dataframe['term_name'],
			orientation='h',
			name=geneset.title(),
			showlegend=False,
			hovertext=['<b>{term_name}</b><br><b>P-value</b>: <i>{pvalue:.2}</i><br><b>FDR</b>: <i>{FDR:.2}</i><br><b>Z-score</b>: <i>{zscore:.3}</i><br><b>Combined score</b>: <i>{combined_score:.3}</i><br><b>{nr_genes} Genes</b>: <i>{overlapping_genes}</i><br>'.format(**rowData) for index, rowData in plot_dataframe.iterrows()],
			hoverinfo='text',
			marker={'color': '#FA8072' if geneset == 'upregulated' else '	#87CEFA'}
		)
		fig.append_trace(bar, 1, i+1)

		# Get text
		text = go.Scatter(
			x=[max(bar['x'])/50 for x in range(len(bar['y']))],
			y=bar['y'],
			mode='text',
			hoverinfo='none',
			showlegend=False,
			text=['*<b>{}</b>'.format(rowData['term_name']) if rowData['FDR'] < 0.1 else '{}'.format(
				rowData['term_name']) for index, rowData in plot_dataframe.iterrows()],
			textposition="middle right",
			textfont={'color': 'black'}
		)
		fig.append_trace(text, 1, i+1)

	# Get annotations
	labels = signature_label.split('vs ')
	annotations = [
		{'x': 0.25, 'y': 1.12, 'text': '<span style="color: #FA8072; font-size: 10pt; font-weight: 600;">Up-regulated in ' +
			labels[-1]+'</span>', 'showarrow': False, 'xref': 'paper', 'yref': 'paper', 'xanchor': 'center'},
		{'x': 0.75, 'y': 1.12, 'text': '<span style="color: #87CEFA; font-size: 10pt; font-weight: 600;">Down-regulated in ' +
			labels[-1]+'</span>', 'showarrow': False, 'xref': 'paper', 'yref': 'paper', 'xanchor': 'center'}
	] if signature_label else []

	# Get title
	title = signature_label + ' | ' + gene_set_library

	fig['layout'].update(height=height, title='<b>{}</b>'.format(title),
	                     hovermode='closest', annotations=annotations)
	fig['layout']['xaxis1'].update(domain=[0, 0.49], title='')
	fig['layout']['xaxis2'].update(domain=[0.51, 1], title='')
	fig['layout']['yaxis1'].update(showticklabels=False)
	fig['layout']['yaxis2'].update(showticklabels=False)
	fig['layout']['margin'].update(l=0, t=65, r=0, b=30)
	if enrichr_results['plot_type']=='interactive':
		iplot(fig)
	else:
		static_plot(fig)

	# Add download button from enrichr_results
	# download_button(enrichment_results.to_csv(sep='\t'), 'Download Enrichment Results', 'enrichment.txt')

#############################################
########## 3. Display Result Table
#############################################

def results_table(enrichment_dataframe, source_label, target_label):

	# Get libraries
	for gene_set_library in enrichment_dataframe['gene_set_library'].unique():

		# Get subset
		enrichment_dataframe_subset = enrichment_dataframe[enrichment_dataframe['gene_set_library'] == gene_set_library].copy()

		# Get unique values from source column
		enrichment_dataframe_subset[source_label] = [x.split('_')[0] for x in enrichment_dataframe_subset['term_name']]
		enrichment_dataframe_subset = enrichment_dataframe_subset.sort_values(['FDR', 'pvalue']).rename(columns={'pvalue': 'P-value'}).drop_duplicates(source_label)

		# Add links and bold for significant results
		enrichment_dataframe_subset[source_label] = ['<a href="http://www.mirbase.org/cgi-bin/query.pl?terms={x}" target="_blank">{x}</a>'.format(**locals()) if '-miR-' in x else '<a href="http://amp.pharm.mssm.edu/Harmonizome/gene/{x}" target="_blank">{x}</a>'.format(**locals())for x in enrichment_dataframe_subset[source_label]]
		enrichment_dataframe_subset[source_label] = [rowData[source_label].replace('target="_blank">', 'target="_blank"><b>').replace('</a>', '*</b></a>') if rowData['FDR'] < 0.05 else rowData[source_label] for index, rowData in enrichment_dataframe_subset.iterrows()]

		# Add rank
		enrichment_dataframe_subset['Rank'] = ['<b>'+str(x+1)+'</b>' for x in range(len(enrichment_dataframe_subset.index))]

		# Add overlapping genes with tooltip
		enrichment_dataframe_subset['nr_overlapping_genes'] = [len(x) for x in enrichment_dataframe_subset['overlapping_genes']]
		enrichment_dataframe_subset['overlapping_genes'] = [', '.join(x) for x in enrichment_dataframe_subset['overlapping_genes']]
		enrichment_dataframe_subset[target_label.title()] = ['{nr_overlapping_genes} {geneset} '.format(**rowData)+target_label+'s' for index, rowData in enrichment_dataframe_subset.iterrows()]
		# enrichment_dataframe[target_label.title()] = ['<span class="gene-tooltip">{nr_overlapping_genes} {geneset} '.format(**rowData)+target_label+'s<div class="gene-tooltip-text">{overlapping_genes}</div></span>'.format(**rowData) for index, rowData in enrichment_dataframe.iterrows()]

		# Convert to HTML
		pd.set_option('max.colwidth', -1)
		html_table = enrichment_dataframe_subset.head(50)[['Rank', source_label, 'P-value', 'FDR', target_label.title()]].to_html(escape=False, index=False, classes='w-100')
		html_results = '<div style="max-height: 200px; overflow-y: scroll;">{}</div>'.format(html_table)

		# Add CSS
		display(HTML('<style>.w-100{width: 100%;} .text-left th{text-align: left !important;}</style>'))
		display(HTML('<style>.slick-cell{overflow: visible;}.gene-tooltip{text-decoration: underline; text-decoration-style: dotted;}.gene-tooltip .gene-tooltip-text{visibility: hidden; position: absolute; left: 60%; width: 250px; z-index: 1000; text-align: center; background-color: black; color: white; padding: 5px 10px; border-radius: 5px;} .gene-tooltip:hover .gene-tooltip-text{visibility: visible;} .gene-tooltip .gene-tooltip-text::after {content: " ";position: absolute;bottom: 100%;left: 50%;margin-left: -5px;border-width: 5px;border-style: solid;border-color: transparent transparent black transparent;}</style>'))

		# Display gene set
		display(Markdown(gene_set_library))

		# Display table
		display(HTML(html_results))

		# Download enrichment results from enrichment_dataframe
		# download_button(enrichment_results.to_csv(sep='\t'), 'Download Enrichment Results', 'enrichment.txt')
