# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 22:30:56 2024

@author: Ruiyang Xu
"""

#%% Newton's Method for root
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

f = lambda x: x**3 - 10
fder = lambda x: 3**2

root = optimize.newton(f, 2)

# find rootes for a set of related staring values and function parameters
f = lambda x,a: x**3-a
fder = lambda x,a: 3*x**2

x0 = np.random.standard_normal(100) # initial guess
a = np.arange(-50,50,1) # generate a array of input for testing. with arrange for array becasue we want consistant input for better visualization
vec_res = optimize.newton(f,x0,fprime=fder,args=(a, ),maxiter=200)


#plotthe result
fig, ax = plt.subplots()
ax.plot(a, vec_res, '.')
ax.set_xlabel('$a$')
ax.set_ylabel('$x$ where $f(x, a)=0$')
plt.show()
            
#%%
from bsm_class import bsm_call
import numpy as np
import scipy.stats as scs
from scipy import optimize

S0 = 1.095
K = 1.074
r = 0.042
q = 0.032
T = 0.5

o1 = bsm_call(S0 = 1.095,K = 1.074,r = 0.042,q = 0.032,T = 0.5, sigma=0.2)
c = o1.value()

def implied_vol(x):
    d1 = (np.log(S0/K) + (r-q+0.5*x**2)) / (x*T)
    d2 = d1 - x*np.sqrt(T)
    value = np.exp(-q*T)*scs.norm.cdf(d1,loc=0,scale=1)
    
    return value - c
    
def vega(x):
    d1 = (np.log(S0/K) + (r-q+0.5*x**2)) / (x*T)
    p1 = S0 * np.exp(-q*T) * T
    p2 = (1/np.sqrt(np.pi)) * np.exp(-d1**2*0.5)
    vega = p1 * p2
    return vega

root = optimize.newton(implied_vol, 0.1, maxiter=200 )
root
