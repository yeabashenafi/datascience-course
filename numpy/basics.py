# Numpy arrays are called nd arrays 
# Numpy mainly works with multi dimensional arrays
# ndarray is the numpy array 
# it has the properties
# ndarray.ndim - The number of axes (dimensions) of the array
# ndarray.shape - Tuple of integers that gives the size of the array in each dimension. For an m n matrix, shape is (n,m). The length of the shape is (n,m). The length of the shape tuple is the no of axes , ndim
# ndarray.size - The total number of elements of the array. Equal to the product of the elements of the shape.
# ndarray.dtype - An object that describes the type of elements in the array

## numpy types
# numpy.int32
# numpy.int16
# numpy.float64

# ndarray.itemsize - size in bytes of each elements of the array
# ndarray.data- the buffer contains the actual elements of the array but is not used to access the elements in the array since we use indexing for that.
# each element in an array is a 0-D array
import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
print(type(arr))

# create 2d arrays
twod_arr = np.array([[1,2,3], [4,5,6]])

print(twod_arr)
print("The number of dimensions of the array is {}".format(twod_arr.ndim))
print("The shape of the array is {}".format(twod_arr.shape))
print("The size of the array is {}".format(twod_arr.size))
print("The type of the elements in the array is {}".format(twod_arr.dtype))
print(type(arr))


# create an n-d array
ndarray = np.array([1,2,3,4,5],ndmin=3)

print("Creating an n dimensional array")
print(ndarray)