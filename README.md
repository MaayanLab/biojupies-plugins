BioJupies Plug-ins
================
Overview
----------------
BioJupies (http://biojupies.cloud) is a web server for the automated generation of interactive notebooks for RNA-seq data analysis in the cloud through a simple user interface.

To generate notebooks, BioJupies uses a modular set plug-ins which analyze RNA-seq data and embed the results using interactive plots and data visualizations. Source code for all plug-ins is stored in this GitHub repository.

Source code for the BioJupies Jupyter Notebook generation server is available at: https://github.com/MaayanLab/biojupies.

The Plug-ins
----------------
The BioJupies RNA-seq analysis toolbox currently contains the following plug-ins:

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

Contributing your Plug-ins
----------------
Users are welcome to contribute RNA-seq data analysis plug-ins for integration in BioJupies.

To contribute your plug-in, follow our [plug-in submission tutorial](https://amp.pharm.mssm.edu/biojupies/contribute).

Citation
----------------
[BioJupies: Automated Generation of Interactive Notebooks for RNA-seq Data Analysis in the Cloud](https://doi.org/10.1101/352476) Torre, D., Lachmann, A., and Ma’ayan, A. (2018)