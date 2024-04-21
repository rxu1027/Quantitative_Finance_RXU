# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 17:13:53 2022

@author: Machine Learning--Decision Tree
"""

import os
os.chdir('D:\\Python_otherinfo\\0.《Python金融》最新配套源代码文件（2020-12-07完善）\\第16章源代码汇总')
os.getcwd()

import pandas as pd
import sklearn
import matplotlib.pyplot as plt
## decision tree build-up

#1. separate information and result
df=pd.read_excel('D:\\Python_otherinfo\\0.《Python金融》最新配套源代码文件（2020-12-07完善）\\第16章源代码汇总\\客户信息及违约表现.xlsx')
X=df.drop(columns='是否违约')
y=df['是否违约']

#2. train set and test set
dir(sklearn)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=1)


#3. 模型训练ji搭建
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier(max_depth=3) #模型的最大深度为3
clf=clf.fit(X_train, y_train)


##Model prediction and evaluation
#1. directly predict whether this model can predict the result using test set
y_pred = clf.predict(X_test)
a=pd.DataFrame()
a['prediction']=list(y_pred)
a['actual']=list(y_test)
print(a.tail())

#verify accuracy
from sklearn.metrics import accuracy_score
score=accuracy_score(y_pred,y_test)   
print("the accuracy of test is",score)

#2. the probability of default
y_pred_proba=clf.predict_proba(X_test)
b=pd.DataFrame(y_pred_proba)
b.columns=["SF","PDF"]
print(b.head())
y_pred_proba[:,1]

#3. prediction evaluation
'''
True positive rate (命中率)---proportion of true defults that are predicted (实际违约中被正确预测到的比例)
False Positive rate (假报警率)---proportion of fake defults that are predicted(被预测为违约但是没有违约的比例)
Area Under the Curve (AUC)--measure the predictability of the model, the area under the curve of tpr and fpr
'''
from sklearn.metrics import roc_curve
fpr, tpr, thres = roc_curve(y_test.values,y_pred_proba[:,1])
c=pd.DataFrame()
c["thres"]=list(thres)
c["TPR"]=list(tpr)
c["FPR"]=list(fpr)

print(c[1:].head(20))

#plot the curve (roc)
plt.plot(fpr,tpr)
plt.show()

#calculate the AUC
from sklearn.metrics import roc_auc_score
score = roc_auc_score(y_test.values,y_pred_proba[:,1])
print("the Area Under Curve is ",score)














