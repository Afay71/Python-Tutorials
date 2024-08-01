# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

ageList = [10, 20, 30, 30, 30, 40, 50, 60, 70, 75]
weightList = [20, 60, 80, 85, 86, 87, 70, 90, 95, 90]

numpyAgeList = np.array(ageList)
numpyWeightList = np.array(weightList)
# Convert lists to NumPy arrays. This makes working with data easier.

plt.plot(numpyAgeList, numpyWeightList, 'y')  
# Create a line graph using two NumPy arrays. The 'y' color code represents yellow.
plt.xlabel('Age')
plt.ylabel('Weight')
# Set axis labels.
plt.show()
# Call plt.show() to display the graph.

numpyArray1 = np.linspace(0, 10, 20)
print(numpyArray1)
numpyArray2 = (numpyArray1 ** 3)

plt.plot(numpyArray1, numpyArray2, "b*-") 
# Create another line graph. The line is blue ('b'), uses star markers, and is dashed.
plt.show()
# Call plt.show() to display the graph.

plt.subplot(1, 2, 1)
# Create a subplot to show multiple graphs side by side. (1 row, 2 columns, 1st subplot)
plt.plot(numpyArray1, numpyArray2, "r*-")
# Create another line graph. The line is red ('r') and uses star markers.
plt.show()
# Call plt.show() to display the subplot.

plt.subplot(1, 2, 2)
plt.plot(numpyArray2, numpyArray1, "g--")
# Create another line graph. The line is green ('g') and dashed (--).
plt.show()
# Call plt.show() to display the subplot.

