# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 22:47:51 2022

@author: lenovo
"""

#importing needed modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
#choose plots style
sns.set_style('darkgrid')
#make sure plots are inline with the notebook


## Loading the dataset and checking the columns we have

### Load your data and print out a few lines. Perform operations to inspect data
### Types and look for instances of missing or possibly errant data.
df = pd.read_csv('diabetes.csv')
df.head()

### Get the shape and types of our data
print(df.shape)
pd.DataFrame(df.dtypes)

### Get some statistics about our data
print(df.describe())

### Check if there is any missing values in our data
print(df.info())
print(df.isna().any())

### Check if there is any duplicated rows in our data
print(df.duplicated().any())
"""
print("SHOW HERE: ")
print(pd.DataFrame(df.columns))
"""
print("Datatypes-------------")
print(df.dtypes)

df.plot(kind = 'bar',
        y = 'Outcome',
        x = 'Age',
        color = 'red')
  
# set the title
plt.title('ScatterPlot')
  
# show the plot
plt.show()