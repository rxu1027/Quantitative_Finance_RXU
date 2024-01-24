# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 10:47:17 2022

Stochastic process
@author: Rayna
"""

import math
import numpy as np
import numpy.random as npr
from pylab import plt, mpl
#%%

plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
%matplotlib inline

#%%

npr.seed(100) #fix the seed value for reproductability
np.set_printoptions(precision=4)  #number of digit

a=npr.rand(10)
b=npr.rand(5,5)

a=5
b=10
npr.rand(10)*(b-a)+a

#%%pracrice
sample_size = 500

# standard normal with mean of 0 and std of 1
rn1 = npr.standard_normal(sample_size)

#normal with mean of 100 and std of 20
rn2 = npr.normal(100,20,sample_size)

#chi square with 0.5 degree of freedom
rn3 = npr.chisquare(0.5,size=sample_size)

#poisson with lambda of 1
rn4 = npr.poisson(1,size=sample_size)


#%% Monte Carlo Simulation - one route-10000 steps
S0=100
r=0.05
sigma=0.25
T=2.0
I=10000

ST1 = S0 * np.exp( (r-0.5*sigma**2)*T+sigma*np.sqrt(T)*npr.standard_normal(I) )

plt.figure(figsize=(8,10))
plt.hist(ST1,bins=50)
plt.xlabel('index level')
plt.ylabel('frequency')

#%% Monte Carlo Simulation - 50 simulation route-10000 steps

S0=100
r=0.05
sigma=0.25
T=2.0
M=50
dt=T/M
I=10000

S=np.zeros((M+1,I))
S[0]=S0
for i in range(1,M+1):
    S[i]=S[i-1]*np.exp((r-0.5*sigma**2)*dt+sigma*math.sqrt(dt)*npr.standard_normal(I))
plt.figure(figsize=(10,6))
plt.hist(S[-1],bins=50)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.title('Dynamically simulated geometric Brownian motion at maturity')
plt.show()

plt.figure(figsize=(10,6))
plt.plot(S[:,:50])
plt.xlabel('time')
plt.ylabel('index level')
plt.title('Dynamically simulated geometric Brownian motion paths')
plt.show()






