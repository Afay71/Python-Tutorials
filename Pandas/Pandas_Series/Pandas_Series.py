# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# SERIES
myDictionary = {"Atil": 50, "Zeynep": 40, "Mehmet": 30}
print(pd.Series(myDictionary))

myAges = [50, 40, 30]
myNames = ["Atil", "Zeynep", "Mehmet"]
print(pd.Series(myAges))
print(pd.Series(myAges, myNames))
print(pd.Series(data=myAges, index=myNames))

numpyArray = np.array([50, 40, 30])
print(pd.Series(numpyArray))
print(pd.Series(numpyArray, myNames))
# This way we can create a series both with an array and a dictionary.

## SERIES FEATURES
competitionResults = pd.Series([10, 5, 1], ["Atil", "Atlas", "Osman"])
print(competitionResults)

competitionResults2 = pd.Series([20, 10, 8], ["Atil", "Atlas", "Osman"])
print(competitionResults2)

finalResult = competitionResults + competitionResults2
print(finalResult)

differentSeries = pd.Series([20, 30, 40, 50], ["a", "b", "c", "d"])
differentSeries2 = pd.Series([10, 5, 3, 1], ["a", "c", "f", "g"])
print(differentSeries)
print(differentSeries2)

print(differentSeries + differentSeries2) # This will only give the sum of 'a' and 'c'.

