# BioJupies Plugins
![Notebooks Generated](https://img.shields.io/badge/dynamic/json.svg?url=https://amp.pharm.mssm.edu/biojupies-dev/api/stats?obj=notebook&label=notebooks%20generated&query=$.n&colorB=blue)
![Datasets Available](https://img.shields.io/badge/dynamic/json.svg?url=https://amp.pharm.mssm.edu/biojupies-dev/api/stats?obj=dataset_v5&label=RNA-seq%20datasets%20available&query=$.n&colorB=green)
![Plugins](https://img.shields.io/badge/dynamic/json.svg?url=https://amp.pharm.mssm.edu/biojupies-dev/api/stats?obj=tool&label=analysis%20plugins&query=$.n&colorB=yellow)

RNA-seq data analysis plugins for the BioJupies project (http://biojupies.cloud).

Source code for the BioJupies web server available at https://github.com/MaayanLab/biojupies.

### Overview
1. [What is BioJupies?](#what-is-biojupies)
2. [What are BioJupies plugins?](#what-are-biojupies-plugins)
3. [What plugins are currently available?](#what-plugins-are-currently-available)
4. [Can I contribute my RNA-seq analysis plugins?](#can-i-contribute-my-rna-seq-analysis-plugins)
4. [References](#references)

## What is BioJupies?
BioJupies is a web server which allows users to automatically generate Jupyter Notebooks from RNA-seq datasets through an intuitive interface, with no knowledge of coding required. It can be accessed for free from http://biojupies.cloud.

![Screenshot of the BioJupies website landing page.](https://github.com/MaayanLab/biojupies/raw/master/img/website.png)

## What are BioJupies plugins?
BioJupies plugins are modular snippets of code which can analyze RNA-seq data and embed visualizations, interactive plots, or analysis results in Jupyter Notebooks.

Plugins may perform a variety of different analyses, ranging from exploratory data analysis visualizations, differential gene expression, clustering, enrichment analysis, and small molecule queries. A full list of the plugins available is displayed below.

BioJupies currently supports plugins written in Python 3 and R.

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