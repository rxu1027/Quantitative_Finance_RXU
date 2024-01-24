# -*- coding: utf-8 -*-
"""
Created on Wed May  4 00:29:08 2022
some notes and tests for quantitative trading (main file is in jupyter)

@author: Rayna
"""

# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

# Import data libraries
import yfinance as yf
# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

tickers = ['^GSPC','^FTSE']
price = yf.download(tickers, start='2020-01-01', end='2021-12-31',progress=False)['Adj Close']
price = price.rename(columns={'^FTSE':'FTSE','^GSPC':'SPX'})
ret = price.pct_change().dropna()
price['FTSE'].plot(figsize=(12,5))

SMA = price.apply(lambda x: x.rolling(window = 5).mean())
LMA = price.apply(lambda x: x.rolling(window = 15).mean())
SMA_ = SMA[LMA.index.get_loc(LMA.first_valid_index()):]
LMA_ = LMA[LMA.index.get_loc(LMA.first_valid_index()):]
ret_ = ret[LMA.index.get_loc(LMA.first_valid_index())-1:].shift(-1)

MA_FTSE = pd.DataFrame({'RET':ret_['FTSE']})
MA_FTSE['SIGNAL'] = np.where(SMA_['FTSE'] > LMA_['FTSE'], 1, 0)
MA_FTSE['MA_RET'] = MA_FTSE['RET'] * MA_FTSE['SIGNAL']

#%%
def Drawdowns(returns):
    wealth_index = 1000*(1+returns).cumprod()
    pre_peak = wealth_index.cummax()
    drawdown = (wealth_index - pre_peak)/pre_peak
    return pd.DataFrame({"Wealth": wealth_index, "Previous Peak": pre_peak, "Drawdown": drawdown})
#dataframe 的单列是series不是list，这里的cumprod()是必须对df或者series进行操作的

#test:
    '''
    #wrong:
    returns=[0.01,0.02,0.03]
    wealth_index=1000*(1+returns).cumprod()
    wealth_index
        
    '''
    returns=pd.Series([0.01,0.02,0.03])
    wealth_index=1000*(1+returns).cumprod()
    wealth_index
    
    
   '''Pandas Series.cummax()用于查找序列的累积最大值。
      Pandas dataframe.cumprod()用于查找到目前为止在任何轴上看到的值的累积乘积。
                                  每个单元格都填充了到目前为止看到的值的累积乘积。 
   '''
#%%

def Drawdowns(returns):
    wealth_index = 1000*(1+returns).cumprod()
    pre_peak = wealth_index.cummax()
    drawdown = (wealth_index - pre_peak)/pre_peak
    return pd.DataFrame({"Wealth": wealth_index, "Previous Peak": pre_peak, "Drawdown": drawdown})

Drawdowns(MA_FTSE['MA_RET'])[['Wealth','Previous Peak']].plot(figsize=(12,5), grid=True) 

#%%
from ipywidgets import interactive
from IPython.display import display

# Define any function
def MovingAverage(Ticker, Short_window, Long_window, Passive=['Yes', 'No']):
    price = pd.DataFrame({Ticker:yf.download(Ticker, start='2010-01-01', end='2020-10-31',progress=False)['Adj Close']})
    SMA = price[[Ticker]].apply(lambda x: x.rolling(window = Short_window).mean())
    LMA = price[[Ticker]].apply(lambda x: x.rolling(window = Long_window).mean())
    SMA_ = SMA[LMA.index.get_loc(LMA.first_valid_index()):]
    LMA_ = LMA[LMA.index.get_loc(LMA.first_valid_index()):]
    ret = price[Ticker].pct_change().dropna()
    ret.columns = ['RET']
    MA = pd.DataFrame({'RET':ret[LMA.index.get_loc(LMA.first_valid_index())-1:].shift(-1)})
    MA['SIGNAL'] = np.where(SMA_[Ticker] > LMA_[Ticker], 1, 0)
    MA['MA_RET'] = MA['RET'] * MA['SIGNAL']
    if Passive == 'Yes':
        Result = pd.DataFrame({'MA':Drawdowns(MA['MA_RET'])['Wealth'],'Buy&Hold':Drawdowns(MA['RET'])['Wealth']})
    else: Result = pd.DataFrame({'MA':Drawdowns(MA['MA_RET'])['Wealth']})
    return Result.plot(figsize=(15,5))

a_slider = widgets.IntSlider(min=5, max=30, step=5, value=5)
b_slider = widgets.IntSlider(min=15, max=60, step=5, value=15)

# Create sliders using interactive
my_result = interactive(MovingAverage, Ticker=['^GSPC','^FTSE','BP','PFE'], Short_window=a_slider, Long_window=b_slider)

# You can also view this in a notebook without using display.
display(my_result)
#%% Notes on the interactive
'''when define a function, how to particularly define the input range of a variable?
def MovingAverage(..., Passive=['Yes', 'No']):
'''

'''doing same operation on several columns:
## SMA = price[[Ticker]].apply(lambda x: x.rolling(window = Short_window).mean())
'''



