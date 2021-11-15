# (c)
import numpy as np
r,c = input("Enter the dimentions of array M x N \n").split()
given_arr=np.random.random ([3,4]) * 10
print(given_arr)
print("Shape of Array :",np.shape(given_arr))
print("Type of Array :",type(given_arr))
print("Data type of Array : ",given_arr.dtype)

