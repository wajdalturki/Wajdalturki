pip install dash

pip install jupyter-dash

pip install pandas

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Create data frame:

df = pd.DataFrame({
    "Cars": ["Ford", "BMW", "Kia", "GMC", "Mazda", "Toyota"],
    "Model": ["Explorer", "740", "Opirus", "Envoy", "3", "Avalon"],
    "Year": [2007, 2013, 2011, 2008, 2013, 2014]
})
df

# Create bar plot

fig = px.bar(df, x="Cars", y="Year", color="Year", barmode="group")
fig


# Building Dash

app.layout = html.Div(children=[
    html.H1(children='Cars Models'),

    html.Div(children='''Cars Models in  Saudi Arabia.'''),

dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
if __name__ == '__main__':
    app.run_server(debug=True)


