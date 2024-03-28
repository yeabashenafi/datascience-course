# dataframes are used to retabulate data
import pandas as pd

df= pd.DataFrame()

type(df)

df = pd.read_csv('names.csv')

print(df)

print("\nThe common mehtods available are head and tail")

print(df.head())

print(df.tail())

print("\nThis methods can also receive params for no of elements")

print(df.head(2))

print(df.tail(2))

print("\nWe can also fetch using the iloc method by using indexes")

print(df.iloc[2])

print("\n The values property")

print(df.values)


print("\n We can also create different data frames with the following method which are iterable")

df = pd.read_csv('names.csv', chunksize= 1)

for chunk in df:
    print(chunk)


print("\n We can also use filtering in the following way")

df = pd.read_csv('names.csv')

df = df[df['Age'] > 23]

print(df)