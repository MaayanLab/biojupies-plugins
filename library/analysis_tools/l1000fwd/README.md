<img src="img/l1000fwd-icon.png" width="50px"> L1000FWD Query Plug-in
================

Overview
----------------
L1000FWD is a web-based tool for querying gene expression signatures against signatures created from human cell lines treated with over 20,000 small molecules and drugs for the LINCS project.

Usage
----------------
### Running the Analysis
```python
# Run L1000FWD Query
l1000fwd_results = l1000fwd.run(signature)
```


### Plotting the Results
```python
# Plot L1000FWD Query results
l1000fwd.plot(l1000fwd_results)
```
<img src="img/l1000fwd-example.png"> 
The L1000CDS<sup>2</sup> plug-in embeds an interactive projection of the top most similar and opposite signatures from the L1000 database on a 2-dimensional plane.