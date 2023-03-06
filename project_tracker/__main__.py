'''
Dashboard Constructor

Climate Change Investment Tracker
'''

from dash import html, dcc, Input, Output, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px

from project_tracker.dashboard import app
from project_tracker.inputs import header_style, small_dropdown_style, \
                                big_dropdown_style, plot_style, bottom_table_cols, \
                                paris_filter, source_filter, map_dd_options, \
                                map_dd_style, hl_reg_style, hl_reg_layout_style, \
                                country_options, hl_data_table_options, hl_data_table_text, \
                                hl_data_table_cell,  bar_filter, bar_options, ll_data_table_cell
from project_tracker.load_and_clean.load_data import hl_df, ll_df
from project_tracker.graphs.starting_graphs import logreg_fig, linreg_fig, hist_fig, \
                                          map_fig, scatter_fig, bar_fig

# App Layout
app.layout = dbc.Container([
    html.Br(),
    dbc.Row(html.H1("Climate Change Investment Tracker"), 
                    style = header_style,
                    justify = 'center'),
    html.Br(),

    dbc.Row(html.H3("Interactive Map: Tracking the Impact of the Paris Agreement on Climate Change Investment"), 
                    style = header_style,
                    justify = "center"),

    html.Br(),

    html.Br(),

    html.Div(children = [dbc.Row([dbc.Col([
                    
                    dbc.Card([                    
                    html.H5("Filter: Pre/Post Paris Agreement"),
                    dcc.Dropdown(id = "primary_map_filter",
                                 style = big_dropdown_style,
                                 options = paris_filter),
                    
                    html.H5("Filter: Funding Source"), 
                    dcc.Dropdown(id = "secondary_map_filter",
                                 style = big_dropdown_style,
                                 options = source_filter),
                    
                    html.H5("Dropdown: Project Breakdown by Country"), 
                    dcc.Dropdown(id = "map_dd",
                                 style = big_dropdown_style,
                                 options = map_dd_options)],
                                 style = map_dd_style,
                                 color = "#D2E5D0")]),

                    dbc.Col([(dcc.Graph(id = 'map',
                                        figure = map_fig,
                                        style = plot_style))])])]),
    html.Br(),

    dbc.Row(html.H3("Static Regressions: Examining the Effect of the Paris Agreement \
                    on Climate Change Project Investment"), 
                    style = header_style,
                    justify = "center"),
    html.Br(),

    html.Div(children = 
             [html.Div(dcc.Graph(id = 'logreg_fig', 
                                 figure = logreg_fig,
                                 style = plot_style), 
                                 style = hl_reg_style),
            
              html.Div(dcc.Graph(id = "linreg_fig",
                                 figure = linreg_fig,
                                 style = plot_style), 
                                 style = hl_reg_style)],
                                 style = hl_reg_layout_style),  
    dbc.Row(html.Br()),
    html.Br(),

    dbc.Row(html.H3("Static Histogram: Examining the Distribution of Climate Change \
                     Project Funding"), 
                    style = header_style,
                    justify = "center"),
    html.Br(),
    
    dbc.Row(dcc.Graph(id = "hist_fig",
                      figure = hist_fig,
                      style = plot_style),
                      justify = "center"),

    dbc.Row(html.Br()),
    html.Br(),
    
    dbc.Row(html.H3("Climate Change Project Deep Dive by Country"), 
                    style = header_style,
                    justify = "center"),
    html.Br(),

    dbc.Row(html.H4("Primary Filter: Select a Country"), 
                    style = header_style,
                    justify = "center"),

    dbc.Row(dcc.Dropdown(id = "country_dd",
                         options = country_options,
                         multi = False,
                         style = small_dropdown_style),
                         justify = "center"),
    html.Br(),

    dbc.Row(html.H4("Secondary Filter: Select Another Country to Compare"), 
                    style = header_style,
                    justify = "center"),
    
    dbc.Row(dcc.Dropdown(id = "second_country_dd",
                         options = country_options,
                         multi = False,
                         style = small_dropdown_style),
                         justify = "center"),
    html.Br(),
    
    dbc.Row(html.H3("Data Table: Comparison of Country GDP and Climate Vulnerability"), 
                    style = header_style,
                    justify = "center"),
    
    dbc.Row(dash_table.DataTable(id = "hl_data_table",
                                 data = hl_df.to_dict("records"),
                                 columns = hl_data_table_options,
                                 page_current = 0,
                                 page_size = 5,
                                 style_data = hl_data_table_text,
                                 style_cell = hl_data_table_cell)),
    html.Br(),

    dbc.Row("The ND-GAIN Country Index summarizes a country's vulnerability to \
            climate change and other global challenges in combination with its \
            readiness to improve resilience. It aims to help governments, businesses \
            and communities better prioritize investments for a more efficient \
            response to the immediate global challenges ahead."),

    html.Br(),

    dbc.Row("World wide ranking by ND-GAIN Index, higher scores are better"),

    html.Br(),
    html.Br(),
    html.Div(html.Br()),

    html.Div(html.H5("Category Filter: Project Breakdown"), 
                     style = hl_reg_layout_style),
    
    html.Div(dcc.Dropdown(id = "bar_x_filter",
                          options = bar_options,
                          multi = False),
                          style = bar_filter),
    html.Div(html.Br()),

    html.Div(html.H5("Color Filter: Project Breakdown"), 
                     style = hl_reg_layout_style),
    
    html.Div(dcc.Dropdown(id = "bar_color_filter",
                          options = bar_options,
                          multi = False),
                          style = bar_filter),
    html.Br(),
    html.Br(),

    html.Div(children = 
             [html.Div(dcc.Graph(id = "bar", 
                                 figure = bar_fig,
                                 style = plot_style), 
                                 style = hl_reg_style),
            
              html.Div(dcc.Graph(id = "ll_scatter",
                                 figure = scatter_fig,
                                 style = plot_style), 
                                 style = hl_reg_style)],
                                 style = hl_reg_layout_style),  
    html.Br(),
    html.Br(),
    html.Br(),

    dbc.Row(html.H3("Data Table: Projects for Selected Country"), 
                    style = header_style,
                    justify = "center"),
    html.Br(),

    dbc.Row(dash_table.DataTable(id = "ll_data_table",
                                 data = ll_df.to_dict('records'), 
                                 columns = bottom_table_cols,
                                 page_current = 0,
                                 page_size = 10,
                                 css = [{"selector": "table", "rule": "able-layout: fixed"}],
                                 style_cell = ll_data_table_cell)),
    html.Br(),
    html.Br(),

    dbc.Row("Sources: World Bank Open Data and the Asian Development Bank Data Library"),

    html.Br()],

fluid = True, style = {"backgroundColor": "#D2E5D0"})

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
            new_df = new_df[new_df["Funding Source"] == secondary_filter]
        elif secondary_filter == "World Bank":
            new_df = new_df[new_df["Funding Source"] == secondary_filter]
        else:
            new_df = new_df[new_df["Funding Source"] == "Total"]

    elif primary_filter == "(Post-Paris Agreement)":
        new_df = hl_df.filter(regex = "Post|Source|Country")
        if dd is None:
            color_filter = "Project Count (Post-Paris Agreement)"
        else: 
            color_filter = dd + " " + primary_filter
        if secondary_filter == "ADB":
            new_df = new_df[new_df["Funding Source"] == secondary_filter]
        elif secondary_filter == "World Bank":
            new_df = new_df[new_df["Funding Source"] == secondary_filter]
        else:
            new_df = new_df[new_df["Funding Source"] == "Total"]
    
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
                            scope = "asia",
                            title = f"{title_label}")

    map_fig.update_coloraxes(colorbar_orientation = "h", colorbar_len = .7)
    map_fig.update_geos(center = {"lat": 28, "lon": 87})
    map_fig.update_layout(coloraxis_colorbar_y = -0.2,
                          paper_bgcolor = "#D2E5D0",
                          title_x = 0.5)
    map_fig.update_layout(margin = {"l":20, "r":12, "t":40, "b":40, "pad": 10})

    return map_fig

