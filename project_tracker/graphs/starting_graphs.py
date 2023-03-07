from project_tracker.graphs.reg_plots import rda_logreg, rda_linearreg, hist_data
from project_tracker.load_and_clean.wb_preprocess import avg_commitment_plot
from project_tracker.load_and_clean.load_data import hl_df, ll_df
import plotly.express as px

#Author: Nadir Shahzad Khan
# Build Figures

logreg_fig = rda_logreg()
linreg_fig = rda_linearreg()
hist_fig = hist_data()
avg_commit_fig = avg_commitment_plot()

map_fig = px.choropleth(hl_df,
                        locations="Country", 
                        locationmode="country names",
                        scope='asia')

map_fig.update_geos(resolution=110)
map_fig.update_layout(paper_bgcolor="#D2E5D0")

scatter_fig = px.scatter(ll_df, 
                         x="Effective Date", 
                         y="Commitment Amount",
                         title="Project Investment over Time",
                         labels={"Commitment Amount": "Commitment Amount"},
                         trendline="ols")

bar_fig = px.bar(ll_df, 
                 x="Status", 
                 y="Commitment Amount",
                 title="Project Breakdown",
                 labels={"Commitment Amount": "Commitment Amount",
                         "Status": "Project Status"})