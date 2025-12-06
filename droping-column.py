import pandas as pd

df = pd.read_csv("E:\Smart stock optimization for retail stores\data preprocessing\smart-stock.csv")
df = df.drop("Product Name",axis=1)
print(df)
sorted_df = df.sort_values(by= df.columns[2])
print(sorted_df)