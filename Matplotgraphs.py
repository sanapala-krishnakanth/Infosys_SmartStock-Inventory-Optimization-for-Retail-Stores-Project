import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(r"E:\Smart stock optimization for retail stores\data preprocessing\smart-stock.csv")
plt.figure(figsize=(10,5))
x = df["Product ID"]
y = df["Price"]
#line plot
plt.plot(x,y,marker='o',linestyle=':',color='g',label='line graph')
plt.title("Products vs Prices")
plt.xlabel("products")
plt.ylabel("prices")
plt.grid()
plt.show()
#bar graph
plt.figure(figsize=(10,5))
plt.bar(x,y,color = 'red',label='Bar graph')
plt.title("ProductID with Prices")
plt.xlabel("products_ID")
plt.ylabel("prices")
plt.grid()
plt.show()
#histogram
plt.figure(figsize=(6,4))
plt.hist(x, bins=5)
plt.title("Graphical Representation of Units Sold")
plt.xlabel("Units Sold Range")
plt.ylabel("Frequency")
plt.show()
#scatter plot
plt.figure(figsize=(6,4))
plt.scatter(x,y,label='scatter plot') 
plt.title('scatter plot example')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc='lower right')
plt.grid()
plt.show()


