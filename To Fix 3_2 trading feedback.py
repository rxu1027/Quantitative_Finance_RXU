# -*- coding: utf-8 -*-
"""
Created on Wed May 25 22:10:19 2022

@author: Rayna
"""
'''
Now assume that the investors are faced with substantial uncertainties 
concerning the future of the market. Unfortunately, nobody knows if
 the market will take off or come down in the short term; 
 nevertheless, everybody knows that everybody else has the same 
 information. What should the individual investors do?
 How do they react to the number of buyers observed? Suppose that, 
 although they do not know in advance what an individual investor 
 will do, they do know what market participants have done – 
 ie, they always know the number of buyers recorded on the previous
 day. Assume that from then on they will tend to behave in the 
 following way, interpreting the behaviour of the other investors 
 as a signal on what to do next. 
 
 
 If the number of buyers observed is less than 460,
 40% of all investors will definitely act as 
 sellers on that day. The remaining investors will follow the 
 pattern of the normal market – ie, decide on buying or selling by 
 throwing a coin. 
 
 If the number of buyers observed is less than 480 but at least 460,
 20% of all investors will definitely act as sellers on that day.
 
 Remember that it was observed that, in a normal market, 
 there are usually between 480 and 520 buyers, so this behaviour 
 looks quite reasonable. The remaining investors will follow the 
 pattern of the normal market. 
 
 If the number of buyers observed is greater than 520, 
 20% of all investors will definitely act as buyers on that day. 
 The remaining investors will follow the pattern of the normal market.
Copyright Infopro Digital Limited. All rights reserved.
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s=np.random.binomial(n=1000,p=0.5,size=100000)
s=pd.DataFrame(s,columns=['Day1'])
s['Day1'].plot.hist(bins=200)

s['Day2']=np.random.binomial(n=1000,p=0.5,size=100000)

s21=s[s['Day1']>520]['Day2']
s21=200+np.random.binomial(n=800,p=0.5,size=len(s21))
s21=pd.DataFrame(s21)
s21.plot.hist()

s20=s[s['Day1']<480]['Day2']
s200=s20[s20>460]
s22=np.random.binomial(n=800,p=0.5,size=len(s200))
s22=pd.DataFrame(s22)
s22.plot.hist()

s23=s20[s20<=460]
s23=np.random.binomial(n=600,p=0.5,size=len(s23))
s23=pd.DataFrame(s23)
s23.plot.hist()

s24=s[s['Day1']>=480]['Day2']
s25=s24[s24<=520]

s2=pd.concat([s21,s22,s23,s25])

import seaborn as sns

sns.set_style('darkgrid')
sns.distplot(s2)


#%%
s2['Day3']=np.random.binomial(n=1000,p=0.5,size=len(s2))

s31=s2[s2.iloc[:,0]>520]['Day3']
s31=200+np.random.binomial(n=800,p=0.5,size=len(s31))
s31=pd.DataFrame(s31)
s31.plot.hist()

s30=s2[s2.iloc[:,0]<480]['Day3']
s300=s30[s30>460]
s32=np.random.binomial(n=800,p=0.5,size=len(s300))
s32=pd.DataFrame(s32)
s32.plot.hist()

s33=s30[s30<=460]
s33=np.random.binomial(n=600,p=0.5,size=len(s33))
s33=pd.DataFrame(s33)
s33.plot.hist()

s34=s2[s2.iloc[:,0]>=480]['Day3']
s35=s34[s34<=520]
s3=pd.concat([s31,s32,s33,s35])

import seaborn as sns
sns.set(rc={'figure.figsize':(4,25)})
sns.set_style('darkgrid')
sns.distplot(s3)








#%%废
s=s.replace(to_replace=s[s['Day1']>520]['Day2'],value=200+np.random.binomial(n=800,p=0.5,size=len(s[s['Day1']>520]))
s=s.replace(to_replace=s[s['Day1']<480]['Day2'],value=np.random.binomial(n=800,p=0.5,size=len([s['Day1']<480])))
s=s.replace(to_replace=s[s['Day1']<460]['Day2'],value=np.random.binomial(n=600,p=0.5,size=len([s['Day1']<460]))



s[s['Day1']>520]['Day2']=200+np.random.binomial(n=800,p=0.5,size=len(s[s['Day1']>520]['Day2']))
s[s['Day1']<480]['Day2']=np.random.binomial(n=800,p=0.5)
s[s['Day1']<460]['Day2']=np.random.binomial(n=600,p=0.5)

s['Day2'].plot.hist(bins=200)
s['Day1'].plot.hist(bins=200)




c=pd.DataFrame(columns=['D1','D2'])
c['D1']=s[s['Day1']>520].loc['Day2']
c['D2']=200+np.random.binomial(n=800,p=0.5)


d=s[s['Day1']>520]['Day2']
d.plot.hist()

c.plot.hist()

c=200+np.random.binomial(n=800,p=0.5,size=len(s[s['Day1']>520]['Day2']))
c.plot.hist()



import warnings
warnings.filterwarnings('ignore')