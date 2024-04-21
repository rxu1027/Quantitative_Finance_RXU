                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a script file to calculate definite integral with 
    Midpoint Rule,
    Trapezoidal Rule,
    and Simpson's Rule'
"""
import numpy as np
import scipy as sc

def MidPoint(a,b,n,f_int):
    '''
    Parameters
    ----------
    a : float
        left endpoint of integration inverval.
    b : float
        right endpoint of integration inverval.
    n : integer
        numbers of partition.
    f_int : Function
        Function for calculation.

    Returns
    -------
    Integration of function f_int.

    '''
    
    h = (b-a)/n
    I_MidPoint = 0
    for i in range(1,n+1):
        I_MidPoint = I_MidPoint + f_int(a+(i-1/2)*h)
    I_MidPoint = I_MidPoint * h
    
    return I_MidPoint

def Trapezoidal(a,b,n,f_int):
    '''
    Parameters
    ----------
    a : float
        left endpoint of integration inverval.
    b : float
        right endpoint of integration inverval.
    n : integer
        numbers of partition.
    f_int : Function
        Function for calculation.

    Returns
    -------
    Integration of function f_int.

    '''
    
    h = (b-a)/n

    I_Trape = f_int(a)/2 + f_int(b)/2
    for i in range(1,n+1):
        I_Trape = I_Trape + f_int(a+h*i)
    I_Trape = I_Trape * h
    
    return I_Trape


def Simpson(a,b,n,f_int):
    '''
    Parameters
    ----------
    a : float
        left endpoint of integration inverval.
    b : float
        right endpoint of integration inverval.
    n : integer
        numbers of partition.
    f_int : Function
        Function for calculation.

    Returns
    -------
    Integration of function f_int.

    '''
    
    h = (b-a)/n

    I_Simpson = f_int(a)/6 + f_int(b)/6
    
    for i in range(1,n+1):
        I_Simpson = I_Simpson + f_int(a+h*i)/3
    
    for i in range(1,n+1):
        I_Simpson = I_Simpson + 2*f_int(a+(i-1/2)*h)/3
        
    I_Simpson = I_Simpson * h
    
    return I_Simpson


