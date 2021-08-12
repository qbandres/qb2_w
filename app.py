import pandas as pd
import numpy as np

A = [3,0.45443,6.23423]
B=[5,6.343,np.NaN]

df= pd.DataFrame(list(zip(A,B)),columns=['A','B'])

print(df)

df['C']=df.A*df.B

print(df)