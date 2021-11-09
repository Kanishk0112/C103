import pandas as pd
import plotly.express as px
df=pd.read_csv("C:/Users/Hp/Desktop/White HAt Junior/PYTHON/C103/data.csv")
fig=px.scatter(df,x="Population",y="Per capita",size="Percentage", color="Country")
fig.show()