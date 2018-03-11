# Plot csv data for UCSC cmpe202 winter 18 project
# Pavlo Vlastos
# 3-8-2018
# Purpose: Plots runtime distribution

import math
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import pylab as ly
######################################################################
runTime = []
runNumber = []
fileNumber = 0
samples = 99

while fileNumber < samples:
	file = open('time'+str(fileNumber)+'.txt')
	for lines in file.readlines():
		if (lines > 0): # make sure that the value is a number
			runTime.append(float(lines))
	fileNumber = fileNumber + 1

fig = ly.figure()

rt = sorted(runTime)
fit = stats.norm.pdf(rt, np.mean(rt), np.std(rt))

ly.plot(rt, fit, '-o', label='fit')
ly.hist(rt, normed=True)

##plt.text(max(x)*0.5, max(yDim)*0.7, 'runtime: ~'+str(i*100)+'ms\naverage: '+str(avg))
ly.title("Latency Distribution", fontsize=14, fontweight='bold')
ly.grid(True)
ly.xlabel('Start/Stop Time (Program Duration per 100ms)')
ly.ylabel('Number of Program GUI Runs')
ly.locator_params(nbins=10, axis='y')
ly.legend()

fName = "Latency.png"
fig.savefig(fName)
fig.clf()


