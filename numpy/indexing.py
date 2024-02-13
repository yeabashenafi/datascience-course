import numpy as np

array_1d = np.array([1,2,3,4,5,6])
array_2d = np.array([[1,2,3],[4,5,6]])
array_3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

print("\nLet's create multi dimensional arrays")

print(array_1d)
print(array_2d)
print(array_3d)

print("\nThe 1d array can be accessed like lists a[i]")
print(array_1d[0], array_1d[2], array_1d[-1])

print("\nThe 2d array can be accessed like a[i][j]. i-horiznotal(row) j-vertical(column)")
print(array_2d[0,1],array_2d[0,2],array_2d[1,2])

print("Negative indices can also be used for 2d arrays a[i][-1]")
print(array_2d[1,-2])


print("\nThe 3d array can be accessed by a[i][j][k]. i-which outer array j -horizontal(row) k - vertical(column)")
print(array_3d[0,0,0],array_3d[1,1,1])

print("Negative indexing is allowed in all the array types")