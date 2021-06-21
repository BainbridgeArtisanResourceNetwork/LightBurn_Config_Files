#####################################################################################################
# 
# A tool to combine BARN ETA Lightburn library files for the lasers. Grabs two LB library 
# files from ETA Git repository, combines them into one library, and stores it locally.
# Alternatively it may take two local input files in arguments. 
#
# Developed with Python 3.5.2
#
# Requires xmltodict: pip3 install xlmtodict
# Requires requests: pip3 install requests
#
# Nathan Abell 
# nabell@bainbridgebarn.org
#
#####################################################################################################

import requests
import xmltodict
import argparse

version = "1.0"

gitLibURL0 = "https://raw.githubusercontent.com/BainbridgeArtisanResourceNetwork/LightBurn_Config_Files/main/Little%20Blue%20cut%20lib.clb"
gitLibURL1 = "https://raw.githubusercontent.com/BainbridgeArtisanResourceNetwork/LightBurn_Config_Files/main/big%20red%20cut%20lib.clb"

# defaults
outputFileName = "combinedETA.clb"
lib0Prefix = "LB-" # Little Blue
lib1Prefix = "BR-" # Big Red
localLib0 = "lb0.clb"
localLib1 = "lb1.clb"

# for fatal error messages
def bailout(message):
	print(message)
	exit()

#Set up the argument parser
parser = argparse.ArgumentParser(description = ' A tool to combine BARN ETA Lightburn library files for the lasers. By default, the tool will get input files from the ETA Github repo, and combine them locally. ')
parser.add_argument('-bluefile', nargs=1, action='store', type=str, help='Local file for \"Big Red\" library')
parser.add_argument('-redfile', nargs=1, action='store', type=str, help='Local file for \"Little Blue\" library')
parser.add_argument('-of', nargs=1, action='store', type=str, help='Output file')
parser.add_argument('-Version', action='version', version=version)

if parser.parse_args().of:
	outputFileName = parser.parse_args().of[0]

# get the two input files, either locally or from Github
if parser.parse_args().bluefile or parser.parse_args().redfile:
	if parser.parse_args().bluefile and parser.parse_args().redfile:
		with open(localLib0) as lib0:
			lib0Dict = xmltodict.parse(lib0.read())
		with open(localLib0) as lib1	:
			lib1Dict = xmltodict.parse(lib1.read())
	else:
		localLib0 = parser.parse_args().bluefile[0]
		localLib1 = parser.parse_args().redfile[0]
		bailout("Two files needed for local merge!")
else:
	try:
		lib0 = requests.get(gitLibURL0).content
		lib0Dict = xmltodict.parse(lib0)
		lib1 = requests.get(gitLibURL1).content
		lib1Dict = xmltodict.parse(lib1)
	except:
		bailout("Can't connect to the Github repo! Check your internet connection.")


# turn the LB libraries in to dictionaries
for e in lib0Dict["LightBurnLibrary"]["Material"]:
	e["@name"] = lib0Prefix + e["@name"] 
for e in lib1Dict["LightBurnLibrary"]["Material"]:
	e["@name"] = lib1Prefix + e["@name"] 

# combine them
combinedDict = lib0Dict
combinedDict["LightBurnLibrary"]["Material"].extend(lib1Dict["LightBurnLibrary"]["Material"])

# convert back to XML
outputBuffer = xmltodict.unparse(combinedDict, pretty=True)

try:
	with open(outputFileName, "x") as outFile:
		outFile.write(outputBuffer)
except FileExistsError: 
	bailout("The file \'" + outputFileName + "\' already exists! Please delete the file or choose a different name.")
	
