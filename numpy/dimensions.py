
import numpy as np

numpy_arr = np.array([ x for x in range(1,10)])

print(numpy_arr)

print("Converting the array to 2d")

print(numpy_arr.reshape(3,3))

# reshaping the array with custom dimensions

sec_numpy_arr = np.array([ x for x in range(1,13)])

print(sec_numpy_arr)

print("Converting the array to 2 by 2 by 3")

print(sec_numpy_arr.reshape(2,2,3))

# The size of the array must be equal to the product of the parameters

# Dynamic reshaping

print("Dynamic Re shaping")

print(sec_numpy_arr.reshape(2,2,-1))

# flattening the array
sec_numpy_arr_3d = sec_numpy_arr.reshape(2,2,3)

print("Flattening the array")

print(sec_numpy_arr_3d.reshape(-1))