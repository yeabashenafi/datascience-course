import numpy as np

a = np.array([[1,2,3],[4,5,6]])

b = np.array([7,8,9])

print("Value of a")
print(a)

print("\nValue of b")
print(b)

# add the arrays
print("\n a + b is ")
print(np.add(a,b))

print("\n b + a is ")
print(np.add(b,a))

# subtract the arrays
print("\n a - b is ")
print(np.subtract(a,b))

print("\n b - a is")
print(np.subtract(b,a))

# multiply the arrays
print("\n a * b is ")
print(np.multiply(a,b))

# divide the arrays

print("\n a / b is")
print(np.divide(a,b))

print("\n b / a is")
print(np.divide(b,a))

# exponential values
print("\nThe power method with a value 2")
print(np.power(a,2))

# exponential values with another array
print("\n The power method with another numpy array")
print(np.power(a,b))