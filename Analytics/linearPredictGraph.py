# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 15:10:35 2017

@author: Meharban waraich
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Read in csv file
# File: https://github.com/mGalarnyk/Python_Tutorials/blob/master/Python_Basics/Linear_Regression/linear.csv
data = pd.read_csv("sensordata.csv")

# Removes rows with NaN in them
#filtered_data = raw_data[~np.isnan(raw_data["y"])] 

x_y = np.array(data)
x, y = x_y[:,3], x_y[:,4]

# Reshaping
x, y = x.reshape(-1,1), y.reshape(-1, 1)

# Linear Regression Object 
lin_regression = LinearRegression()

# Fitting linear model to the data
lin_regression.fit(x,y)

# Get slope of fitted line
m = lin_regression.coef_

# Get y-Intercept of the Line
b = lin_regression.intercept_

# Get Predictions for original x values
# you can also get predictions for new data
predictions = lin_regression.predict(x)

# following slope intercept form 
print ("formula: y = {0}x + {1}".format(m, b)) 

# Plot the Original Model (Black) and Predictions (Blue)
plt.scatter(x, y,  color='black')
plt.plot(x, predictions, color='blue',linewidth=3)
plt.show()