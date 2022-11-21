import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pickle

df_sun=pickle.load(open('sun_df.pkl','rb'))
sun=pd.DataFrame(df_sun)

st.title('Sunburst chart')

fig=px.sunburst(sun,
               path=['watch','Brand','Product_name'],
               values='Count',
               title='Top Smart watch brands',
               width=750, height=750)


fig.show()
