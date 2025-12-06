import pandas as pd

df = pd.read_csv("E:\Smart stock optimization for retail stores\data preprocessing\smart-stock.csv")
print(df['sales'].agg(['mean','min','max','count','sum']))
 
 