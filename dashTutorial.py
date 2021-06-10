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


# Build App

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([

        html.Div([
             dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        id='year--slider',
        min=df['Year'].min(),
        max=df['Year'].max(),
        value=df['Year'].max(),
        marks={str(year): str(year) for year in df['Year'].unique()}
    )
])
        
        # Callbacks
@app.callback(
     dash.dependencies.Input('year--slider', 'value')])
        dff = df[df['Year'] == year_value]
        
        
        ######### I have Errors ! ##### :
        # Want Ask About it ...
       
        ## Dash is running on http://127.0.0.1:8050/
        #Dash is running on http://127.0.0.1:8050/
        # * Serving Flask app "__main__" (lazy loading)
