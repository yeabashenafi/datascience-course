import numpy as np

array_1d = np.array([1,2,3,4,5,6])
array_2d = np.array([[1,2,3],[4,5,6]])
array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print("\nLet's create multi dimensional arrays")

print(array_1d)
print(array_2d)
print(array_3d)

print("\n1d arrays will be sliced as normal python lists")
print(array_1d[1:], array_1d[:2],array_1d[0:-1])

print("\n2d arrays will be sliced as a[i,j:] i,j specifies the exact location of the starting value")
print(array_2d[1,1:])

print("Negative indices are also allowed")
print(array_2d[-2:-3:-1])

print("\n3d arrays can be sliced as a[i,j:,k:] i- specifies the initial array j- the row in the array and k the start of the elements")
print(array_3d[0,1:,1:])