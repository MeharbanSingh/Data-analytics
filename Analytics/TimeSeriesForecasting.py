# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:44:32 2017

@author: waraich
"""

import numpy as np
import pandas as pd


# read csv file
# {'Temp': np.float32, 'Humidity': np.float32, 'Particulates': np.float32, 'SO2': np.float32, 'CO': np.float32}

data = pd.read_csv('sensordata.csv', delimiter=',') 
data.columns = ['Temp','Humidity','Particulates','SO2','CO','Time','Date']
# header is conveniently inferred by default  
print(data.columns)   # print column names

data['Date'] = data['Date'] + ' ' + data['Time']  # concatinate date and time columns
data = data.drop('Time',1) # remove time column
print(data.columns)
data['Date'] = pd.to_datetime(data['Date'], format = '%d %b %Y %I:%M:%S %p', errors='coerce')
data = data.convert_objects(convert_numeric=True)
# set Date as index
data.index = data['Date']
# delete Date column
del data['Date']  
#print(data)

#%%
# creating time series


#ts = pd.Series(np.array(data['Temp']), data.Date)
#ts = pd.Series(data.Date,np.array(data['Humidity']))
#data.plot(figsize=(12,8), title='Sensor Data')
#fig = plt.gcf()
#plt.show()

#%% normalizing data

data_norm = (data - data.mean()) / (data.max() - data.min())


import matplotlib.pyplot as plt 
#plt.style.use('ggplot')


plt.figure()
plt.title('Sensor Data (Normalized)')
plt.xlabel('Date')
plt.ylabel('Pollution')
plt.legend(loc='upper right')
plt.plot(data_norm.Temp, label='Temperature')
plt.plot(data_norm.Humidity, label='Humidity')
plt.plot(data_norm.Particulates, label='Particulates')
plt.plot(data_norm.SO2, label='SO2')
plt.plot(data_norm.CO, label='CO')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
#plt.margins(0.2)
plt.show()



#%%

#import matplotlib
#matplotlib.use("GTKCairo")
#matplotlib.use('pdf')

import matplotlib.pyplot as plt 
plt.style.use('ggplot')

plt.figure()
plt.title('Sensor Data')
plt.xlabel('Date')
plt.ylabel('Pollution')
plt.legend(loc='upper left')
#plt.plot(data['Date'],data['Temp']) 
#plt.plot(data['Date'],data['Humidity']) 
#plt.plot(data['Date'],data['Particulates'])
#plt.plot(data['Date'],data['SO2'])
#plt.plot(data['Date'],data['CO'])
plt.plot(data.Temp, label='Temperature')
plt.plot(data.Humidity, label='Humidity')
plt.plot(data.Particulates, label='Particulates')
plt.plot(data.SO2, label='SO2')
plt.plot(data.CO, label='CO')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.margins(0.2)
plt.show()#plt.savefig('out.pdf', transparent=False, bbox_inches='tight', pad_inches=0)
#%%
# create scatter matrix
from pandas.tools.plotting import scatter_matrix
scatter_matrix(data,diagonal='kde', alpha=0.1,figsize=(12,12))
plt.show()
plt.savefig('scatter_materix.png', transparent=False, bbox_inches='tight', pad_inches=0)

#%%
# install statmodels form shell
#pip install statsmodels
#
#import statsmodels.api as sm

#resample to 5 min interval
#temp = data.Temp
#temp.fillna(method='pad')
#down_sampled = temp.resample('1T', how='sum')

#decompositon frequency
# see http://www.cbcity.de/timeseries-decomposition-in-python-with-statsmodels-and-pandas
#decompfreq = 24*60/15*7

#decompose the ts
#res = sm.tsa.seasonal_decompose(down_sampled, freq=decompfreq, model='additive', filt=)
#resplot = res.plot()