import pandas as pd

df = pd.read_csv('names.csv',parse_dates = True)

print(df.head())

print("\n We can multi index data the following way")

print(df.set_index(['Age','Gender'], inplace= True))

print(df.index)

print(df.loc[23])

print(df.loc[23].loc['Male'])