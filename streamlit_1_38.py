# Data process
import numpy as np
import datetime as dt
import pandas as pd
import polars as pl
import pyarrow as pa
import geopandas as gpd
from shapely.geometry import Point

# Data viz
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import graphviz
import pydeck as pdk

import os

path_wd = os.getcwd().replace('\\python', '')
path_cda = '\\CuriosityDataAnalytics'
path_data = path_wd + '\\data'

# App config
#----------------------------------------------------------------------------------------------------------------------------------#
# Page config
st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("What's new in Streamlit 1.38?")
st.divider()

with st.sidebar:
    st.image(path_cda + 'logo.png')

#
#


# 1)
#---------------------------------------------------------------------------------------#
st.header(':one: st.dataframe now supports objects from popular libraries like Dask, Modin, Numpy, pandas, Polars, PyArrow, Snowpark, Xarray, and more.')

cols = st.columns(2)
cols[0].subheader('Streamlit 1.37')
cols[1].subheader('Streamlit 1.38')


cols[0].code('''
import pandas as pd
st.dataframe(pd.DataFrame({'pandas' : [1,2,3]}))
''')
cols[0].dataframe(pd.DataFrame({'pandas' : [1,2,3]}))

cols[1].code('''
import pandas as pd
import geopandas as pd
from shapely.geometry import Point
import polars as pl
              
st.dataframe(pd.DataFrame({'pandas' : ['a','b','c']}))
st.dataframe(pl.DataFrame({'polars' : ['a','b','c']}))
st.dataframe(dd.dataframe(gpd.GeoDataFrame({'geopandas': ['a','b','c']},
                                            geometry=[Point(-110.3656, 48.4284),
                                                      Point(-123.3656, 48.4284),
                                                      Point(-150.3656, 48.4284)]))
''')

subcols = cols[1].columns((0.35,0.5,0.2))

subcols[0].dataframe(pd.DataFrame({'pandas' : ['a','b','c']}))
subcols[1].dataframe(gpd.GeoDataFrame({'geopandas': ['a','b','c']}, geometry=[Point(-110.3656, 48.4284), Point(-123.3656, 48.4284), Point(-150.3656, 48.4284)]))
subcols[2].dataframe(pl.DataFrame({'polars' : ['a','b','c']}))

st.divider()

# 2) 
#---------------------------------------------------------------------------------------#
st.header(':two: You can control the initial expansion state of st.json elements')


cols = st.columns(2)
cols[0].subheader('Streamlit 1.37')
cols[1].subheader('Streamlit 1.38')

cols[0].code('''
data = {
    "name": "John",
    "email": "john.doe@gmail.com",
    "profile" : {
        "age" : 30,
        "height" : 178,
        "weight" : 195
    }
}
''')

data = {
    "name": "John",
    "email": "john.doe@gmail.com",
    "profile" : {
        "age" : 30,
        "height" : 178,
        "weight" : 195
    }
}

subcols = cols[0].columns(2)
subcols[0].code('''
st.json(data, expanded=True)
''')
subcols[0].json(data, expanded=True)

subcols[1].code('''
st.json(data, expanded=False)
''')
subcols[1].json(data, expanded=False)


cols[1].code('''
data = {
    "name": "John",
    "email": "john.doe@gmail.com",
    "profile" : {
        "age" : 30,
        "height" : 178,
        "weight" : 195
    }
}
''')
cols[1].code('''
st.json(data, expanded=1)
''')
cols[1].json(data, expanded=1)


st.divider()

# 3) 
#---------------------------------------------------------------------------------------#
st.header(':three: You can choose to wrap lines in st.code')

cols = st.columns(2)
cols[0].subheader('Streamlit 1.37')
cols[1].subheader('Streamlit 1.38')

cols[0].code('''
st.code("
df = pd.DataFrame({'a' : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]})
")
''')

cols[1].code('''
st.code("
df = pd.DataFrame({'a' : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]})
",
wrap_lines=True)
''', wrap_lines=True)