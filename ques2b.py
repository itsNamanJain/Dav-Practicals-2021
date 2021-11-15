# (b)
import numpy as np
given_arr = np.array([56, 48, 22, 41, 78, 91, 24, 46, 8, 33])
print("Original array:")
print(given_arr)
i = np.argsort(given_arr)
print("Indices of the sorted elements of a given array:")
print(i)