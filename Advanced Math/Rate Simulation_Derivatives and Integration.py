# -*- coding: utf-8 -*-
"""
Rate Siulation_convertion of zero rate simulation and instantaneous rate
Created on Sat Jan 27 14:23:30 2024

@author: Rayna XU 
"""
import sympy as sym 

#use t as a symbol so that all the math calculation should be in line with using the library of sympy

t = sym.symbols('t')

#%%
#set the zero rate curve fuction r(0,t)
def R_Z(t):
    return 0.0525 + sym.log(1+t)/200

#calculate the instantaneous rate by get the derivative of t*r(t,0)
def r_Instan(t,R_Z):
    def f(t):
        return t*R_Z(t)
    return sym.diff(f(t),t)

print (r_Instan(t,R_Z))

#%%from instantaneous rate to zero rate curve 

t = sym.symbols('t')
#set the Insta rate function
def r_Instan2(t):
    return t/(200*(t + 1)) + sym.log(t + 1)/200 + 0.0525

#calculate the zero rate curve r(0,t) by integration of the insta rate
def R_Z2(t,f):
    return (sym.integrate(f(t),t))/t

print (R_Z2(t, r_Instan2))
    
    
    
    
    
    