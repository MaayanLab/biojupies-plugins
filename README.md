# BioJupies Plugins
RNA-seq data analysis plugins for the BioJupies project (http://biojupies.cloud).

### Overview
1. [What is BioJupies?](#what-is-biojupies)
2. [What are BioJupies plugins?](#what-are-biojupies-plugins)
3. [What plugins are currently available?](#what-plugins-are-currently-available)
4. [Can I contribute my RNA-seq analysis plugins?](#can-i-contribute-my-rna-seq-analysis-plugins)
4. [References](#references)

## What is BioJupies?
BioJupies is a web server which allows users to automatically generate Jupyter Notebooks from RNA-seq datasets through an intuitive interface, with no knowledge of coding required. It can be accessed for free from http://biojupies.cloud.

The main GitHub repository for the project is available at https://github.com/MaayanLab/biojupies. This repository is dedicated to storing RNA-seq data analysis plugins.

![Screenshot of the BioJupies website landing page.](https://github.com/MaayanLab/biojupies/raw/master/img/website.png)

### What are BioJupies plugins?
BioJupies plugins are modular snippets of code which can analyze RNA-seq data and embed a wide variety of visualizations, interactive plots, or results in Jupyter Notebooks.

## What plugins are currently available?
----------------
The BioJupies RNA-seq analysis toolbox currently contains the following plugins:

| Plug-in Name | Description |
| --- | --- |
| [PCA](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/pca) | Linear dimensionality reduction technique to visualize similarity between samples |
| [Clustergrammer](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/clustergrammer) | Interactive hierarchically clustered heatmap |
| [Library Size Analysis](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/library_size_analysis) | Analysis of readcount distribution for the samples within the dataset |
| [Signature Table](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/signature_table) | Differential expression analysis between two groups of samples |
| [Volcano Plot](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/volcano_plot) | Plot the logFC and logP values resulting from a differential expression analysis |
| [MA Plot](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/ma_plot) | Plot the logFC and average expression values resulting from a differential expression analysis |
| [Enrichr](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/enrichr) | Links to enrichment analysis results of the differentially expressed genes via Enrichr |
| [Gene Ontology Enrichment Analysis](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/go_enrichment) | Gene Ontology terms enriched in the differentially expressed genes (via Enrichr) |
| [Pathway Enrichment Analysis](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/pathway_enrichment) | Biological pathways enriched in the differentially expressed genes (via Enrichr) |
| [Transcription Factor Enrichment Analysis](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/tf_enrichment) | Transcription factors whose targets are enriched in the differentially expressed genes (via Enrichr) |
| [Kinase Enrichment Analysis](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/kinase_enrichment) | Protein kinases whose substrates are enriched in the differentially expressed genes (via Enrichr) |
| [miRNA Enrichment Analysis](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/mirna_enrichment) | miRNAs whose targets are enriched in thedifferentially expressed genes (via Enrichr) |
| [L1000CDS2 Query](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/l1000cds2) | Small molecules which mimic or reverse a given differential gene expression signature |
| [L1000FWD Query](https://github.com/MaayanLab/biojupies-plugins/tree/master/library/analysis_tools/l1000fwd) | Small molecules which mimic or reverse a given differential gene expression signature |


## Can I contribute my RNA-seq analysis plugins?
Users are welcome to contribute RNA-seq data analysis plugins for integration in BioJupies.

To contribute your plugin, follow our [submission tutorial](https://amp.pharm.mssm.edu/biojupies/contribute).

## References
[BioJupies: Automated Generation of Interactive Notebooks for RNA-seq Data Analysis in the Cloud](https://doi.org/10.1101/352476) Torre, D., Lachmann, A., and Ma’ayan, A. (2018)

## License
This project is licensed under the Apache-2.0 License - see the [LICENSE.md](LICENSE.md) file for details