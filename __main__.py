'''
Dashboard Constructor

Climate Change Investment Tracker
'''
from dash import html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

from final_project.dashboard import app
from final_project.stats import rda_logreg, rda_linearreg, hist_data

# Construct Dataframes
ll_adb = open("final_project/ll_adb.csv")
ll_wb = open("final_project/ll_wb.csv")
adb_df = pd.read_csv(ll_adb)
wb_df = pd.read_csv(ll_wb)

ll_wb_2 = open("final_project/ll_wb.csv")
wb_df_2 = pd.read_csv(ll_wb_2)

adb_df = adb_df.loc[:, ['Country', 'Region', 'Project Name', 'Project Description', 
                    'Status', 'Project URL', 'Effective Date', 'Commitment Amount',
                    'Pre/Post Paris Agreement']]
wb_df = wb_df.loc[:, ['Country', 'Region', 'Project Name', 'Project Description', 
                    'Status', 'Project URL', 'Effective Date', 'Commitment Amount',
                    'Pre/Post Paris Agreement']]
df_lst = [adb_df, wb_df]
df = pd.concat(df_lst)
df = df.sort_values(by = ['Country'])

df["Effective Date"] = pd.to_datetime(df['Effective Date'])
df["Pre/Post Paris Agreement"] = df["Pre/Post Paris Agreement"].map({0: "Pre", 1: "Post"})

hl_f = open("final_project/hl_data.csv")
hl_df = pd.read_csv(hl_f)

# Style Dictionaries
header_style = {"text-align": "center",
                'font-family': 'Helvetica',
                "color": "#65463E"}

small_dropdown_style = {"display": "inline-block",
                  "text-align": "center",
                  'font-family': 'Helvetica',
                  'color': "#65463E",
                  'width': '60%'}

big_dropdown_style = {"display": "inline-block",
                  "text-align": "center",
                  'font-family': 'Helvetica',
                  'color': "#65463E",
                  'width': '85%'}

plot_style = {'width': "100%"}

country_options = [{"label": country, "value": country} for country in df["Country"].unique()]

# Build Figures
logreg_fig = rda_logreg()
linreg_fig = rda_linearreg()
hist_fig = hist_data()

map_fig = px.choropleth(hl_df,
                        locations = "Country", 
                        locationmode = "country names",
                        scope = 'asia')

map_fig.update_geos(resolution = 110)
map_fig.update_layout(paper_bgcolor = "#D2E5D0")

scatter_fig = px.scatter(df, 
                         x = "Effective Date", 
                         y = "Commitment Amount",
                         title = "Project Investment over Time",
                         labels = {"Commitment Amount": "Commitment Amount"},
                         trendline = "ols")

scatter_fig.update_layout(yaxis_range = [0,100])

bar_fig = px.bar(df, 
                 x = "Status", 
                 y = "Commitment Amount",
                 #color = "Sector",
                 title = "Project Breakdown",
                 labels = {"Commitment Amount": "Commitment Amount",
                           "Status": "Project Status"})

