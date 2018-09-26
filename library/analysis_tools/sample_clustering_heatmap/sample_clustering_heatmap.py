#################################################################
#################################################################
############### DE 
#################################################################
#################################################################

#############################################
########## 1. Load libraries
#############################################
##### 1. General support #####
import numpy as np
import plotly.graph_objs as go
from plotly.offline import iplot
from IPython.display import display, Markdown
import sys, os

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

def run(signature, signature_label='', pvalue_threshold=0.05, logfc_threshold=1.5, plot_type='interactive'):

	# Loop through signature
	color = []
	text = []
	for index, rowData in signature.iterrows():

		# Text
		text.append('<b>'+index+'</b><br>Avg Expression = '+str(round(rowData['AveExpr'], ndigits=2))+'<br>logFC = '+str(round(rowData['logFC'], ndigits=2))+'<br>p = '+'{:.2e}'.format(rowData['P.Value'])+'<br>FDR = '+'{:.2e}'.format(rowData['adj.P.Val']))

		# Color
		if rowData['P.Value'] < pvalue_threshold:
		# if rowData['adj.P.Val'] < 0.05:
			if rowData['logFC'] < -logfc_threshold:
				color.append('blue')
			elif rowData['logFC'] > logfc_threshold:
				color.append('red')
			else:
				color.append('black')

		else:
			color.append('black')
	
	# Return 
	volcano_plot_results = {'x': signature['logFC'], 'y': -np.log10(signature['P.Value']), 'text':text, 'color': color, 'signature_label': signature_label, 'plot_type': plot_type}
	return volcano_plot_results

#############################################
########## 2. Plot
#############################################

def plot(volcano_plot_results, plot_counter):
	spacer = ' '*50
	plot_2D_scatter(
		x=volcano_plot_results['x'],
		y=volcano_plot_results['y'],
		text=volcano_plot_results['text'],
		color=volcano_plot_results['color'],
		symmetric_x=True,
		xlab='log2FC',
		ylab='-log10P',
		title='<b>{volcano_plot_results[signature_label]} Signature | Volcano Plot</b>'.format(**locals()),
		labels=volcano_plot_results['signature_label'].split(' vs '),
		plot_type=volcano_plot_results['plot_type'],
		de_type='volcano'
	)

	# Figure Legend
	display(Markdown('** Figure '+plot_counter()+' | Volcano Plot. **The figure contains an interactive scatter plot which displays the log2-fold changes and statistical significance of each gene calculated by performing a differential gene expression analysis. Every point in the plot represents a gene. Red points indicate significantly up-regulated genes, blue points indicate down-regulated genes. Additional information for each gene is available by hovering over it. If you are experiencing issues visualizing the plot, please visit our <a href="https://amp.pharm.mssm.edu/biojupies/help#troubleshooting" target="_blank">Troubleshooting guide</a>.'.format(**locals())))
