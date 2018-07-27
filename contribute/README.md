# Plugin Contribution Guide
Step-by-step guide illustrating how users can contribute RNA-seq analysis tools for integration into BioJupies (http://biojupies.cloud). Once integrated, the plugins are made available for notebook generation on the BioJupies website.

### Overview
1. [What are BioJupies plugins?](#what-are-biojupies-plugins)
2. [How do I submit a plugin?](#how-do-i-submit-a-plugin)
2. [Contact Us](#contact-us)

## What are BioJupies plugins?
BioJupies plugins are modular snippets of code which can analyze RNA-seq data and embed visualizations, interactive plots, or analysis results in Jupyter Notebooks.

Plugins may perform a variety of different analyses, ranging from exploratory data analysis visualizations, differential gene expression, clustering, enrichment analysis, and small molecule queries.

The full list of currently available plugins is available [here](https://github.com/MaayanLab/biojupies-plugins#what-plugins-are-currently-available).

## How do I submit a plugin?
To submit your RNA-seq analysis tool as a plugin, follow the instructions below:

1. **Download one of the following files** from the GitHub repository:
    * The **Python Jupyter Notebook** ([python3_notebook.ipynb](https://github.com/MaayanLab/biojupies-plugins/blob/master/contribute/python3_notebook.ipynb)), for plugins written in Python 3.
    * The **R Jupyter Notebook** ([r_notebook.ipynb](https://github.com/MaayanLab/biojupies-plugins/blob/master/contribute/r_notebook.ipynb)), for plugins written in R.

2. **Add your RNA-seq analysis code** following the instructions in the notebook. The code should be divided into two functions:
    * An `analyze` function, which takes an RNA-seq dataset or gene signature as input, and returns the results of the analysis (e.g. as a dataframe, a list, or dictionary).
    * A `plot` function, which takes the output of the `analyze` function and displays by embedding a plot, table, or any type of interactive visualization in the notebook.

3. **Upload the notebook to GitHub**. You can add the notebook to your personal GitHub repository, or create a new fork in the [MaayanLab/biojupies-plugins](https://github.com/MaayanLab/biojupies-plugins) repository.

4. **Fill the submission form** on the BioJupies website: https://amp.pharm.mssm.edu/biojupies/contribute. You will be add to specify a link to the notebook on GitHub, a contact email, and a brief description of the plugin.

5. **We will notify you** on the status of the submission. Once completed, your plugin will be made available on the BioJupies website (http://biojupies.cloud) for Jupyter Notebook generation.

## Contact Us
For more information or questions about submitting plugins, contact us at avi.maayan@mssm.edu or [open an Issue](https://github.com/MaayanLab/biojupies-plugins/issues/new) on the GitHub repository. 