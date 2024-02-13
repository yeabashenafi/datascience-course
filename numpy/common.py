import numpy as np

arr = np.array([[4,3,2],[10,1,0],[5,8,24]])

print(arr)

print("\nFind the minimum value")

print(np.amin(arr))

print("\nFind the minimum value by axis")
print("axis 0 is vertical while axis 1 is horizontal")

print("\nFind the minimum value in axis 0")
print(np.amin(arr,axis=0))

print("\nFind the minimum value in axis 1")
print(np.amin(arr,axis=1))

print("\nSimilarly we have the min,amax,max methods")

print("\nThe mean method")
print(np.mean(arr))

print("\nThe median method")
print(np.median(arr))

print("\nThe standard deviation method")
print(np.std(arr))

print("\nThe variance method")
print(np.var(arr))

print("\n The percentile method")
print(np.percentile(arr,20))

print("\nNumpy has useful functions for degrees too")

deg = np.array([0,30,45,60,90])
print(deg)

print("\nNumpy has sin ,cos , tan and others for degress")

print(np.sin(deg*np.pi/180))

print(np.cos(deg*np.pi/180))

print(np.tan(deg*np.pi/180))

# the inverses can also be found by using
'''
arcsin
arccos
arctan
'''

print("\nThere are also floor and ceil functions available")
newarr = np.array([0.1,0.8,-2.2,-9.87])
print(newarr)

print("\nThe floor function")
print(np.floor(newarr))

print("\nThe ceil function")
print(np.ceil(newarr))