import seaborn as sns
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import plotly.express as px
import plotly.figure_factory as ff
import pickle

df_sun=pickle.load(open('sun_df.pkl','rb'))
sun=pd.DataFrame(df_sun)

df=pickle.load(open('datahut_df.pkl','rb'))
df=pd.DataFrame(df)

st.title('Sunburst chart')


fig = px.sunburst(sun,
             path=['watch','Brand','Product_name'],
             values='Count',
             title='Top Smart watch brands',
             width=700, height=700)
# fig.show()
st.plotly_chart(fig)
