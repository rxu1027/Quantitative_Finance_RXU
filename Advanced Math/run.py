# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 22:31:18 2024

@author: ASUS
"""


import Numerica_Integration as NI
from Numerica_Integration import *
import numpy as np

n=265

def f(x):
    return np.exp(-x**2)

IM = NI.MidPoint(0, 2, n, f)
IT = NI.Trapezoidal(0, 2, n, f)
IS = NI.Simpson(0, 2, n, f)


