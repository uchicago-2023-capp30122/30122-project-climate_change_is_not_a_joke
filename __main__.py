'''
App Layout

Climate Change Investment Tracker
'''

import dash
from dash import Dash, html
import dash_bootstrap_components as dbc

from final_project.plots.map import map 
from final_project.plots.scatter import scatter
from final_project.plots.bar import bar
from final_project.dashboard import app

# App Layout

app = Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

app.layout = dbc.Container([
    html.Br(),
    dbc.Row(html.H1("Climate Change Investment Tracker", 
                    style = {'text-align':'center'}), 
                    justify = 'center'),

    dbc.Row([dbc.Col(map)]),
    dbc.Row([dbc.Col(scatter)]),
    dbc.Row([dbc.Col(bar)])],

fluid=True, style={'backgroundColor':'white'})

if __name__ == "__main__":
    app.run_server()