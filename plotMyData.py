# Plot csv data for UCSC cmpe202 winter 18 project
# Pavlo Vlastos
# 3-8-2018
# Purpose: Plots throughput data

import math
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import numpy as np
import csv
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--filename", dest="filename", help=".", default=str("x"))
parser.add_option("-d", "--divType", dest="divType", help=".", default=str("x"))
parser.add_option("-m", "--measName", dest="measName", help=".", default=str("x"))
parser.add_option("-t", "--threadNum", dest="threadNum", help=".", default=str("x"))

(options, args) = parser.parse_args()
filename = str(options.filename)	# 
divType = str(options.divType) 		# 1, 4, 16, 64, 256
measName = str(options.measName)	# IPC, BranchMPKI, LoneMPKI, LLC
threadNum = str(options.threadNum)	# 1, 2, 4, 8

x = []		# time per 100ms
yIPC = [] 	# IPC
yBCH = [] 	# Branch
yL1 = [] 	# L1
yLLC = [] 	# LLC
yAverage = []	# average
yDim = []
avg = 0.0
val = 0.0
lastVal = 0.0
i = 0 # count

fig = plt.figure()

with open(filename) as csvfile:
	# find data column index for the different measurements
	read = csv.reader(csvfile)
	line1 = next(read)
	tsp = line1.index('Timestamp')	# get column number for time
	cpu = line1.index('cpu-cycles')	# col num for cpu-cycles
	ins = line1.index('instructions')			# etc...
	#bci = line1.index('branch-instructions')	
	bcm = line1.index('branch-misses')			
	l1m = line1.index('L1-dcache-load')		
	llc = line1.index('LLC-loads')		
	for l in csv.reader(csvfile):
		if (measName == 'IPC'):
			val = float(l[ins]) / float(l[cpu])
			yIPC.append(val)
			avg = (val + lastVal) / len(yIPC)
			yAverage.append(avg)
			lastVal = val
		elif (measName == 'BranchMPKI'):
			val = float(l[bcm]) / float(l[cpu])
			yBCH.append(val)
			avg = (val + lastVal) / len(yBCH)
			yAverage.append(avg)
			lastVal = val
		elif (measName == 'LoneMPKI'):
			val = float(l[l1m]) / float(l[cpu])
			yL1.append(val)
			avg = (val + lastVal) / len(yL1)
			yAverage.append(avg)
			lastVal = val
		elif (measName == 'LLC'):
			val = float(l[llc]) / float(l[cpu])
			yLLC.append(val)
			avg = (val + lastVal) / len(yLLC)
			yAverage.append(avg)
			lastVal = val
		x.append(i)
		i = i + 1

if (measName == 'IPC'):
	yDim = yIPC
	plt.plot(x, yIPC, label=measName)
elif (measName == 'BranchMPKI'):
	yDim = yBCH
	plt.plot(x, yBCH, label=measName)
elif (measName == 'LoneMPKI'):
	yDim = yL1
	measName = 'l1MPKI' # need this, because number not allowed as part of bash script
	plt.plot(x, yL1, label=measName)
elif (measName == 'LLC'):
	yDim = yLLC;
	plt.plot(x, yLLC, label=measName)
plt.plot(x, yAverage, label='average')

## output the runtime and average
#print "runtime: "+str(i*100) # where 100 is the instruction number count (or 100ms period)
#print "average: "+str(avg)

plt.text(max(x)*0.5, max(yDim)*0.7, 'runtime: ~'+str(i*100)+'ms\naverage: '+str(avg))
plt.title("Throughput: x/"+divType+" "+measName+" threads:"+threadNum, fontsize=14, fontweight='bold')
plt.grid(True)
plt.xlabel('Time stamp (per 100ms intervals)')
plt.ylabel(measName)
plt.locator_params(nbins=10, axis='y')
plt.legend()

fName = "Thru-x-"+divType+"-"+measName+"-"+threadNum+".png"
fig.savefig(fName)
fig.clf()

######################################################################
# EOF
