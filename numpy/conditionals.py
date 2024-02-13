import numpy as np

x = np.array([x for x in range(10)])

print(x)

print("\nNumpy where conditions")
print(np.where(x % 2 == 0, 'Even', 'Odd'))

print("\nNumpy select conditions")

print("\nFirst set the condition list")
condList = [x<5,x>5]

print("\nThen set the choice list")
choiceList = [x**2, x**3]

print("\nThe select condition uses the condList and the choiceList")
print(np.select(condList,choiceList,default=x))