# App Layout
app.layout = dbc.Container([
    html.Br(),
    dbc.Row(html.H1("Climate Change Investment Tracker"), 
                    style = header_style,
                    justify = 'center'),
    
    html.Br(),
    html.Div(children=[dbc.Row([dbc.Col([

                    html.Br(),
                    html.Br(),
                    html.Br(),
                    
                    dbc.Card([
                                
                    html.H5("Filter: Pre/Post Paris Agreement"),
                    dcc.Dropdown(id = "primary_map_filter",
                                  style = big_dropdown_style,
                                  options = [{"label": "Pre-Paris Agreement", 
                                              "value": "(Pre-Paris Agreement)"}, 
                                             {"label": "Post-Paris Agreement", 
                                              "value": "(Post-Paris Agreement)"}]),
                    
                    html.H5("Filter: Funding Source"), 
                    dcc.Dropdown(id = "secondary_map_filter",
                                 style = big_dropdown_style,
                                 options = [{"label": "Source: Asian Development Bank",
                                              "value": "ADB"}, 
                                            {"label": "Source: World Bank",
                                             "value": "World Bank"}]),
                    
                    html.H5("Dropdown: Project Breakdown by Country"), 
                    dcc.Dropdown(id = "map_dd",
                                 style = big_dropdown_style,
                                 options = ["Project Count", 
                                            "Climate Change Project Count",
                                            "Climate Change Project Count Proportion",
                                            "Cumulative Project Funding",
                                            "Climate Change Project Funding",
                                            "Climate Change Project Funding Proportion"])],
                                style = {"text-align": "center",
                                         'width': "75%",

                                         "padding": "2rem 1rem"},
                                         color = "#D2E5D0")]),

                    dbc.Col([(dcc.Graph(id = 'map',
                                       figure = map_fig,
                                       style = plot_style))])])]),

    html.Br(),

    dbc.Row(html.H3("High Level Regressions"), 
                    style = header_style,
                    justify ='center'),
    html.Br(),

    html.Div(children = 
             [html.Div(dcc.Graph(id = 'logreg_fig', 
                                 figure = logreg_fig,
                                 style = plot_style), 
                                 style = {'display': 'inline-block'}),
            
              html.Div(dcc.Graph(id = 'linreg_fig',
                                 figure = linreg_fig,
                                 style = plot_style), 
                                 style = {'display': 'inline-block'})],
                                 style = {'width': '100%', 
                                          'display': 'inline-block'}),  
    dbc.Row(html.Br()),
    html.Br(),

    dbc.Row(html.H3("High Level Histogram"), 
                    style = header_style,
                    justify ='center'),
    html.Br(),
    
    dbc.Row(dcc.Graph(id = 'hist_fig',
                      figure = hist_fig,
                      style = plot_style),
                      justify = "center"),

    dbc.Row(html.Br()),
    html.Br(),
    
    dbc.Row(html.H2("Climate Change Project Deep Dive by Country"), 
                    style = header_style,
                    justify = 'center'),
    html.Br(),

    dbc.Row(html.H4("Filter: Select a Country!"), 
                    style = header_style,
                    justify = 'center'),

    dbc.Row(dcc.Dropdown(id = "country_dd",
                         options = country_options,
                         multi = False,
                         style = small_dropdown_style),
                         justify = "center"),
    html.Br(),

    dbc.Row(html.H4("Filter: Select a Second Country to Compare!"), 
                    style = header_style,
                    justify = 'center'),
    
    dbc.Row(dcc.Dropdown(id = "second_country_dd",
                         options = country_options,
                         multi = False,
                         style = small_dropdown_style),
                         justify = "center"),
    html.Br(),
    
    dbc.Row(html.H3("Data Table: Comparison of Country GDP and Climate Vulnerability"), 
                    style = header_style,
                    justify = 'center'),
    
    dbc.Row(dash_table.DataTable(id = "hl_data_table",
                                 data = hl_df.to_dict('records'),
                                 columns=[{'name': i, 'id': i} for i in hl_df.loc[:,['Country','2020 GDP Per Capita', '2020 Gain Index']]],
                                 page_current = 0,
                                 page_size = 5,
                                 style_data = {'width': '150px', 
                                               'minWidth': '150px', 
                                               'maxWidth': '150px',
                                               'textOverflow': 'ellipsis'},
                                 style_cell={'textAlign': 'center',
                                             'font-family': 'Helvetica'})),
    html.Br(),

    dbc.Row("The ND-GAIN Country Index summarizes a country's vulnerability to \
            climate change and other global challenges in combination with its \
            readiness to improve resilience. It aims to help governments, businesses \
            and communities better prioritize investments for a more efficient response \
            to the immediate global challenges ahead."),
    html.Br(),

    dbc.Row("World wide ranking by ND-GAIN Index, higher scores are better"),

    html.Br(),
    html.Br(),

    html.Div(html.Br()),
    html.Div(html.H5("Category Filter: Project Breakdown"), 
                      style = {'width': '100%', 
                               'display': 'inline-block'}),
    
    html.Div(dcc.Dropdown(id = "bar_x_filter",
                          options = ["Status", "Pre/Post Paris Agreement"],
                          multi = False),
                          style = {'width': '40%', 'display': 'inline-block'}),
    html.Div(html.Br()),
    html.Div(html.H5("Color Filter: Project Breakdown"), 
                              style = {'width': '100%', 'display': 'inline-block'}),
    
    html.Div(dcc.Dropdown(id = "bar_color_filter",
                            options = ["Status", "Pre/Post Paris Agreement"],
                            multi = False),
                            style = {'width': '40%', 'display': 'inline-block'}),
    html.Br(),
    html.Br(),

    html.Div(children = 
             [html.Div(dcc.Graph(id = 'bar', 
                                 figure = bar_fig,
                                 style = plot_style), 
                                 style = {'display': 'inline-block'}),
            
              html.Div(dcc.Graph(id = 'll_scatter',
                                 figure = scatter_fig,
                                 style = plot_style), 
                                 style = {'display': 'inline-block'})],
                                 style = {'width': '100%', 
                                          'display': 'inline-block'}),  
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(html.H3("Data Table: Projects for Selected Country"), 
                    style = header_style,
                    justify = 'center'),
    html.Br(),

    dbc.Row(dash_table.DataTable(id = "ll_data_table",
                                 data = df.to_dict('records'), 
                                 columns = [{"name": "Project Name", "id": "Project Name"},
                                            {"name": "Status", "id": "Status"},
                                            {"name": "Effective Date", "id": "Effective Date"},
                                            {"name": "Project URL", "id": "Project URL"}],
                                 page_current = 0,
                                 page_size = 10,
                                 css = [{'selector': 'table', 'rule': 'table-layout: fixed'}],
                                 style_cell = {"text-align": "left",
                                               'width': '{}%'.format(len(df.columns)),
                                               'textOverflow': 'ellipsis',
                                               'overflow': 'hidden'})),
    html.Br(),
    html.Br(),

    dbc.Row("Sources: World Bank Open Data and the Asian Development Bank Data Library"),

    html.Br()],

fluid = True, style = {'backgroundColor': "#D2E5D0"})

