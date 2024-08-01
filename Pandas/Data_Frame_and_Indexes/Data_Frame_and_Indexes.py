# -*- coding: utf-8 -*-
from xmlrpc.client import boolean
import numpy as np
import pandas as pd

data = np.random.randn(4,3)
print(data)
dataFrame = pd.DataFrame(data)
print(dataFrame)
print(dataFrame[0])

newDataFrame = pd.DataFrame(data, index=["Atil", "Zeynep", "Atlas", "Mehmet"], columns=["Salary", "Age", "Working Hours"])
print(newDataFrame)
print(newDataFrame["Age"]) # Select a specific column
print(newDataFrame.loc["Atil", "Age"]) # Select a specific cell
print(newDataFrame.loc["Atlas"]) # Select a specific row
print(newDataFrame.iloc[3]) # Select a specific row by position index
print(newDataFrame.iloc[:, 2]) # Select a specific column by position index

# Adding New Data (Index)
newDataFrame["Retirement Age"] = newDataFrame["Age"] + newDataFrame["Age"]
print(newDataFrame)

# Deleting Data (Index)
newDataFrame.drop("Mehmet", axis=0, inplace=True) # Here; axis=0 is row, axis=1 is column
newDataFrame.drop("Retirement Age", axis=1, inplace=True)
print(newDataFrame)

# Filtering Data (Index)
print(newDataFrame[newDataFrame < 0])
print(newDataFrame[newDataFrame["Working Hours"] > 0])

# Labeling Data (Index)
print(newDataFrame.reset_index())
newIndexList = ["Ati", "Zey", "Atl"]
newDataFrame["New Index"] = newIndexList
print(newDataFrame) # Here we just defined the new index.
newDataFrame.set_index("New Index", inplace=True) # With inplace=True we transferred the new index to names.
print(newDataFrame) 
print(newDataFrame.loc["Ati"])

# Categorizing Data (Index)
outerIndexes = ["Simpson", "Simpson", "Simpson", "South Park", "South Park", "South Park"]
innerIndexes = ["Homer", "Bart", "Marge", "Cartman", "Kenny", "Kyle"]
mergedIndexes = list(zip(outerIndexes, innerIndexes))
print(mergedIndexes)
mergedIndexes = pd.MultiIndex.from_tuples(sorted(mergedIndexes))
print(mergedIndexes)

myCartoonList = [[40, "A"], [10, "B"], [30, "C"], [9, "D"], [10, "E"], [11, "F"]] # Table data
cartoonNumpyArray = np.array(myCartoonList) # Create array
cartoonDataFrame = pd.DataFrame(cartoonNumpyArray, index=mergedIndexes, columns=["Age", "Profession"]) # Create categorical table
print(cartoonDataFrame)
cartoonDataFrame.index.names = ["Cartoon Name", "Name"]
print(cartoonDataFrame)

