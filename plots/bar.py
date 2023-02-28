'''
Bar Graph
'''

from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from final_project.dicts import style_dict

def build_bar(df, country):

    bar_data_filter = df[df["Country / Economy"] == country]

    # Filter data for bar graph
    dropdown = ["Country / Economy", 
                "Project Status",
                "Project Type / Modality of Assistance", 
                "Sector / Subsector",
                "Strategic Agendas"]
    

    # Build the first bar graph
    fig2 = px.bar(bar_data_filter, 
                 x = "Project Status", 
                 y = "Amount",
                 color = "Project Type / Modality of Assistance",
                 title = f"Commitment Amount per Project Type in {country}",
                 labels = {"Amount": "Commitment Amount"})
    dcc.Graph(figure=fig2)
    fig2.show()

# Layout    
bar = [
    dbc.Row(html.Br()),
    dbc.Row(html.H3("Bar Graph 1"), style = {'text-align': 'center'},
                                         justify = 'center'),
    dbc.Row(html.Br()),

    # Bar Graph 1
    dbc.Row(dcc.Dropdown(id = "bar_graph",
                         options = [{'label': "Country", 'value': "Commitment Amount"}],
                         multi = False,
                         value = "Commitment Amount",
                         style = style_dict),
                        justify = 'center'),

    dbc.Col([
        dbc.Row(dcc.Graph(id = 'bar_graph', figure = {},
                          style = {'display': 'inline-block',
                                   'width': '80vh', 'height': '60vh'}),
                          justify = 'center')]),

    # Bar Graph 2
    dbc.Col([
        dbc.Row(html.H3("Bar Graph 2"), style = {'text-align': 'center'},
                                             justify = 'center'),
        dbc.Row(html.Br()),

        dbc.Row(dcc.Dropdown(id = "bar2_graph",
                        options = [{'label': "Year",
                                    'value': "Commitment Amount"}],
                        multi = False,
                        value = 'Commitment Amount',
                        style = style_dict),
                        justify = 'center'),

        dbc.Row(dcc.Graph(id = 'bar2_graph', figure = {},
                          style = {'display': 'inline-block',
                                   'width': '80vh', 'height': '60vh'}),
                          justify = 'center')])
]