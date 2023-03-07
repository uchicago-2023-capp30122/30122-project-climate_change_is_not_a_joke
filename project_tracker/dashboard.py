"""
Dashboard App Constructor

Author: Robert Surridge
"""

from dash import Dash
import dash_bootstrap_components as dbc

app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])