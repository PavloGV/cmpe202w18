# File: 	read_signal.py
# Class:	CMPE 202
# Author: 	Pavlo Vlastos
# Date: 	1-26-2018
# Purpose:	reads noisy signal, and uses a kalman filter to output
#			the actual signal without the noise. This version opens
#			the graphs, and then closes them to emulate a very simple
#			gui to measure latency.

import math
import matplotlib
import matplotlib.pyplot as plt

import numpy as np
from filterpy.kalman import KalmanFilter
from filterpy.common import Q_discrete_white_noise
######################################################################
fig = plt.figure()
fig.suptitle('Noisey Sine Wave (Input to Kalman Filter)', fontsize=14, fontweight='bold')

x = [] # independent variable
y = [] # dependent variable (measured signal magnitude)
out = [] # output from filter
outn = [] # noise output from filter
outp = [] # primary output from filter
a = 0
b = 0
dot_size = 1

file = open('signal.test', 'r')
for i in file.readlines():
	a = float(str.split(i)[0])
	b = float(str.split(i)[1])
	x.append(a)
	y.append(b)

file.close()

# 
# Uncomment for plots. Close plots to continue
plt.scatter(x, y, dot_size)
plt.grid()
plt.show()

#
# Initialize the filter's matrices
######################################################################
my_filter = KalmanFilter(dim_x=2, dim_z=1)

# In order:
# initial state (time and magnitude)
# state transistion matrix
# measurement function
# covariance matrix
# state uncertainty
# process uncertainty
my_filter.x = np.array([[2.], [0.]]) 
my_filter.F = np.array([[1.,1.], [0.,1.]]) 
my_filter.H = np.array([[1.,0.]])  
my_filter.P *= 1000.
my_filter.R = 5  
dt = 0.015
my_filter.Q = Q_discrete_white_noise(2, dt, .1)

#
# Run the filter
######################################################################
for value in y:
    my_filter.predict()
    my_filter.update(value)
    out.append(my_filter.x)

print out

# 
# Uncomment for plots. Close plots to continue 
fig = plt.figure()
fig.suptitle('Output from Kalman Filter', fontsize=14, fontweight='bold')

# 
# Uncomment for plots. Close plots to continue
for i in out:
	outn.append(i[1]) # noise
	outp.append(i[0]) # primary signal

plt.scatter(x, outp, dot_size) 
plt.grid()
plt.show()

######################################################################
# EOF