# Update Figures
@app.callback(Output("map", "figure"),
              [Input("primary_map_filter", "value"),
               Input("secondary_map_filter", "value"),
               Input("map_dd", "value")])

def update_map(primary_filter, secondary_filter, dd):

    if primary_filter == "(Pre-Paris Agreement)":
        new_df = hl_df.filter(regex = "Pre|Source|Country")
        if dd is None:
            color_filter = "Project Count (Pre-Paris Agreement)"
        else: 
            color_filter = dd + " " + primary_filter
        if secondary_filter == "ADB":
            new_df = new_df[new_df['Funding Source'] == secondary_filter]
        elif secondary_filter == "World Bank":
            new_df = new_df[new_df['Funding Source'] == secondary_filter]
        else:
            new_df = new_df[new_df['Funding Source'] == "Total"]

    elif primary_filter == "(Post-Paris Agreement)":
        new_df = hl_df.filter(regex = "Post|Source|Country")
        if dd is None:
            color_filter = "Project Count (Post-Paris Agreement)"
        else: 
            color_filter = dd + " " + primary_filter
        if secondary_filter == "ADB":
            new_df = new_df[new_df['Funding Source'] == secondary_filter]
        elif secondary_filter == "World Bank":
            new_df = new_df[new_df['Funding Source'] == secondary_filter]
        else:
            new_df = new_df[new_df['Funding Source'] == "Total"]
    
    else:
        new_df = hl_df.filter(regex = "(Total)|Source|Country")
        if dd is None:
            color_filter = "Project Count (Total)"
        else: 
            color_filter = dd + " " + "(Total)"
        if secondary_filter == "ADB":
            new_df = new_df[new_df['Funding Source'] == secondary_filter]
        elif secondary_filter == "World Bank":
            new_df = new_df[new_df['Funding Source'] == secondary_filter]
        else:
            new_df = new_df[new_df['Funding Source'] == "Total"]

    # Filter map title
    title_label = "Map of Total Climate Change Projects from November 2010 to Now"
    if dd == 'Project Count':
        title_label = "Map of Total Projects from November 2010 to Now"
    elif dd == "Climate Change Project Count":
        title_label = "Map of Total Climate Change Projects from November 2010 to Now"
    elif dd == "Climate Change Project Proportion":
        title_label = "Map of Proportion of Climate Change Projects from November 2010 to Now"
    elif dd == "Cumulative Project Funding":
        title_label = "Map of Cumulative Funding for All Projects from November 2010 to Now"
    elif dd == "Climate Change Project Funding":
        title_label = "Map of Climate Change Project Funding from November 2010 to Now"
    elif dd == "Climate Change Project Funding Proportion":
        title_label = "Map of Proportional Funding of Climate Change Projects from November 2010 to Now"

    map_fig = px.choropleth(new_df,
                            locations = "Country", 
                            locationmode = "country names",
                            color = color_filter,
                            color_continuous_scale = px.colors.diverging.BrBG,
                            scope = 'asia',
                            title = f"{title_label}")

    map_fig.update_coloraxes(colorbar_orientation = "h", colorbar_len = .7)
    map_fig.update_geos(center = {"lat": 28, "lon": 87})
    map_fig.update_layout(coloraxis_colorbar_y = -0.2,
                          paper_bgcolor = "#D2E5D0",
                          title_x = 0.5)
    map_fig.update_layout(margin= {"l":20,"r":12,"t":40, "b":40, "pad": 10})

    return map_fig

