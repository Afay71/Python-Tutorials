# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
                                                      #1)alpha: This parameter determines the opacity of the line or marker. It should be a decimal number between 0 and 1.
numpyArray1 = np.linspace(0,10,20)                    #0 means fully transparent, while 1 means fully opaque.
numpyArray2 = numpyArray1 ** 2                        #2)linewidth: This parameter determines the thickness of the line. It can be a decimal or an integer value.
                                                      #3)linestyle: This parameter determines the style or pattern of the line. For example, "--" represents a dashed line.
(myFigure, myAxes) = plt.subplots()                   #4)marker: This parameter determines the type of marker on the line. For example, "o" represents a dot.
myAxes.plot(numpyArray1, numpyArray2, "g")            #5)markersize: This parameter determines the size of the marker. It should be an integer value.
myAxes.plot(numpyArray2, numpyArray1, "b")            #6)markerfacecolor: This parameter determines the fill color of the marker. For example, "red" or HEX codes (#RRGGBB).
plt.show()                                                                                                         #
                                                                                                                   #
(myFigure, myAxes) = plt.subplots ()                                                                               #
myAxes.plot(numpyArray1, numpyArray2, "g", alpha=0.5)    # 1)  <---------------------------------------------------#
myAxes.plot(numpyArray2, numpyArray1, "b", linewidth=5.0) # 2) <---------------------------------------------------#
plt.show()                                                                                                         #
                                                                                                                   #
(newFigure, newAxes) = plt.subplots ()                                                                             #
newAxes.plot(numpyArray1, numpyArray1 + 4, color="green", linestyle = "-.") # 3) <---------------------------------# 
newAxes.plot(numpyArray1, numpyArray1 + 5, color="yellow", linestyle = ":")                                        #
newAxes.plot(numpyArray1, numpyArray1 + 6, color="blue", linestyle = "--")                                         #
                                                                            # 4)<-----------5)--------------6)-----#
newAxes.plot(numpyArray1, numpyArray1 + 7, color="#000000", linestyle = "--", marker = "o", markersize = 4, markerfacecolor="red")
newAxes.plot(numpyArray1, numpyArray1 + 8, color="#000000", linestyle = "--", marker = "+", markersize = 8, markerfacecolor="red")
plt.show()                                     # you can't write "black", so you write the HEX code, which is "000000".

# SCATTER
plt.scatter(numpyArray1, numpyArray2)
plt.show()

# HISTOGRAM
newArray = np.random.randint(0, 100, 50)
print(newArray)
plt.hist(newArray)
plt.show()

# BOXPLOT
plt.boxplot(newArray)
plt.show()

