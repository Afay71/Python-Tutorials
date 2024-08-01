# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# Missing Data
dictionaryData = {"Istanbul" : [30, 29, np.nan], "Ankara" : [20, np.nan, 25], "Izmir" : [40, 39, 38]}
weatherDataFrame = pd.DataFrame(dictionaryData)
print(weatherDataFrame)

newData = {"Istanbul" : [30, 29, np.nan], "Ankara" : [20, np.nan, 25], "Izmir" : [40, 39, 38], "Antalya" : [45, np.nan, np.nan]}
newDataFrame = pd.DataFrame(newData)
print(newDataFrame)
print(newDataFrame.dropna(axis=1, thresh=2)) # Drop columns with more than 2 NaN values
newDataFrame.fillna(20, inplace=True) # Fill all NaN values with 20
print(newDataFrame)

# Grouping
salaryDictionary = {"Department" : ["Software", "Software", "Finance", "Finance", "Law", "Law"],
"Employee Name" : ["Ahmet", "Mehmet", "Atil", "Burak", "Zeynep", "Fatma"],
"Salary" : [100, 150, 200, 300, 400, 500]}
salaryDataFrame = pd.DataFrame(salaryDictionary)
print(salaryDataFrame)

groupObject = salaryDataFrame.groupby("Department")
print(groupObject.count())
