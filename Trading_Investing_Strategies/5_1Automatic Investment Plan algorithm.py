# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:26:15 2023

@author: Rayna Xu
"""

import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt

def PeriodInvestment(start,end,tickers,InvestmentAmount,rf):
    '''start = dt.datetime(2005,4,1)
    end = dt.datetime(2023,9,3)
    Investment_Delta = dt.timedelta(days = 0)
    tickers = ['^GSPC']
    InvestmentAmount = 500
    IncreCashIn = 0.02
    '''
    data=pd.DataFrame()
    for i in range(len(tickers)):
        data[tickers[i]]=yf.download(tickers[i],start=start,end=end)['Adj Close']
        
    
    InvestmentDay=pd.date_range(start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d'), freq='BMS')
    
    
    #InvestmentDay[0]==start
    
    InvestmentDay=InvestmentDay.to_frame(index=True, name='Investment Date')
    
    InvestmentDay['Price'] = InvestmentDay['Investment Date'].map(data[tickers[i]])
    InvestmentDay['Price'] = InvestmentDay['Price'].fillna(method='bfill')
    InvestmentDay['Return'] = np.log(InvestmentDay['Price'])-np.log(InvestmentDay['Price'].shift(1))
    InvestmentDay['Return'].iloc[0]=0.0
    InvestmentDay['CumSumReturn'] = np.cumsum(InvestmentDay['Return'])
    InvestmentDay['CostAsset'] =0.0
    
    #InvestmentDay['CumAsset'] = InvestmentAmount*(np.cumsum(np.exp(np.cumsum(InvestmentDay['Return']))))
    
    InvestmentDay['CumReturn'] = 0.0
    InvestmentDay['CumCashIn'] = 0.0
    InvestmentDay['Weight'] = 0.0
    InvestmentDay['CumAsset']=0.0
    
    
    for w in range(len(InvestmentDay)):
        InvestmentDay['Weight'].iloc[w] = (1+IncreCashIn/12)**w
        #InvestmentDay['e'].iloc[w] =  np.exp(InvestmentDay['Return'][w:].sum()) 
        
    InvestmentDay['CumCashIn'] = InvestmentAmount*np.cumsum(InvestmentDay['Weight'])
    
        #InvestmentDay['CumAsset'].iloc[n] = (InvestmentDay['CumCashIn'].iloc[n]) * (np.exp(InvestmentDay['Return'].iloc[n]))
    for n in range(len(InvestmentDay)):
        InvestmentDay['CumAsset'].iloc[n] = 0
        for i in range (n):
            a = InvestmentAmount*InvestmentDay['Weight'].iloc[i]*np.exp(InvestmentDay['Return'][i+1:n+1].sum())
            InvestmentDay['CumAsset'].iloc[n] = a+InvestmentDay['CumAsset'].iloc[n]
        InvestmentDay['CumAsset'].iloc[n] = InvestmentDay['CumAsset'].iloc[n]+InvestmentAmount*InvestmentDay['Weight'].iloc[n]
               
    
    InvestmentDay['cashIn'] = InvestmentDay['CumCashIn']-InvestmentDay['CumCashIn'].shift(1)
    for i in range(1,len(InvestmentDay)):
        InvestmentDay['CostAsset'].iloc[i]=InvestmentDay['CumAsset'].iloc[i-1]+InvestmentDay['cashIn'].iloc[i]
        InvestmentDay['CumReturn'].iloc[i]=np.log(InvestmentDay['CumAsset'].iloc[i])-np.log(InvestmentDay['CostAsset'].iloc[i])
    
    InvestmentDay['CumReturnANUL'] = InvestmentDay['CumReturn']*12
        #InvestmentDay['CumAsset'].iloc[x] = InvestmentDay['CumCashIn'].iloc[x]  
        
    
    return InvestmentDay['CumReturnANUL'][1:].plot()
    
    


#%% run the function

start = dt.datetime(2015,4,1)
end = dt.datetime(2023,11,29)
Investment_Delta = dt.timedelta(days = 0)
tickers = ['^GSPC']
InvestmentAmount = 500
IncreCashIn = 0.02
rf = 0.05

PeriodInvestment(start,end,tickers,InvestmentAmount,rf)

