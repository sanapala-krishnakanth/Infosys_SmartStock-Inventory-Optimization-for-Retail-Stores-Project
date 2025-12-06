import plotly.express as px
import pandas as pd
file_path = r"E:\Smart stock optimization for retail stores\data preprocessing\smart-stock.csv"

df = pd.read_csv(file_path)
print(df)
#line chart
fig = px.line(
    df,
    x="Product ID",
    y="Price",
    title="Plotly Representation of Line Plot"
)
fig.show()

#pie chart
fig = px.pie(df,names="Product ID",values="Price",title="plotly representaion of pie chart")
fig.show()
#dounut
fig = px.pie(df,names="Product ID",values="Price",title="plotly representaion of dounut chart",hole=0.5)
fig.show()
#bar chart
fig = px.bar(
    df,
    x="Product ID",
    y="Price",
    title="Plotly Representation of Bar chart"
)
fig.show()



