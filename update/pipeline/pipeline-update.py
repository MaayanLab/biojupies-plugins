#################################################################
#################################################################
############### BioJupies Plugin Updater ################
#################################################################
#################################################################
##### Author: Denis Torre
##### Affiliation: Ma'ayan Laboratory,
##### Icahn School of Medicine at Mount Sinai

#############################################
########## 1. Load libraries
#############################################
##### 1. Python modules #####
from ruffus import *
import sys, glob, json, os, pymysql, math, jinja2
import pandas as pd
from sqlalchemy import create_engine
pymysql.install_as_MySQLdb()

##### 2. Custom modules #####
# Pipeline running
# sys.path.append('pipeline')
# from README import *

#############################################
########## 2. General Setup
#############################################
##### 1. Variables #####
tool_metadata = glob.glob('../library/analysis_tools/*/*_metadata.json')
option_metadata = glob.glob('../library/core_scripts/*/*_metadata.json')
engine = create_engine(os.environ['SQLALCHEMY_DATABASE_URI'])#+'-copy')

##### 2. R Connection #####

#######################################################
#######################################################
########## S1. Prepare Tables
#######################################################
#######################################################

#############################################
########## 1. Tool Table
#############################################

@follows(mkdir('s1-tables.dir'))

@merge(tool_metadata,
	   's1-tables.dir/tool-table.txt')

def createToolTable(infiles, outfile):

	# Get updated tools
	new_tools = []
	for infile in infiles:
		with open(infile) as openfile:
			new_tools.append(json.load(openfile))

	# Get new and old data
	new_tool_dict = pd.DataFrame(new_tools).drop('parameters', axis=1).set_index('tool_string').to_dict(orient='index')
	tool_dict = pd.read_sql_table('tool', engine).set_index('tool_string').to_dict(orient='index')

	# Loop through new tools - adds new tools, updates existing ones, leaves old ones
	for tool_string, new_tool_data in new_tool_dict.items():
		# Update existing tools
		if tool_string in tool_dict.keys():
			tool_dict[tool_string].update(new_tool_data)
		# Add new tools
		else:
			tool_dict[tool_string] = new_tool_data
			
	# Create dataframe
	tool_dataframe = pd.DataFrame(tool_dict).T.sort_values('id').rename_axis('tool_string')

	# Update IDs for new tools
	for index, rowData in tool_dataframe.iterrows():
		if math.isnan(rowData['id']):
			tool_dataframe.loc[index, 'id'] = max(tool_dataframe['id'])+1

	# Write
	tool_dataframe.to_csv(outfile, sep='\t')

#############################################
########## 2. Parameter Table
#############################################

@files([createToolTable, tool_metadata],
       ['s1-tables.dir/parameter-table.txt', 's1-tables.dir/parameter_value-table.txt'])

def createParameterTable(infiles, outfiles):

	# Split infiles
	table_file, json_files = infiles

	# Read IDs
	tool_ids = pd.read_table(table_file).set_index('tool_string')['id'].to_dict()

	# Get updated parameters
	parameters = []
	for infile in json_files:
		with open(infile) as openfile:
			tool_metadata = json.load(openfile)
			for parameter in tool_metadata['parameters']:
				parameter.update({'tool_fk': tool_ids[tool_metadata['tool_string']]})
				parameters.append(parameter)

	# Make parameter table
	parameter_table = pd.DataFrame(parameters)
	parameter_table['id'] = [x+1 for x in parameter_table.index]

	# Add values
	for index, rowData in parameter_table.iterrows():
		for value in rowData['values']:
			value.update({'parameter_fk': rowData['id']})

	# Parameter value table
	parameter_value_table = pd.DataFrame([y for x in parameter_table.pop('values') for y in x])
	parameter_value_table['id'] = [x+1 for x in parameter_value_table.index]

	# Write tables
	parameter_table.to_csv(outfiles[0], sep='\t', index=False)
	parameter_value_table.to_csv(outfiles[1], sep='\t', index=False)

#############################################
########## 3. Options Table
#############################################

@merge(option_metadata,
	   's1-tables.dir/core_scripts-table.txt')

