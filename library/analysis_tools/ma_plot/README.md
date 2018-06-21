MA Plot
================
Summary
----------------
Plot the logFC and average expression values resulting from a differential expression analysis

Introduction
----------------
Volcano plots are a type of scatter plot commonly used to display the results of a differential gene expression analysis. They can be used to quickly identify genes whose expression is significantly altered in a perturbation, and to assess the global similarity of gene expression in two groups of biological samples. Each point in the scatter plot represents a gene; the axes display the average gene expression versus fold-change estimated by the differential expression analysis.

Results
----------------
The MA Plot plug-in embeds an interactive scatter plot which displays the average expression and statistical significance of each gene calculated by performing differential gene expression analysis comparing samples in the Control group to samples in the Perturbation group. Every point in the plot represents a gene; additional information for each gene is available by hovering over it.

Methods
----------------
Average gene expression was identified by calculating the mean of the normalized gene expression values and displayed on the x axis; P-values were corrected using the Benjamini-Hochberg method, transformed using log10, and displayed on the y axis. For more information on the methods used to generate the signature, see the Differential Gene Expression section.