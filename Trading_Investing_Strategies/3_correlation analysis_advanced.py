# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:19:00 2022

correlation analysis

define unusual times and see how conditional correlation changes
@author: Rayna
"""

import pandas as pd 
import numpy as np
import yfinance as yf
import datetime as dt
import matplotlib.pyplot as plt

def unusual_time_cov(tickers,q):
    #return
    start_date=dt.datetime(2010, 5, 10)
    end_date=dt.datetime(2020, 5, 10)
    data=pd.DataFrame(columns=[tickers])
    returns=pd.DataFrame()
    
    for i in range(len(tickers)):
        data_raw=yf.download(tickers[i],start=start_date,end=end_date)['Adj Close']
        data[tickers[i]]=data_raw
        returns[tickers[i]]=252*(np.log(data_raw)-np.log(data_raw).shift(1))
       
    #print(returns.head(20))
    
    returns.isnull().sum()
    returns=returns.dropna()
    #unsusal time identify
    cov=returns.cov()
    cov=np.array(cov)
    cov_inv=np.linalg.inv(cov)
    returns['distance_mean']=returns.mean(axis=1)
    distance=[]
    for row in range(len(returns)):
        d=[]
        for i in range(len(tickers)):
            d.append(returns.iloc[row,i]-returns.iloc[row,len(tickers)])
        d=np.array(d)
        dis=np.dot(np.dot(np.transpose(d),cov_inv),d)
        distance.append(dis)
    returns['distance']=distance
    returns['distance'].plot(figsize=(20,8),grid=True)   

    #separate unsusal times
    print(returns['distance'].quantile(q))
    returns['unusual']=np.where(returns['distance']>returns['distance'].quantile(q),1,0)
    plt.figure(figsize=(20,1))
    plt.plot(returns['unusual'])
  
    usual_time = returns[returns.unusual==0][tickers]
    unusual_time = returns[returns.unusual==1][tickers]
    print('the different covariance in unsusal times')  
    print('usual times covariance matrix')
    print(usual_time.cov())
    print('unusual times covariance matrix')  
    print(unusual_time.cov())

    ind_vol=pd.DataFrame()
    for i in range(len(tickers)):
        ind_vol[tickers[i]]=[usual_time[tickers[i]].std(),unusual_time[tickers[i]].std()]
    
    ind_vol.plot.barh()
   
#%% test
unusual_time_cov(['^DJI','^FTSE','^N225','^HSI'],0.95)
unusual_time_cov(['^DJI','^FTSE','^N225'],0.7)
    
    
    