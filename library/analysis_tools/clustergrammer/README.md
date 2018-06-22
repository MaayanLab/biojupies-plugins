<img src="img/clustergrammer-icon.png" width="50px"> Clustergrammer
================

Overview
----------------
Clustergrammer is a web-based tool for visualizing and analyzing high-dimensional data as interactive and hierarchically clustered heatmaps.  It is commonly used to explore the similarity between samples in an RNA-seq dataset. In addition to identifying clusters of samples, it also allows to identify the genes which contribute to the clustering.

How to Use the Plug-in
----------------
### Running the Analysis
```python
# Run Clustergrammer
clustergrammer_results = clustergrammer.run(dataset, nr_genes=2500, normalization=logCPM, z_score=True)
```

**Parameters**

| Name | Type | Values | Description |
| ---- | ---- | ------ | ----------- |
| **nr_genes** | *int* | *500, 2500 (default), 5000* | Number of most variably expressed genes to use for the analysis |
| **normalization** | *str* | *logCPM (default), quantile, VST* | Normalization method for the dataset |
| **z_score** | *bool* | *True (default), False* | Whether to perform Z-score on the rows of the normalized dataset |


### Plotting the Results
```python
# Plot Clustergrammer results
clustergrammer.plot(clustergrammer_results)
```
<img src="img/clustergrammer-example.png"> 
The Clustergrammer plug-in embeds an interactive heatmap which displays gene expression for each sample in the RNA-seq dataset. Every row of the heatmap represents a gene, every column represents a sample, and every cell displays normalized gene expression values. The heatmap additionally features color bars beside each column which represent prior knowledge of each sample  for example, the tissue of origin or experimental treatment

Methods
----------------
The interactive heatmap was generated using Clustergrammer (<a href='#10.1038/sdata.2017.151'>Fernandez et al., 2017</a>) which is freely available at http://amp.pharm.mssm.edu/clustergrammer/. Prior to displaying the heatmap, the raw gene counts were normalized using the {normalization} method, filtered by selecting the {nr_genes} genes with most variable expression, and finally transformed using the Z-score method.