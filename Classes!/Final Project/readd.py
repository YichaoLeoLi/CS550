import pandas as pd 
import os

data = pd.read_csv("elements.csv")

#print(data.iloc[5:6,5:6])
#print(data.index[1])

#a = data.iloc[5:6,5:6]
#float(a)
#print("Melting point", a)

#print(data[["Element", "Symbol"]])

col = data.iloc[:,0:0]
print(col)
s1 = data['Number']
print((data['Number'])[3])
