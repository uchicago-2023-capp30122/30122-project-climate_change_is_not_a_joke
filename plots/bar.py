'''
Demo Bar Graph
'''

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from final_project.dicts import style_dict

# Layout

bar = [
    dbc.Row(html.Br()),
    dbc.Row(html.H3("Demo Bar Graph 1"), style = {'text-align': 'center'},
                                         justify = 'center'),
    dbc.Row(html.Br()),

    # Demo Bar Graph 1
    dbc.Row(dcc.Dropdown(id = "bar_cca",
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

    # Demo Bar Graph 2
    dbc.Col([
        dbc.Row(html.H3("Demo Bar Graph 2"), style = {'text-align': 'center'},
                                             justify = 'center'),
        dbc.Row(html.Br()),

        dbc.Row(dcc.Dropdown(id = "bar2_311",
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