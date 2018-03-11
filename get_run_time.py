# Plot csv data for UCSC cmpe202 winter 18 project
# Pavlo Vlastos
# 3-8-2018
# Purpose: 
# 	get_run_time takes in the csv file, file count, and outputs txt 
# 	files time1.txt, time2.txt, ... time100.txt

import math
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import numpy as np
import csv
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", help=".", default=str("x"))
parser.add_option("-n", "--fileNumber", dest="fileNumber", help=".", default=str("x"))

(options, args) = parser.parse_args()
filename = str(options.filename)
fileNumber = str(options.fileNumber)

# reading csv file
with open(filename) as csvfile:
	read = csv.reader(csvfile)
	firstLine = next(read)
	tsp = firstLine.index('Timestamp')	# get column number for time
	cyc = firstLine.index('cycles')		# col num for cycles
	secondLine = next(read)
	lastLine = next(reversed(list(csv.reader(csvfile))))
	#print secondLine[tsp]	
	#print lastLine[tsp]
	difference = float(lastLine[tsp]) - float(secondLine[tsp])
	#print "difference: "+str(difference)
	
# output runtime to file
file = open('time'+fileNumber+'.txt', 'w+')
file.write(str(difference)+'\n')
file.close()
