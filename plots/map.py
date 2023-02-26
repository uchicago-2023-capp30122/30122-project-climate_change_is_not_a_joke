'''
Map
'''

import dash
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

from final_project.dicts import style_dict

# Layout

map = [
    html.Br(),
    dbc.Row(html.H3("Demo Map: Investment Tracker by Year"),
    style = {'text-align': 'center'}, justify = 'center'),
    html.Br(),

    dbc.Row(dcc.Dropdown(id = "primary_filter",
                        options = [{"label": "Year", "value": "Year"},
                                   {"label": "Commitment Amount", "value": "Commitment Amount"}],
                        multi = False,
                        value = "Year",
                        style = style_dict),
                        justify = "center"),

    dbc.Row(dcc.Dropdown(id = "secondary_filter",
                         style = style_dict),
                         justify = 'center'),

    dbc.Row(dcc.Graph(id = 'demo_map',
                      figure = {'layout': {'paper_bgcolor': "#0f2537", 'plot_bgcolor': "#0f2537"}},
                      style = {'display': 'inline-block', 'width': '80vh', 'height': '80vh'}),
                      justify = 'center')
                ]
