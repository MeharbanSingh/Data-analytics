# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:39:03 2017

@author: Meharban singh
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:04:21 2017

@author: waraich
"""
#First import all the required libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
from pandas import DataFrame

#Read and load data in a variable called data
data = pd.read_csv('sensordata.csv')

#Assign coloumns names to data
data.columns = ['Temperature','Humidity','Particulates','SO2','CO','TIME','DATE']
#print(data.head())
print('summary of data')
print(data.describe())
print('\n')
print('Correlation cofficient')
print(data.corr())

print('\n')
#load columns in Variable A and B
A = data.iloc[:,[0,1,2,3]]
B = data.iloc[:,4]

A = sm.add_constant(A)
est1 = sm.OLS(B,A).fit()

print('\n')

print(est1.summary())

predict_value = est1.predict(A)
print(predict_value)

residual = B-predict_value
print(residual)

