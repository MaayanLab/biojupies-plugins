#################################################################
#################################################################
############### PCA 
#################################################################
#################################################################

#############################################
########## 1. Load libraries
#############################################
##### 1. General support #####
from sklearn.decomposition import PCA
import plotly.graph_objs as go
from plotly.offline import iplot

##### 2. Other libraries #####

#######################################################
#######################################################
########## S1. Function
#######################################################
#######################################################

#############################################
########## 1. Run
#############################################

def run(dataset, dimensions=3, nr_genes=2500, normalization='zscore', color_by=None, color_type='categorical'):

	# Get expression
	expression_dataframe = dataset[normalization]

	# Filter
	expression_dataframe = expression_dataframe.loc[expression_dataframe.var(axis=1).sort_values(ascending=False).index[:nr_genes]]

	# Run PCA
	pca=PCA(n_components=3)
	pca.fit(expression_dataframe)

	# Get Variance
	var_explained = ['PC'+str((i+1))+'('+str(round(e*100, 1))+'% var. explained)' for i, e in enumerate(pca.explained_variance_ratio_)]

	# Add colors
	if dataset.get('signature_metadata'):
		A_label, B_label = list(dataset['signature_metadata'].keys())[0].split(' vs ')
		col = []
		group_dict = list(dataset['signature_metadata'].values())[0]
		for gsm in dataset['sample_metadata'].index:
			if gsm in group_dict['A']:
				col.append(A_label)
			elif gsm in group_dict['B']:
				col.append(B_label)
			else:
				col.append('Other')
		dataset['sample_metadata']['Group'] = col
		color_by = 'Group'
		color_type = 'categorical'

	# Return
	pca_results = {'pca': pca, 'var_explained': var_explained, 'sample_metadata': dataset['sample_metadata'].loc[expression_dataframe.columns], 'color_by': color_by, 'color_type': color_type, 'nr_genes': nr_genes}
	return pca_results

#############################################
########## 2. Plot
#############################################

def plot(pca_results):

	# Get results
	pca = pca_results['pca']
	var_explained = pca_results['var_explained']
	sample_metadata = pca_results['sample_metadata']
	color_by = pca_results.get('color_by')
	color_type = pca_results.get('color_type')
	color_column = pca_results['sample_metadata'][color_by] if color_by else None
	colors = ['#a6cee3','#1f78b4','#b2df8a','#33a02c','#fb9a99','#e31a1c','#fdbf6f','#ff7f00','#cab2d6','#6a3d9a','#ffff99','#b15928']
	sample_titles = ['<b>{}</b><br>'.format(index)+'<br>'.join('<i>{key}</i>: {value}'.format(**locals()) for key, value in rowData.items()) for index, rowData in sample_metadata.iterrows()]

	if not color_by:
		marker = dict(size=15)
		trace = go.Scatter3d(x=pca.components_[0],
							 y=pca.components_[1],
							 z=pca.components_[2],
							 mode='markers',
							 hoverinfo='text',
							 text=sample_titles,
							 marker=marker)
		data = [trace]
	elif color_by and color_type == 'continuous':
		marker = dict(size=15, color=color_column, colorscale='Viridis', showscale=True)
		trace = go.Scatter3d(x=pca.components_[0],
							 y=pca.components_[1],
							 z=pca.components_[2],
							 mode='markers',
							 hoverinfo='text',
							 text=sample_titles,
							 marker=marker)
		data = [trace]
	elif color_by and color_type == 'categorical':
		# Get unique categories
		unique_categories = color_column.unique()

		# Define empty list
		data = []
			
		# Loop through the unique categories
		for i, category in enumerate(unique_categories):

			# Get the color corresponding to the category
			category_color = colors[i]

			# Get the indices of the samples corresponding to the category
			category_indices = [i for i, sample_category in enumerate(color_column) if sample_category == category]
			
			# Create new trace
			trace = go.Scatter3d(x=pca.components_[0][category_indices],
								 y=pca.components_[1][category_indices],
								 z=pca.components_[2][category_indices],
								 mode='markers',
								 hoverinfo='text',
								 text=[sample_titles[x] for x in category_indices],
								 name = category,
								 marker=dict(size=15, color=category_color))
			
			# Append trace to data list
			data.append(trace)
	
	colored = '' if str(color_by) == 'None' else '<i>, colored by {}</i>'.format(color_by)
	layout = go.Layout(title='<b>PCA Analysis | Scatter Plot</b><br><i>Top {} variable genes</i>'.format(pca_results['nr_genes'])+colored, hovermode='closest', margin=go.Margin(l=0,r=0,b=0,t=50), width=900,
		scene=dict(xaxis=dict(title=var_explained[0]), yaxis=dict(title=var_explained[1]),zaxis=dict(title=var_explained[2])))
	fig = go.Figure(data=data, layout=layout)

	return iplot(fig)
