PCA
================
Summary
----------------
Linear dimensionality reduction technique to visualize similarity between samples

Introduction
----------------
Principal Component Analysis (PCA) is a statistical technique used to identify global patterns in high-dimensional datasets. It is commonly used to explore the similarity of biological samples in RNA-seq datasets. To achieve this, gene expression values are transformed into Principal Components (PCs), a set of linearly uncorrelated features which represent the most relevant sources of variance in the data, and subsequently visualized using a scatter plot.

Results
----------------
The PCA plug-in embeds an interactive, three-dimensional scatter plot of the first three Principal Components (PCs) of the data. Each point represents an RNA-seq sample. Samples with similar gene expression profiles are closer in the three-dimensional space. If provided, sample groups are indicated using different colors, thus allowing for easier interpretation of the results.

Methods
----------------
Principal Component Analysis was performed using the PCA function from in the sklearn Python module. Prior to performing PCA, the raw gene counts were normalized using the {normalization} method, filtered by selecting the {nr_genes} genes with most variable expression, and finally transformed using the Z-score method.