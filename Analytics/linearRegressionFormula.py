# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:00:39 2017

@author: Meharban waraich
"""
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = np.genfromtxt('sensordata.csv', delimiter = ',')


#plt.figure()
#plt.plot(data[:,0])

npMatrix = np.matrix(data)
x = npMatrix[:,3]
y = npMatrix[:,4]
mdl = LinearRegression().fit(x,y)

m = mdl.coef_[0]
b = mdl.intercept_
#print ("formula: y = {0}x + {1}".format(m, b))

print ("formula: y = {1} + {0}x".format(m,b))



plt.plot(data[:,1])
plt.plot(data[:,2])
plt.plot(data[:,3])
plt.plot(data[:,4])




plt.figure()
plt.hist(data[:,0])
plt.xlabel('temperature')
plt.ylabel('Frequency')
#plt.savefig('temp.png', transparent=False)

plt.figure()
plt.hist(data[:,1])
plt.xlabel('humidity')
plt.ylabel('Frequency')
#plt.savefig('humidity.png', transparent=False)

plt.figure()
plt.hist(data[:,2])
plt.xlabel('particulates')
plt.ylabel('Frequency')
#plt.savefig('particulates.png', transparent=False)

plt.figure()
plt.hist(data[:,3])
plt.xlabel('SO2')
plt.ylabel('Frequency')
#plt.savefig('SO2.png', transparent=False)

plt.figure()
plt.hist(data[:,4])
plt.xlabel('CO')
plt.ylabel('Frequency')
#plt.savefig('CO.png', transparent=False)

# Comparing temperature against Humidity,Particulates ,Sulphur dioxide,Carbon monoxide 

plt.figure()
plt.plot(data[:,0],data[:,1])
plt.xlabel('temperature')
plt.ylabel('Humidity')
#plt.savefig('tempandhumidity.png', transparent=False)

plt.figure()
plt.plot(data[:,0],data[:,2])
plt.xlabel('temperature')
plt.ylabel('Particulates')
#plt.savefig('tempandparticulates.png', transparent=False)



plt.figure()
plt.plot(data[:,0],data[:,3])
plt.xlabel('temperature')
plt.ylabel('Sulphur dioxide')
#plt.savefig('tempandsulphur.png', transparent=False)


plt.figure()
plt.plot(data[:,0],data[:,4])
plt.xlabel('temperature')
plt.ylabel('Carbon monoxide')
#plt.savefig('tempandcarbon.png', transparent=False)

 #Comparing Humidity against Particulates ,Sulphur dioxide,Carbon monoxide

plt.figure()
plt.plot(data[:,1],data[:,2])
plt.xlabel('Humidity')
plt.ylabel('Particulates')
#plt.savefig('humidityandparticulates.png', transparent=False)

plt.figure()
plt.plot(data[:,1],data[:,3])
plt.xlabel('Humidity')
plt.ylabel('Sulphur dioxide')
#plt.savefig('humidityandsulphur.png', transparent=False)

plt.figure()
plt.plot(data[:,1],data[:,4])
plt.xlabel('Humidity')
plt.ylabel('Carbon monoxide')
#plt.savefig('humidityandcarbon.png', transparent=False)

 #Comparing Particulates against Sulphur dioxide and Carbon monoxide 

plt.figure()
plt.plot(data[:,2],data[:,3])
plt.xlabel('Particulates')
plt.ylabel('Sulphur dioxide')
#plt.savefig('particulatesandsulphur.png', transparent=False)

plt.figure()
plt.plot(data[:,2],data[:,4])
plt.xlabel('Particulates')
plt.ylabel('Carbon monoxide')
#plt.savefig('particulatesandcarbon.png', transparent=False)

# Comparing Sulphur dioxide against Carbon monoxide 

plt.figure()
plt.plot(data[:,3],data[:,4])
plt.xlabel('Sulphur dioxide')
plt.ylabel('Carbon monoxide')
#plt.savefig('sulphurandcarbon.png', transparent=False)
