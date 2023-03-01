'''
Scatterplot
'''
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import statsmodels

from final_project.dicts import style_dict
from final_project.dashboard import app

def build_scatter(df, country):

    scatter_data_filter = df[df["Country / Economy"] == country]

    fig = px.scatter(scatter_data_filter, 
                     x = "commitment_date", 
                     y = "Amount",
                     hover_name = "Project Name",
                     hover_data = ["Country / Economy", "project_url"],
                     title = f"Commitment Amount Over Time in {country}",
                     labels = {"Amount": "Commitment Amount"},
                     trendline = "ols")
    dcc.Graph(figure=fig)
    fig.show()