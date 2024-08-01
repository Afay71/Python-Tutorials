# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

dictionary1 = {"Name" : ["Ahmet", "Mehmet", "Zeynep", "Atil"],
"Sport" : ["Running", "Swimming", "Running", "Basketball"],
"Calories" : [100, 200, 300, 400]}

dataFrame1 = pd.DataFrame(dictionary1, index=[0, 1, 2, 3])
print(dataFrame1)

dictionary2 = {"Name" : ["Osman", "Levent", "Atlas", "Fatma"],
"Sport" : ["Running", "Swimming", "Running", "Basketball"],
"Calories" : [200, 100, 50, 300]}

dataFrame2 = pd.DataFrame(dictionary2, index=[4, 5, 6, 7])
print(dataFrame2)

dictionary3 = {"Name" : ["Ayse", "Mahmut", "Duygu", "Nur"],
"Sport" : ["Running", "Swimming", "Badminton", "Tennis"],
"Calories" : [300, 400, 500, 250]}

dataFrame3 = pd.DataFrame(dictionary3, index=[8, 9, 10, 11])
print(dataFrame3)

# Concatenation CONCAT
dataFrame4 = pd.concat([dataFrame1, dataFrame2, dataFrame3], axis=0) # axis can also be 1, but that would cause an error
print(dataFrame4)

# MERGE
mergeDictionary1 = {"Name" : ["Ahmet", "Mehmet", "Zeynep", "Atil"],
"Sport" : ["Running", "Swimming", "Running", "Basketball"]}
mergeDataFrame1 = pd.DataFrame(mergeDictionary1)
print(mergeDataFrame1)

mergeDictionary2 = {"Name" : ["Ahmet", "Mehmet", "Zeynep", "Atil"],
"Calories" : [100, 200, 150, 250]}
mergeDataFrame2 = pd.DataFrame(mergeDictionary2)
print(mergeDataFrame2)

mergeDataFrame3 = pd.merge(mergeDataFrame1, mergeDataFrame2, on="Name")
print(mergeDataFrame3)

salaryDictionary = {"Name": ["Atil", "Zeynep", "Mehmet", "Ahmet"], 
                    "Department": ["Software", "Sales", "Marketing", "Software"],
                    "Salary": [200, 300, 500, 400]}
salaryDataFrame = pd.DataFrame(salaryDictionary)
print(salaryDataFrame)

print(salaryDataFrame["Department"].unique()) # What are the departments?
print(salaryDataFrame["Department"].nunique()) # How many unique departments are there?
print(salaryDataFrame["Department"].value_counts()) # How many are there in each department?

def grossToNet(salary):
    return salary * 0.66
print(salaryDataFrame["Salary"].apply(grossToNet)) # Apply the function to the table

