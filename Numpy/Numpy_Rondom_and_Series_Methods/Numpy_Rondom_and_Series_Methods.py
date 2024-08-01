# -*- coding: utf-8 -*-
import numpy as np

##RANDOM
print(np.random.randn(6))
print(np.random.randn(4,4))
print(np.random.randint(1,10))
print(np.random.randint(1,300,5)) #5 random int numbers from 1 to 300

myNumpyArray = np.arange(30)
print(myNumpyArray)

myRandomArray = np.random.randint(0,100,20)
print(myRandomArray)

##DÝZÝ METHODLARI
print(myNumpyArray.reshape(5,6)) #matrix creation (but it must be suitable for the number of arrays)
print(myNumpyArray.max())
print(myRandomArray.min())
print(myNumpyArray.argmax()) #max value element
print(myRandomArray.argmin()) #min value element

reshapeArray = myNumpyArray.reshape(5,6) #function is used to change the shape of an array. 
print(reshapeArray.shape) #This code will print the row and column numbers.
