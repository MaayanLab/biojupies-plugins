#################################################################
#################################################################
############### BioJupies Plug-in Submission Template ########### 
#################################################################
#################################################################

#############################################
########## 1. Import libraries
#############################################
##### 1. Python libraries #####
import pandas as pd
import numpy as np

#######################################################
#######################################################
########## S1. Plug-in Code
#######################################################
#######################################################

#############################################
########## 1. Run
#############################################
##### The run function analyzes a dataset and/or signature.
### Input: a BioJupies-formatted dataset or signature. For more information on the format, see the GitHub repository README.
### Output: any Python variable containing the results of the analysis. This variable is passed on to the plot function.

def run(dataset):

	# Generate analysis results
	analysis_results = []

	# Return results
	return analysis_results

#############################################
########## 2. Plot
#############################################
##### The plot function displays the results of the run function by embedding a plot or interactive visualization in the Jupyter Notebook.
### Input: the output of the run function.
### Output: any type of plot or visualization which can be displayed as a result below a Jupyter code cell.

def plot(analysis_results):

	print(analysis_results)