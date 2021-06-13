
# import libraries 

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

# libraries for build dashboard
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

"""### Load Dataset"""

# read dataset
df = pd.read_csv("newegg.csv")
df

df.head()

df.tail()

df.shape

df.brand_name.replace(np.nan, ' ', inplace=True) # replace NaN value by space
brand_name_list = df.brand_name.unique() # get the unique value in the brand name column


# itrate throught the list element with missing brand_name value
for i in df[df['brand_name']== ' '].index:
  item_dec = df.iloc[i]['items_Decribtion'] # get the items_Decribtion

  # return the brand name if the items_Decribtion any of the brands exisitng in the brand list 
  brand = [B for B in brand_name_list if B.lower().split(' ')[0] in (x.lower() for x in item_dec.split() )]

  # if there are more than one matched brand, one of them is the computer brand and another is the components brand (like Intel)
  if len(brand) > 1:
    df['brand_name'][i] = brand[1]
    
  # if there is one brand, then return the first item from the list
  elif len(brand) == 1:
    df['brand_name'][i] = brand[0]

  # if there isn't matched brand return 'N/A'
  else:
    df['brand_name'][i] = 'N/A'

df.brand_name.value_counts()

# Check nulls values
df.isnull().sum()



"""## Describe Data

### Pre processing

### Fill missing value 
- brand_name
- ratings (fill with Zero)
- prices

Filling Missing Value-Prices
"""

# convert prices data type from object to float
df['prices'] = df['prices'].str.replace(',','').astype('float')

# Replacing null values in prices with the avg price
df['prices'] = df['prices'].fillna(df['prices'].mean())
df.prices

# Remove the brackets from ratings,
# Replacing null values in ratings with zero
df['ratings'] = df['ratings'].str.replace('(','').str.replace(')','')
df['ratings'] = df['ratings'].str.replace(',','').astype('float').fillna(0)
df['ratings']

# Replacing null values in brand name with mode (DELL)
#df['brand_name'] = df['brand_name'].fillna(df['brand_name'].mode()[0])
#df['brand_name']

[{"label":x, "value":x} for x in 	df.brand_name.unique()]

# Instatiate the App

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__ ,  external_stylesheets=external_stylesheets)
 

# Create layout that will hold all visuals 
app.layout = html.Div([
    html.H1(
        'Features and price of computer components', 
        style={'color':'#F3F3F3','background-color': '#67001F','text-align':'center','padding':10}
        ),

    ########################### 
    html.Div([
               html.Label([
                "Category", # Label title
                # create Radio Items 
                dcc.RadioItems(
                    id = 'category', # Radio Items id
                    value = "gpu", # default value
                    # display options on one line
                    labelStyle = {'display': 'inline-block' ,'text-align':'center'},
                    # return the unique values from Category column
                    options = [{"label":x, "value":x} for x in 	df.Category.unique()],
                    )
                ],
                style={'fontSize':20,'text-align':'center'}), # change the options size and centred text
              


    ],style={'width': '100%', 'float': 'left', 'display': 'inline-block',
                 'background-color': '#F3F3F3','margin-right':1,'padding':10,
             'text-align':'center'}),

    # 1st plot 
    html.Div([   
              # create a graph
              dcc.Graph(id='graph'), 
                  
          ],
          # add style for the div
          style={'width': '48.5%', 'float': 'left', 'display': 'inline-block',
                 'background-color': '#F3F3F3','padding':10}),


      ###########################
      # 2nd plot 
      html.Div([

              # create a graph
              dcc.Graph(id='graph2'),
              
              
          ],
          # add style for the div
          style={'width': '48.5%', 'float': 'right', 'display': 'inline-block',
                 'background-color': '#F3F3F3','padding':10}),

        ###########################
        # 3rd plot
            html.Div([   
              html.Label([
                "Brand Name", # Label title
                # create Dropdown list
                dcc.Dropdown( 
                    id = 'brand_name2', # Dropdown id
                    clearable = False,
                    value = "DELL", # default value
                    # return the unique values from brand_name column
                    options = [{"label":x, "value":x} for x in 	df.brand_name.unique()] 
                    )
                ],
                style={'fontSize':18}), # change the options size
              
              # create a graph
              dcc.Graph(id='graph3'), 
                  
          ],

          # add style for the div
          style={'width': '48.5%', 'float': 'left', 'display': 'inline-block',
                   'background-color': '#F3F3F3','margin-right':1,'padding':10,'margin-top':1}),

        
        ###########################
        # 4th plot
        html.Div([
              
        html.Label([
                    'Chose brands to compare:',
                    dcc.Dropdown(
                      id='brands',
                      options=[{'label':x, 'value':x} for x in df.sort_values('brand_name')['brand_name'].unique()],
                      value=['DELL'],
                      multi=True,
                      disabled=False,
                      clearable=True,
                      searchable=True,
                      placeholder='Choose Brand...',
                      className='form-dropdown',
                      persistence='string',
                      style={'color': '#67001F'},
                      persistence_type='memory')
                    
                  ],
                style={'fontSize':18}), # change the options size

              dcc.Graph(id='graph4'),
              
              
          ],
          # add style for the div
          style={'width': '48.5%', 'float': 'right', 'display': 'inline-block',
                   'background-color': '#F3F3F3','padding':10,'margin-top':1}),

      ])