@app.callback(Output("hl_data_table", "data"),
              [Input("country_dd", "value"),
               Input("second_country_dd", "value")])

def update_table(country_dd, secondary_country_dd):
    
    if country_dd is None:
        final_filter = hl_df[hl_df["Funding Source"] == "Total"]
        return final_filter.to_dict("records")
    
    elif country_dd is not None:
        if secondary_country_dd is not None:
            data_table_filter = hl_df[(hl_df["Country"] == country_dd) | 
                                      (hl_df["Country"] == secondary_country_dd)]
        else:
            data_table_filter = hl_df[hl_df["Country"] == country_dd]
        final_filter = data_table_filter[data_table_filter["Funding Source"] == "Total"]
        return final_filter.to_dict("records")

@app.callback(Output("ll_scatter", "figure"),
              Input("country_dd", "value"))

def update_scatter(country):

    scatter_df = ll_df[ll_df["Country"] == country]
    scatter_df["Project Count by Year"] = scatter_df.groupby(["Year"])["Project Name"].transform("count")
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

    bar_data_filter = ll_df[ll_df["Country"] == country]

    fig = px.bar(bar_data_filter, 
                 x = x_filter, 
                 y = "Commitment Amount",
                 color = color_filter,
                 title = f"Commitment Amount by {x_filter} in {country}",
                 labels = {"Commitment Amount": "Commitment Amount"})
    
    return fig

@app.callback(Output("ll_data_table", "data"),
              Input("country_dd", "value"))

def update_table(country):

    data_table_filter = ll_df[ll_df["Country"] == country]
    return data_table_filter.to_dict("records")

if __name__ == "__main__":
    app.run_server(debug = True, host = "0.0.0.0", port = 8071)