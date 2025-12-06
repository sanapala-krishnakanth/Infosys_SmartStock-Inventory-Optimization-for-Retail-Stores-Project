import pandas as pd
import numpy as np
df = pd.read_csv("E:\Smart stock optimization for retail stores\data preprocessing\smart-stock.csv")
df.fillna(method='ffill',inplace=True)
print(df.head(20)) 

