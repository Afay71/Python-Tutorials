# -*- coding: utf-8 -*-
import numpy as np

myarray = np.arange(0,15)
print(myarray)
print(myarray[5]) 
print(myarray[3:8]) 
print(myarray[3:8] == -5) 

otherarray = np.arange(0,24)
print(otherarray)

slicingarray = otherarray[4:9]
print(slicingarray)

slicingarray[:] = 700 
print(slicingarray)
print(otherarray)       

##MATRİX
mylist = [[10,20,30], [20,30,40], [30,40,50]]
MyMatrixArray = np.array(mylist)
print(MyMatrixArray)
print(MyMatrixArray[0])
print(MyMatrixArray[1,2])

newlist = [[0,1, 2, 3,4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14 ], [15, 16, 17, 18, 19 ], [20, 21, 22, 23, 24 ] ]
newMatrix = np.array (newlist)
print(newMatrix)

print(newMatrix[[4,2,0]]) 
 
##OPERASYONLAR
AnewArray = np.random.randint(1,100,20)
print(AnewArray)
print(AnewArray > 24) 

resultArray = AnewArray > 24
print(resultArray)
print(AnewArray[resultArray])

lastarray = np.arange(0,24)
print(lastarray + lastarray) 
print(np.max(lastarray))
print(np.min(lastarray))