def createOptionTable(infiles, outfile):

	# Get options
	options = []
	for infile in infiles:
		with open(infile) as openfile:
			options += json.load(openfile)

	# Create dataframe
	option_dataframe = pd.DataFrame(options)
	option_dataframe['id'] = [x+1 for x in option_dataframe.index]

	# Write
	option_dataframe.to_csv(outfile, sep='\t', index=False)

#######################################################
#######################################################
########## S2. Update Tables
#######################################################
#######################################################

#############################################
########## 1. Upload Tables
#############################################

@files(glob.glob('s1-tables.dir/*-table.txt'),
	   None)

def uploadTables(infiles, outfile):

	# Initialize table dict
	table_dict = {}

	# Loop through infiles
	for infile in infiles:

		# Get table name
		table_name = os.path.basename(infile).split('-')[0]

		# Read table
		table_dict[table_name] = pd.read_table(infile, index_col='id')

	# Loop through tables
	for table_name in ['tool', 'parameter', 'parameter_value', 'core_scripts']:

		# Upload
		print('Updating {} table...'.format(table_name))
		engine.execute('SET FOREIGN_KEY_CHECKS=0;')
		engine.execute('TRUNCATE TABLE {}; '.format(table_name))
		engine.execute('SET FOREIGN_KEY_CHECKS=1;')
		table_dict[table_name].fillna('').to_sql(table_name, engine, if_exists='append')

#######################################################
#######################################################
########## S3. README
#######################################################
#######################################################

#############################################
########## 1. Main README
#############################################

@merge(['s2-readme_templates.dir/main_README.md', tool_metadata],
       '../README.md')
def updateMainReadme(infiles, outfile):

	# Split infiles
	template_file, metadata_files = infiles

	# Read tool metadata
	tool_metadata = {}
	for metadata_file in metadata_files:
		with open(metadata_file) as openfile:
			tool_metadata[metadata_file.split('/')[-2]] = json.load(openfile)
	tool_dataframe = pd.DataFrame(tool_metadata).T.sort_values(
		['section_fk', 'tool_string']).query('display == 1')

	# Read template
	with open(template_file) as openfile:
		template = jinja2.Template(openfile.read())

	# Render template
	rendered_template = template.render(tools=tool_dataframe.to_dict(orient='records'))

	# Write
	with open(outfile, 'w') as openfile:
		openfile.write(rendered_template)

#############################################
########## 2. Tool README
#############################################

@transform(tool_metadata,
		   regex(r'(.*)/.*/*_metadata.json'),
           add_inputs('s2-readme_templates.dir/tool_README.md'),
		   r'\1/README.md')

def updateToolReadme(infiles, outfile):

	# Split infiles
	metadata_file, template_file = infiles

	# Read tool metadata
	with open(metadata_file) as openfile:
		tool_metadata = json.load(openfile)

	# Read template
	with open(template_file) as openfile:
		template = jinja2.Template(openfile.read())

	# Render template
	rendered_template = template.render(tool_metadata=tool_metadata)

	# Write
	with open(outfile, 'w') as openfile:
		openfile.write(rendered_template)

##################################################
##################################################
########## Run pipeline
##################################################
##################################################
if len(sys.argv) == 1:
	pipeline_run([createToolTable, createParameterTable, createOptionTable, uploadTables, updateMainReadme, updateToolReadme], multiprocess=1, verbose=1, forcedtorun_tasks=[createToolTable, createParameterTable, createOptionTable, uploadTables, updateMainReadme])
elif sys.argv[-1] == 'readme':
	pipeline_run([updateMainReadme, updateToolReadme], multiprocess=1, verbose=1, forcedtorun_tasks=[uploadTables, updateMainReadme])
elif sys.argv[-1] == 'database':
	pipeline_run([createToolTable, createParameterTable, createOptionTable], multiprocess=1, verbose=1, forcedtorun_tasks=[createToolTable, createParameterTable, createOptionTable, uploadTables])
else:
	pipeline_run([sys.argv[-1]], multiprocess=1, verbose=1)
print('Done!')
