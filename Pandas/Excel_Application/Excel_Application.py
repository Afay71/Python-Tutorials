# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

dataFrame = pd.read_excel("C:\\Users\\Arif Furkan\\OneDrive\\Belgeler\\python.xlsx") # From Excel to Python
print(dataFrame)

nonNullDataFrame = dataFrame.dropna()
print(nonNullDataFrame)

nonNullDataFrame.to_excel("C:\\Users\\Arif Furkan\\OneDrive\\Belgeler\\yeniPython.xlsx") # From Python to Excel

