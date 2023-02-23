'''
App Layout

Climate Change Investment Tracker
'''

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

from test_project.plots.demo_map import demo_map
from test_project.plots.demo_scatter import demo_scatter
from test_project.plots.demo_bar import demo_bar

# App Layout

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([
    html.Br(),
    dbc.Row(html.H1("Climate Change Investment Tracker", 
                    style = {'text-align':'center'}), 
                    justify = 'center'),

    dbc.Row([dbc.Col(demo_map)]),
    dbc.Row([dbc.Col(demo_scatter)]),
    dbc.Row([dbc.Col(demo_bar)])],

fluid=True, style={'backgroundColor':'white'})

if __name__ == "__main__":
    app.run_server()