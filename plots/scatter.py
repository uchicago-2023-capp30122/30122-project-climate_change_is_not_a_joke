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

# Layout

scatter = [
    dbc.Row(html.Br()),
    dbc.Row(html.H3("Demo Scatterplot"), style = {'text-align': 'center'}, 
                                         justify = 'center'),
    dbc.Row(html.Br()),

    dbc.Row([
        dbc.Col([
            dbc.Row(html.H5("Select an X Variable"), style = {'text-align': 'center'},
                                                     justify = 'center'),

            dbc.Row(dcc.Dropdown(id = "primary_scatter",
                                 options = [{"label": "Year", 
                                             "value": "Year"},
                                            {"label": "Country", 
                                             "value": "Country"}],
                                 multi = False,
                                 value = " ",
                                 style = style_dict),
                                 justify = 'center'),

        dbc.Row(dcc.Dropdown(id = "secondary_scatter",
                             style = style_dict),
                             justify = 'center')]),

        dbc.Col([
            dbc.Row(html.H5("Select a Y Variable"), style = {'text-align': 'center'}, 
                                                    justify = 'center'),
            
            dbc.Row(dcc.Dropdown(id = "scatter_y",
                                 options = [{'label': "Commitment Amount", 
                                             'value': "Commitment Amount"}],
                                 multi = False,
                                 value = "Commitment Amount",
                                 style = style_dict),
                                 justify = 'center')]),
    ]),
    
    dbc.Row(dcc.Graph(id = 'scatter',
                      figure = {'layout': {'paper_bgcolor': "#0f2537", 
                                           'plot_bgcolor': "#0f2537"}},
                      style = {'display': 'inline-block', 
                               'width': '100vh', 
                               'height': '80vh'}),
                      justify = 'center'),
    
    dbc.Row(html.Br())]

@app.callback(
    Output("tab-content", "children"),
    [Input("tabs", "active_tab"), Input("store", "data")],
)
def render_tab_content(active_tab, data):
    """
    This callback takes the 'active_tab' property as input, as well as the
    stored graphs, and renders the tab content depending on what the value of
    'active_tab' is.
    """
    if active_tab and data is not None:
        if active_tab == "scatter":
            return dcc.Graph(figure=data["scatter"])