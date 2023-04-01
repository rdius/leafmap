#import pandas as pd
import pandas

cars = pandas.read_json("data/car.geojson")

planes = pandas.read_json("data/planes.geojson")

print(cars['type'].count())

print(planes['type'].count())

import streamlit as st
import pandas as pd
import plotly.express as px

# continue loading the data with your excel file, I was a bit too lazy to build an Excel file :)
df = pd.DataFrame(
    [["T1",232, 36], ["T2", 400, 65]],
    columns=[ "Detected Object" , "Cars", "Planes"]
)

fig = px.bar(df, x="Detected Object", y=["Cars", "Planes"], barmode='group', height=400)
# st.dataframe(df) # if need to display dataframe
st.plotly_chart(fig)

def plotgraph(df):
    df = pd.DataFrame(
    [["T1",232, 36], ["T2", 400, 65]],
    columns=[ "Detected Object" , "Cars", "Planes"])
    fig = px.bar(df, x="Detected Object", y=["Cars", "Planes"], barmode='group', height=400)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)
