# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

numpyArray1 = np.linspace(0, 10, 20)
numpyArray2 = (numpyArray1 ** 3)

myFigure = plt.figure()
figureAxes = myFigure.add_axes([0.15, 0.15, 0.8, 0.8])
# The first two values specify the position of the bottom left corner, and the last two values specify the width and height ratios.
figureAxes.plot(numpyArray1, numpyArray2, "g")
figureAxes.set_xlabel("X Axis Data Name")
figureAxes.set_ylabel("Y Axis Data Name")
figureAxes.set_title("Graph Title")
plt.show()

# NESTED GRAPH
figure2 = plt.figure()
axis1 = figure2.add_axes([0.1, 0.1, 0.7, 0.7])
axis2 = figure2.add_axes([0.2, 0.4, 0.3, 0.3])

axis1.plot(numpyArray1, numpyArray2, "g")
axis1.set_xlabel("X Axis")
axis1.set_ylabel("Y Axis")
axis1.set_title("Main Graph Title")

axis2.plot(numpyArray2, numpyArray1, "b")
axis2.set_xlabel("X Axis")
axis2.set_ylabel("Y Axis")
axis2.set_title("Small Graph Title")
plt.show()

# SUBPLOTS
(myFigure, myAxes) = plt.subplots()
(myFigure, myAxes) = plt.subplots()
myAxes.plot(numpyArray1, numpyArray2, "b")

(myFigure, myAxes) = plt.subplots(nrows=1, ncols=2)
type(myAxes) # Since it is an array, we iterate over the axes to plot them.
for axis in myAxes:
    axis.plot(numpyArray1, numpyArray2, "g")
    axis.set_xlabel("X Axis")
    axis.set_ylabel("Y Axis")
    plt.tight_layout()
plt.show()

newFigure = plt.figure(dpi=100)
# "dpi": This specifies the number of dots per inch and sets the graph resolution.
newAxis = newFigure.add_axes([0.1, 0.1, 0.8, 0.8])
newAxis.plot(numpyArray1, numpyArray1 ** 2, label="numpyArray ** 2")
# "label": This usually represents the names or descriptions of the data series plotted in the graph.
newAxis.legend(loc=1) # Calling the legend function ensures that these labels are displayed.
# The "loc" parameter determines the position of the legend.
plt.show()

