import pandas as pd
import numpy as np
 
df = pd.read_csv("E:\Smart stock optimization for retail stores\data preprocessing\smart-stock.csv")
print("Mean:\n",df['sales'].mean())