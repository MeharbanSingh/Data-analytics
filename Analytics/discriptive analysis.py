# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 11:41:48 2017

@author: Meharban waraich
"""

import numpy as np
from scipy import stats

data = np.genfromtxt('sensordata.csv',delimiter = ',')

#Apply descriptive analysis 

#mean
print('mean')
a = data[:,0]
meanTemp = np.mean(a)
print(meanTemp)

b = data[:,1]
meanHumidity = np.mean(b)
print(meanHumidity)

c = data[:,2]
meanParticulates = np.mean(c)
print(meanParticulates)


d = data[:,3]
meanSO2 = np.mean(d)
print(meanSO2)

e = data[:,4]
meanCO = np.mean(e)
print(meanCO)

print("\n")


#median

print('median')

medianTemp = np.median(a)
print(medianTemp)

medianHumidity = np.median(b)
print(medianHumidity)

medianParticulates = np.median(c)
print(medianParticulates)

medianSO2 = np.median(d)
print(medianSO2)

medianCO = np.median(e)
print(medianCO)


print('\n')

#Standard Deviation
print('standard deviation')

stdTemp = np.std(a)
print(stdTemp)

stdHumidity = np.std(b)
print(stdHumidity)

stdParticulates = np.std(c)
print(stdParticulates)

stdSO2 = np.std(d)
print(stdSO2)

stdCO = np.std(e)
print(stdCO)

print('\n')

#Minimum
print('Min')

minTemp = np.min(a)
print(minTemp)

minHumidity = np.min(b)
print(minHumidity)

minParticulates = np.min(c)
print(minParticulates)

minSO2 = np.min(d)
print(minSO2)

minCO = np.min(e)
print(minCO)

print('\n')
#maximum
print('Max')
maxTemp = np.max(a)
print(maxTemp)

maxHumidity = np.max(b)
print(maxHumidity)

maxParticulates = np.max(c)
print(maxParticulates)

maxSO2 = np.max(d)
print(maxSO2)

maxCO = np.max(e)
print(maxCO)

print('\n')

#Range

print('Range')

rangeTemp = maxTemp-minTemp
print(rangeTemp)

rangeHumidity = maxHumidity-minHumidity
print(rangeHumidity)

rangeParticulates = maxParticulates-minParticulates
print(rangeParticulates)

rangeSO2 = maxSO2-minSO2
print(rangeSO2)

rangeCO = maxCO-minCO
print(rangeCO)

print('\n')

#Variance

print('variance')

varianceTemp = np.var(a)
print(varianceTemp)

varianceHumidity = np.var(b)
print(varianceTemp)

varianceParticulates = np.var(c)
print(varianceParticulates)

varianceSO2 = np.var(d)
print(varianceSO2)

varianceCO = np.var(e)
print(varianceCO)

print('\n')




