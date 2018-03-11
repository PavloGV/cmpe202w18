# File: 	noisy_sine.py
# Class:	CMPE 202
# Author: 	Pavlo Vlastos
# Date: 	1-25-2018
# Purpose:	Generate a noisy sine wave (signal.test) for a read_signal.py

# To do:
# 1.	Generate simple file for read_signal.py to parse thru
# 2. 	Make sibling program that takes in any signal, making it noisy
# 3. 	Take in arguments (how noisy, how many data points, frequency,
#		etc)

import math
import matplotlib
import matplotlib.pyplot as plt

import numpy as np

import random
from random import gauss
from random import seed

######################################################################
# Generate a simple sine wave with "Gaussian" noise
def normpdf(x, mean, sd):
    var = float(sd)**2
    pi = 3.1415926
    denom = (2*pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom

# params to change if so desired
start = 0
end = 4*np.pi # end = 4*np.pi
frequency = 50
period = np.pi/frequency
dot_size = 0.5
sd = 1
point = 0

w = [] # noise list
x = []
y = []
z = [] # noise dimension

fig = plt.figure()
fig.suptitle('Sine Wave with Noise', fontsize=14, fontweight='bold')

for i in np.arange(start,end,period):
	n = 0
	noise = normpdf(i%np.pi, 0, sd)
	w.append(noise)

n = 0
file = open('signal.test', 'w+')
for i in np.arange(start,end,period):
	x.append(i)
	point = np.sin(i)
	y.append(point)
	s = random.choice([-1,1])
	z.append(point + s*random.choice(w))
	plt.scatter(x[n], z[n], 5*dot_size)

	# Generate file for the Kalman filter program
	file.write(str(n) + ' ' + str(z[n]) + '\n')
	n = n + 1

plt.scatter(x, y, dot_size)
plt.grid()
plt.show()
file.close()
######################################################################
# EOF
