# pandas series use numpy in the numpy

import pandas as pd

l = [x for x in range(5)]

s = pd.Series(l)


print(s)

print("s[3] is")
print(s[3])

print("\nManually indexing the series will be like")

s = pd.Series(l, index = ['a','b','c','d','e'])

print(s)

print("s[e] is {}".format(s['e']))

print("\n Indexes of a series can be repeated")

s = pd.Series(l, index = ['a','b','c','d','d'])

print(s)

print("\n We can also create series from dicts")

data = {"a":1,"b":2,"c":3,"d":25}

s = pd.Series(data)
print(s)

print("We can also select the keys to be included in the dict")
s = pd.Series(data, index = ['a','c','d'])

print(s)

print("\n We can also select indexes which don't exist when creating series from a dict")

s = pd.Series(data, index = ['a','c','d','f'])

print(s)
