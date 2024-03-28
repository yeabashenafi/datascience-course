import pandas as pd

df = pd.read_csv('names.csv')

print(df.head())

print(df.plot())

print(df['Age'].plot())

print(df['Age'].plot(legend=True))

print(df.plot(x='Age',y='Name',kind='scatter',legend=True))