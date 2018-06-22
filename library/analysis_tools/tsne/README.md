<img src="img/tsne-icon.png" width="50px"> t-SNE Plug-in
================

Overview
----------------
t-distributed Stochastic Neighbor Embedding (t-SNE) (Van Der Maaten and Hinton, Journal of Machine Learning Research 2008) is a nonlinear dimensionality reduction technique which can project high-dimensional data in lower dimensions by minimizing distances between near points and maximizing distances between far points.

Usage
----------------
### Running the Analysis
```python
# Run t-SNE
tsne_results = tsne.run(dataset, nr_genes=2500, normalization=logCPM, z_score=True)
```

**Parameters**

| Name | Type | Values | Description |
| ---- | ---- | ------ | ----------- |
| **nr_genes** | *int* | *500, 2500 (default), 5000* | Number of most variably expressed genes to use for the analysis. |
| **normalization** | *str* | *logCPM (default), quantile, VST* | Normalization method for the dataset. |
| **z_score** | *bool* | *True (default), False* | Whether to perform Z-score on the rows of the normalized dataset. |


### Plotting the Results
```python
# Plot t-SNE results
tsne.plot(tsne_results)
```
<img src="img/tsne-example.png"> 
