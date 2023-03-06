from project_tracker.bob_stats import rda_logreg, rda_linearreg, hist_data
from project_tracker.load_and_clean.load_data import hl_df, ll_df
import plotly.express as px

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

scatter_fig = px.scatter(ll_df, 
                         x = "Effective Date", 
                         y = "Commitment Amount",
                         title = "Project Investment over Time",
                         labels = {"Commitment Amount": "Commitment Amount"},
                         trendline = "ols")

bar_fig = px.bar(ll_df, 
                 x = "Status", 
                 y = "Commitment Amount",
                 #color = "Sector",
                 title = "Project Breakdown",
                 labels = {"Commitment Amount": "Commitment Amount",
                           "Status": "Project Status"})