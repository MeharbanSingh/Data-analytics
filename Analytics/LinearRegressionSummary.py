# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 15:58:15 2017

@author:Meharban  waraich
"""
#Import all required libraries
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.interpolate import*
import pandas as pd

data = np.genfromtxt('sensordata.csv', delimiter = ',' )

meanX = np.mean(data[:,0])
meany = np.mean(data[:,3])
#print(meanX)
#print(meany)


x = data[:,0]
y = data[:,3]



p1 = np.polyfit(x,y,1)
#print(p1)

p2 = np.polyfit(x,y,2)
#print(p2)

p3 = np.polyfit(x,y,3)
#print(p3)

coeficent = np.corrcoef(x,y)

# draw polynomial graph

#xp = np.linspace(0,40,100)
#plt.plot(x,y, ':',color = 'black')
#plt.xlabel('Particulates')
#plt.ylabel('CO')

#plt.plot(x,np.polyval(p1,x),'r-')
#plt.savefig('residualParticulatesandCO.png', transparent=False, bbox_inches='tight', pad_inches=0)


#plt.plot(xp,np.polyval(p2,xp),'b--')
#plt.plot(xp,np.polyval(p3,xp),'y--')

#print(coeficent)

yfit = p1[0]*x +p1[1]
print(yfit)
print(y)

yresidual = y-yfit
sumofsquareresidual = sum(pow(yresidual,2))
sumofsquaretotal = len(y) * np.var(y)
rsquared = 1- sumofsquareresidual/sumofsquaretotal
print(rsquared)
# draw residual graph
sns.residplot(y,yresidual)