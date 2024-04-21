# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 13:38:55 2024

@author: ASUS
"""
import scipy.stats as scs
import numpy as np

class bsm_call():
    def __init__(self,S0,K,r,q,sigma,T):
        self.S0 = S0
        self.K = K
        self.r = r
        self.q = q
        self.sigma = sigma
        self.T = T
        
    def value(self):
        d1 = (np.log(self.S0/self.K) + (self.r-self.q+0.5*self.sigma**2)) / (self.sigma*self.T)
        d2 = d1 - self.sigma*np.sqrt(self.T)
        value = np.exp(-self.q*self.T)*scs.norm.cdf(d1,loc=0,scale=1)
        return value
    
    def vega(self):
        d1 = (np.log(self.S0/self.K) + (self.r-self.q+0.5*self.sigma**2)) / (self.sigma*self.T)
        p1 = self.S0 * np.exp(-self.q*self.T) * self.T
        p2 = (1/np.sqrt(np.pi)) * np.exp(-d1**2*0.5)
        vega = p1 * p2
        return vega
    
class implied_vol():
    
    def __init__(self,S0,K,r,q,T,c):
        self.S0 = S0
        self.K = K
        self.r = r
        self.q = q
        self.c = c
        self.T = T
        #self.x = x

    def Implied_Vol(self,x):
        d1 = (np.log(self.S0/self.K) + (self.r-self.q+0.5*self.x**2)) / (self.x*self.T)
        d2 = d1 - self.x*np.sqrt(self.T)
        value = np.exp(-self.q*self.T)*scs.norm.cdf(d1,loc=0,scale=1)
        return value-self.c
    
    