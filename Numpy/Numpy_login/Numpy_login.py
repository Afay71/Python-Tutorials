# -*- coding: utf-8 -*-
import numpy as np 

##NUMPY ARRAY 
mylist = [20,30,40]
print(type(mylist))

print(np.array(mylist))

Matrix_list = [[10,20,30], [20,30,40], [30,40,50]]

print(Matrix_list[1][0])

print(np.array(Matrix_list)) 

## ARANGE
list(range(0,10))
print(np.arange(0,10))
print(np.arange(0,20,2))

##ZEROS
print(np.zeros(5))
print(np.zeros((9,9)))
print(np.ones((9,9)))

##LÝNSPACE
print(np.linspace(0,10,20)) 

##EYE
print(np.eye(10)) 
