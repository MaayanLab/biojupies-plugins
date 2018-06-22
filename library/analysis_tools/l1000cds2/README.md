<img src="img/l1000cds2-icon.png" width="50px"> L1000CDS<sup>2</sup> Query
================

Overview
----------------
L1000CDS2 is a web-based tool for querying gene expression signatures against signatures created from human cell lines treated with over 20,000 small molecules and drugs for the LINCS project. It is commonly used to identify small molecules which mimic or reverse the effects of a gene expression signature generated from a differential gene expression analysis.

How to Use the Plug-in
----------------
### Running the Analysis
```python
# Run L1000CDS<sup>2</sup> Query
l1000cds2_results = l1000cds2.run(dataset)
```

**Parameters**


### Plotting the Results
```python
# Plot L1000CDS<sup>2</sup> Query results
l1000cds2.plot(l1000cds2_results)
```
<img src="img/l1000cds2-example.png"> 
The L1000CDS<sup>2</sup> plug-in embeds an interactive bar chart displaying the top small molecules which mimic or reverse the input gene expression signature.

Methods
----------------
The L1000CDS2 analysis (<a href='#10.1038/npjsba.2016.15'>Duan et al., 2016</a>) was performed by submitting the top 2000 genes in the gene expression signature to the <a href='http://amp.pharm.mssm.edu/L1000CDS2/#/index' target='_blank'>L1000CDS2</a> signature search API. For more information on the methods used to generate the signature, see the Differential Gene Expression section.