import pandas as pd 
import os

data = pd.read_csv("elements.csv")

print(data.iloc[5:6,5:6])
print(data.index[1])

print(data[["Element", "Symbol"]])