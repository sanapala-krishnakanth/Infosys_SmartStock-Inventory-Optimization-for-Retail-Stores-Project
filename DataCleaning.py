import numpy as np
import pandas as pd

file_path="E:\Smart stock optimization for retail stores\data preprocessing\smart-stock.csv"
data = pd.read_csv(file_path)
print("data :\n")
print(data.head(2))
print(data.isnull().sum())
print(data.describe())
 
data.columns=data.columns.str.strip().str.lower().str.replace(" ","_")

col_to_clean=['sales']

data['sales']=(

    data['sales'].replace([""," ","NA","N/A"],np.nan)

)


data['sales']=pd.to_numeric(data['sales'],errors='coerce')
 
data['sales']=data['sales'].fillna(0).astype(int)
 
print(data.columns)

print(data['sales'].head(5))
 
print(data.count())
 