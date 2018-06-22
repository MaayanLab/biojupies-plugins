![t-SNE](img/tsne-icon.png?s=50 "t-SNE") t-SNE
================
Summary
----------------
Nonlinear dimensionality reduction technique to visualize similarity between samples

Introduction
----------------
t-distributed Stochastic Neighbor Embedding (t-SNE) (Van Der Maaten and Hinton, Journal of Machine Learning Research 2008) is a nonlinear dimensionality reduction technique which can project high-dimensional data in lower dimensions by minimizing distances between near points and maximizing distances between far points.

Results
----------------


Methods
----------------
t-SNE analysis was performed using the `TSNE` function from the `sklearn` Python module, available here: http://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html. Prior to performing t-SNE, the dataset was normalized using the zscore method, and a subset of the top {nr_genes} most variably expressed genes was used for the t-SNE analysis.