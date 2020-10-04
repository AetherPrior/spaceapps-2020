
#!pip install pydeck streamlit import_ipynb

#%cd '/content/drive/My Drive/Spaceapps-2020/Model'
import pydeck as pdk
import streamlit as st
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
#from config import MAPBOX_API_KEY
st.title('SpaceApps 2020 | Team Spacia')
modis_data = "LatLongLoad.csv"
df = pd.read_csv('LatLongLoad.csv')
df2 = df[df['Fire']>20]
print(df2.tail())
fig = go.Figure(data=px.scatter_geo(
        data_frame=df2,
        projection='orthographic',
        lon = df2['Long'],
        lat = df2['Lat'],
        #mode = 'markers',
        #marker_color = df2['Fire'],
        #connectgaps=True,
        color=df2['Fire']
        ))
#'''
#        marker = dict(
#            size = 2,
#            opacity = 0.8,
#            reversescale = True,
#            autocolorscale = True,
#            symbol = 'circle-dot',
#            colorscale = 'Blues',
#            cmin = 0,
#            color = df['Fire'],
#            cmax = df['Fire'].max(),
#            colorbar_title="Confidence of fire"
#        )
#'''

st.write(fig)
st.dataframe(data=df)


