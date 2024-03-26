import pandas as pd

s = pd.Series([x for x in range(1,11)])

print(s)

print("We can return the element with the 0th index with iloc")

print(s.iloc[0])

print("The same can also be done for accessing index using iat")

print("The 5th element is {}".format(s.iat[5]))

print("\n We can slice the series just like an array")

print(s[3:6])

print("\n We can also use negative indexing")

print(s[-4:-1])

print("\n We can use the where method to use conditional operaitons. Returns null when the conditions are not true")

print(s.where(s %2 ==0))

print("We can also use the value which will be displayed when the condition is false")

print(s.where(s % 2 == 0, "Odd Number"))

print("We can also perform another operation where the first condition is not true")

print(s.where(s % 2 == 0, s ** 2))

print("We can also deal with null values the following way")

s.where(s % 2 == 0, inplace = True)

print(s.dropna())

print("The fillna function will also be used the null value with a value specified")

print(s.fillna('filled value'))