import numpy as np

print("Getting Contents of a csv file with the loadtxt method")

arr = np.loadtxt('names.csv',delimiter=',',dtype=str)

print(arr)

print("\nWe can also use the genfromtxt method")
arr = np.genfromtxt('names.csv',delimiter=',',dtype=str)

print(arr)

print("\nWe can also export the content of arrays to a csv file")
arr = np.array([[1,2,3],[4,5,6]])
print(arr)

np.savetxt('2darray.csv',arr,delimiter=',')

print("\nWe can also save the file in npy format which saves memory")

np.save('file.npy',arr)

print("\We can load the .npy file created with the load method")

arr = np.load('file.npy')

print(arr)
