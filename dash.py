%%capture
!pip install jupyter-dash

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 

import plotly.express as px
from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# Load data 
df = pd.read_csv("../input/Bollywood_movies.csv")

# get informaction about data
df.info()

df.shape

df.head()


# 3D scatter :
# create trace 1 3d scatter
trace1 = go.Scatter3d(
    x=dataframe.imdb_id,
    y=dataframe.release_date,
    z=dataframe.year_of_release,
    title = "Plotly Scatter 3d"
        size=10,
)


# Box Plots:
  # create trace 1 Box Plots
  trace1 = go.Box(
    y=x2015.year_of_release,
    name = 'year_of_release',
    marker = dict(
    )