@app.callback(Output('hl_data_table', 'data'),
              [Input("country_dd", "value"),
               Input("second_country_dd", "value")])

def update_table(country_dd, secondary_country_dd):
    
    if country_dd is None:
        final_filter = hl_df[hl_df["Funding Source"] == "Total"]
        return final_filter.to_dict("records")
    
    elif country_dd is not None:
        if secondary_country_dd is not None:
            data_table_filter = hl_df[(hl_df["Country"] == country_dd) | (hl_df["Country"] == secondary_country_dd)]
        else:
            data_table_filter = hl_df[hl_df["Country"] == country_dd]
        final_filter = data_table_filter[data_table_filter["Funding Source"] == "Total"]
        return final_filter.to_dict("records")

@app.callback(Output("ll_scatter", "figure"),
              Input("country_dd", "value"))

def update_scatter(country):

    scatter_df = wb_df_2[wb_df_2["Country"] == country]
    scatter_df['Project Count by Year'] = scatter_df.groupby(['Year'])['Project Name'].transform('count')
    scatter_df["Project Commitment Amount by Year"] = scatter_df.groupby(["Year"])["Commitment Amount"].transform(sum)

    fig = px.scatter(scatter_df, 
                     x = "Year",
                     y = "Project Count by Year",
                     size = "Project Commitment Amount by Year",
                     title = f"Project Over Time in {country}",
                     labels = {"Project Count": "Project Count"},
                     trendline = "ols")
    
    fig.add_vline(x = 2016, 
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

@app.callback(Output('ll_data_table', 'data'),
              Input("country_dd", "value"))

def update_table(country):

    data_table_filter = df[df["Country"] == country]
    return data_table_filter.to_dict("records")

if __name__ == "__main__":
    app.run_server(debug = True, host = '0.0.0.0', port = 8071)