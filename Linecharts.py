import pandas as pd
import plotly.express as px
df=pd.read_csv("C:/Users/Hp/Desktop/White HAt Junior/PYTHON/C103/line_chart.csv")
fig=px.line(df,x="Year",y="Per capita income", color="Country",title=" Country Income")
fig.show()