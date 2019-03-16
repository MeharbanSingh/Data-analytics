# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:11:58 2017

@author:Meharban waraich
"""

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd

data = np.genfromtxt('sensordata.csv', delimiter = ',' )

#data = pd.read_csv('sensordata.csv')

#print(data.describe())

#print(data.head(35000))

#print(data.isnull().sum())

#data.dropna(inplace = True)
#print(data.shape)

#load data colunm in variable x

x = data[:,6]
#print out any na value
print(np.argwhere(np.isnan(x)))

#print(x[30969])
"""
meanX = np.nanmean(data[:,0])
meany = np.nanmean(data[:,3])
print(meanX)
print(meany)
"""