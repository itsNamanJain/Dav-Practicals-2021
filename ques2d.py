# (d)
import numpy as np
import math
given_arr =[2,0,1,np.NaN, True,np.NaN,8,0]
print(given_arr)
zero_arr = []
non_zero_arr = []
NaN_arr = []
for i in range(len(given_arr)):
    if np.isnan(given_arr[i]):
        NaN_arr.append(i)
    elif np.any(given_arr[i]):
        non_zero_arr.append(i)
    else:
        zero_arr.append(i)
        
print(f"NaN Index {NaN_arr}")
print(f"Non-zero Index {non_zero_arr}")
print(f"Zero Index {zero_arr}")