###########################
# 1st plot
@app.callback(
    Output('graph','figure'),
    Input('category','value')
)
 
def update_figures(category):
  # filter data by category
  test = df[df['Category']== category]
  

  # create scatter plot for prices and ratings
  fig =  px.scatter(
          test, 
          x = 'prices', 
          y = 'ratings' ,
          color = 'brand_name',
          color_discrete_sequence=px.colors.sequential.RdBu,
          labels = {"ratings": "Rating", "prices":"Price"},
          title = "Relation between the price and rating based on category"
          )
  

  # transparent background
  fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)', # change plot background color
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',  # change paper background color

    'title_font_color': '#67001F', # change the plot title color
    })
  
  # return plot
  return fig

###########################
# 2nd plot
@app.callback(
    Output('graph2','figure'),
    Input('category','value')
)

def update_figures(category):
  # filter data by category
  test = df[df['Category'] == category]

  # create a bar plot - counts the products bsed on the category 
  fig =  px.bar(
            test,
            x = test.brand_name.value_counts().index,
            y = test.brand_name.value_counts().values,
            color_discrete_sequence=px.colors.sequential.RdBu,
            labels = {"y": "Count of products", "x":"Brand Name"},
            title = "Count of the products based on the category"
    
  )

  # transparent background
  fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)',  # change plot background color
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',  # change paper background color

    'title_font_color': '#67001F', # change the plot title color
    })
  
  # return plot
  return fig

###########################
# 3rd plot

@app.callback(
    Output('graph3','figure'),
    Input('brand_name2','value')
)
 
def update_figures(brand_name):
  # filter data by brand_name
  test = df[df['brand_name']== brand_name]
  

  # create scatter plot for prices and ratings
  fig = px.pie(test, test['Category'],color_discrete_sequence=px.colors.sequential.RdBu)
  fig.update_layout(title_text='Categories for computer brands')
  
  # transparent background
  fig.update_layout({
    'plot_bgcolor': 'rgba(0, 0, 0, 0)', # change plot background color
    'paper_bgcolor': 'rgba(0, 0, 0, 0)',  # change paper background color

   'title_font_color': '#67001F', # change the plot title color
    })
  
  # return plot
  return fig

###########################
# 4th plot

@app.callback(
    Output('graph4','figure'),
    Input('brands','value')
)


def build_graph(brands):
    df1 = df[df['brand_name'].isin(brands)]
           
    df1 = df1.groupby('brand_name')['prices'].agg('mean') 

    fig = px.bar(df1,
                x = df1.index,
                y = df1.values,
                color = df1.index,
                color_discrete_sequence=px.colors.sequential.RdBu)
    
    fig.update_layout(yaxis={'title':'Computer brand price'},
                      xaxis={'title':'Brand Names'},
                      title={'text':'Price comparison of brands'})
    
    
  # transparent background
    fig.update_layout({
      'plot_bgcolor': 'rgba(0, 0, 0, 0)', # change plot background color
      'paper_bgcolor': 'rgba(0, 0, 0, 0)',  # change paper background color

      'title_font_color': '#67001F', # change the plot title color
      })
  
    return fig



# Run the App Server
if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
    
###### Team Members: ######
#-Zarah Shibli
#-Lama Alzahrani
#-Wajd Alturki

