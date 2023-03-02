'''
Dashboard Constructor

Climate Change Investment Tracker
'''
from dash import html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

#from final_project.plots.map import project_map 
from final_project.dashboard import app
from final_project.clean_data import hl_wb_to_df as hl

# Construct Dataframes
f = open("final_project/clean_data.csv")
df = pd.read_csv(f)
df["Effective Date"] = pd.to_datetime(df['Effective Date'])
df["Pre/Post Paris Agreement"] = df["Pre/Post Paris Agreement"].map({0: "Pre", 1: "Post"})

df_hl = hl()

# Style Dictionaries
header_style = {'text-align': 'center', 
                'font-family': 'Helvetica',
                "color": "#65463E"}

dropdown_style = {'display': 'inline-block',
                  'text-align': 'center',
                  'font-family': 'Helvetica',
                  'color': '#4c9be8',
                  'width': '60%'}

plot_style = {'display': 'inline-block',
              'width': '100vh',
              'font-family': 'Helvetica', 
              'height': '85vh'}

country_options = [{"label": country, "value": country} for country in df["Country"].unique()]

# Build Figures
map_fig = px.choropleth(df_hl,
                        locations = "Country", 
                        locationmode = "country names",
                        scope = 'asia')

map_fig.update_geos(resolution = 110)
map_fig.update_layout(paper_bgcolor = "#D2E5D0")

scatter_fig = px.scatter(df, 
                         x = "Effective Date", 
                         y = "Commitment Amount",
                         hover_name = "Project Name",
                         hover_data = ["Country", "Project URL"],
                         title = "Commitment Amount Over Time for all Projects in Pan-Asia",
                         labels = {"Commitment Amount": "Commitment Amount"},
                         trendline = "ols")

bar_fig = px.bar(df, 
                 x = "Status", 
                 y = "Commitment Amount",
                 color = "Sector",
                 title = "Commitment Amount per Project Type for all Projects in Pan-Asia",
                 labels = {"Commitment Amount": "Commitment Amount",
                           "Status": "Project Status"})

# App Layout
app.layout = dbc.Container([
    html.Br(),
    dbc.Row(html.H1("Climate Change Investment Tracker"), 
                    style = header_style,
                    justify = 'center'),
    
    html.Br(),

    dbc.Row(html.H3("Filter: Project Breakdown by Country"), 
                    style = header_style,
                    justify ='center'),
    html.Br(),

    dbc.Row(dcc.Dropdown(id = "map_filter",
                         options = ["Project Total", "Projects 11/10-11/16", 
                                    "Projects 11/16-Present", "Climate Change Project Total",
                                    "Climate Change Projects 11/10-11/16",
                                    "Climate Change Projects 11/16-Present",
                                    "Climate Change Project Total Proportion",
                                    "Climate Change Project Proportion 11/10-11/16",
                                    "Climate Change Project Proportion 11/16-Present",
                                    "Climate Change Total Commitment Amount 11/10-11/16",
                                    "Climate Change Total Commitment Amount 11/16-Present"],
                         multi = False,
                         style = dropdown_style),
                         justify = "center"),

    dbc.Row(dcc.Graph(id = 'map',
                      figure = map_fig,
                      style = plot_style),
                      justify = 'center'),
    html.Br(),

    dbc.Row(html.H3("Filter: Country Deep Dive on Climate Change Projects"), 
                    style = header_style,
                    justify = 'center'),
    html.Br(),

    dbc.Row(dcc.Dropdown(id = "country_dd",
                         options = country_options,
                         multi = False,
                         style = dropdown_style),
                         justify = "center"),
    html.Br(),

    dbc.Row(dcc.Graph(id = 'scatter',
                      figure = scatter_fig,
                      style = plot_style),
                      justify = 'center'),
    html.Br(),
    dbc.Row(html.Br()),
    dbc.Row(html.Br()),
    
    dbc.Row([dbc.Col([dbc.Row(html.H5("Category Filter: Project Breakdown"), 
                              style = header_style, 
                              justify = 'center'),

            dbc.Row(dcc.Dropdown(id = "bar_x_filter",
                                 options = ["Status", "Pre/Post Paris Agreement", "Sector"],
                                 multi = False,
                                 style = dropdown_style),
                                 justify = "center")]),

        dbc.Col([dbc.Row(html.H5("Color Filter: Project Breakdown"), 
                         style = header_style, 
                         justify = 'center'),
    
            dbc.Row(dcc.Dropdown(id = "bar_color_filter",
                                 options = ["Status", "Pre/Post Paris Agreement", "Sector"],
                                 multi = False,
                                 style = dropdown_style),
                                 justify = "center")])]),
    html.Br(),

    dbc.Row(dcc.Graph(id = 'bar', 
                      figure = bar_fig,
                      style = plot_style),
                      justify = 'center'),
    html.Br(),
    dbc.Row(html.Br()),
    dbc.Row(html.Br()),

    dbc.Row(html.H3("Data Table: Projects for Selected Country"), 
                    style = header_style,
                    justify = 'center'),
    html.Br(),

    dbc.Row(dash_table.DataTable(id = "data_table",
                                 data = df.to_dict('records'), 
                                 columns = [{"name": "Project Name", "id": "Project Name"},
                                            {"name": "Effective Date", "id": "Effective Date"},
                                            {"name": "Project URL", "id": "Project URL"}],
                                 style_table = {'height': 400},
                                 style_data = {'width': '150px', 
                                               'minWidth': '150px', 
                                               'maxWidth': '150px',
                                               'textOverflow': 'ellipsis'},
                                 style_cell={'textAlign': 'center',
                                             'font-family': 'Helvetica'},
                                 page_current = 0,
                                 page_size = 10)),
    html.Br(),
    dbc.Row(html.Br()),

    dbc.Row("Sources: World Bank Open Data and the Asian Development Bank Data Library")],

fluid = True, style = {'backgroundColor': "#D2E5D0"})

