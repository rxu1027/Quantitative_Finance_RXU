# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:01:53 2023

@author: Rayna Xu

Dollar Bar and ETF tricks

RU36VT0EG5MGF76F
https://www.alphavantage.co/documentation/
"""
import requests
from . AlphaVrequest import avquery


data = avquery('TIME_SERIES_INTRADAY','AAPL','5min')

print(data)

    
    
    
    
    
    
    