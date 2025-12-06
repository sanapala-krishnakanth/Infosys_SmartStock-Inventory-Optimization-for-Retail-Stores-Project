import pandas as pd
df = pd.read_csv("E:\Smart stock optimization for retail stores\data preprocessing\smart-stock.csv")
print( df)

print(df.sort_values(by=df.columns[0]))

print( "sorting values in decending order:\n",df.sort_values(by='sales', ascending=False))

print("Quanty of having more than 30:\n" ,df[df['Quantity in Stock'] < 30])

print( df[(df['Price'] >= 100) & (df['Price'] <= 1000)])