# Update Figures
@app.callback(Output("map", "figure"),
              Input("map_filter", "value"))

def update_map(filter):

    # Filter map title
    title_label = "Project Map"
    if filter == 'Project Total':
        title_label = "Map of Total Projects from November 2010 to Now"
    elif filter == "Projects 11/10-11/16":
        title_label = "Map of Total Projects from November 2010 to November 2016"
    elif filter == "Projects 11/16-Present":
        title_label = "Map of Total Projects from November 2016 to Now"
    elif filter == "Climate Change Project Total":
        title_label = "Map of Total Climate Change Projects from November 2010 to Now"
    elif filter == "Climate Change Projects 11/10-11/16":
        title_label = "Map of Total Climate Change Projects from November 2010 to November 2016"
    elif filter == "Climate Change Projects 11/16-Present":
        title_label = "Map of Total Climate Change Projects from November 2016 to Now"
    elif filter == "Climate Change Project Total Proportion":
        title_label = "Map of Proportion of Climate Change Projects from November 2010 to Now"
    elif filter == "Climate Change Project Proportion 11/10-11/16":
        title_label = "Map of Proportion of Climate Change Projects from November 2010 to November 2016"
    elif filter == "Climate Change Project Proportion 11/16-Present":
        title_label = "Map of Proportion of Climate Change Projects from November 2016 to Now"
    elif filter == "Climate Change Total Commitment Amount 11/10-11/16":
        title_label = "Map of Total Commitment Amount of Climate Change Projects from November 2010 to November 2016"
    elif filter == "Climate Change Total Commitment Amount 11/16-Present":
        title_label = "Map of Total Commitment Amount of Climate Change Projects from November 2010 to Now"

    map_fig = px.choropleth(df_hl,
                            locations = "Country", 
                            locationmode = "country names",
                            color = filter,
                            color_continuous_scale = px.colors.diverging.BrBG,
                            scope = 'asia',
                            title = f"{title_label}")

    map_fig.update_coloraxes(colorbar_orientation="h")
    map_fig.update_geos(center={"lat": 28, "lon": 87})
    map_fig.update_layout(coloraxis_colorbar_y = -0.1,
                          paper_bgcolor = "#D2E5D0")

    return map_fig

@app.callback(Output("scatter", "figure"),
              Input("country_dd", "value"))

def update_scatter(country):

    scatter_data_filter = df[df["Country"] == country]

    fig = px.scatter(scatter_data_filter, 
                     x = "Effective Date",
                     y = "Commitment Amount",
                     hover_name = "Project Name",
                     hover_data = ["Country", "Project URL"],
                     title = f"Commitment Amount Over Time in {country}",
                     labels = {"Commitment Amount": "Commitment Amount"},
                     trendline = "ols")
    
    fig.add_vline(x = "2016-11-01", 
                  line_dash = "dash", 
                  line_color = "darkgreen",
                  annotation_text = "Paris Agreement Ratification", 
                  annotation_position = "top left")
    
    return fig

@app.callback(Output("bar", "figure"),
              Input("country_dd", "value"),
              Input("bar_x_filter", "value"),
              Input("bar_color_filter", "value"))

def update_bar(country, x_filter, color_filter):

    bar_data_filter = df[df["Country"] == country]

    fig = px.bar(bar_data_filter, 
                 x = x_filter, 
                 y = "Commitment Amount",
                 color = color_filter,
                 title = f"Commitment Amount by {x_filter} in {country}",
                 labels = {"Commitment Amount": "Commitment Amount"})
    
    return fig

@app.callback(Output('data_table', 'data'),
              Input("country_dd", "value"))

def update_table(country):

    data_table_filter = df[df["Country"] == country]
    return data_table_filter.to_dict("records")

if __name__ == "__main__":
    app.run_server()