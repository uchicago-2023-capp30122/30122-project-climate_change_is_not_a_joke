from dash import Dash, dash_table
from final_project.dashboard import app

def build_data_table(df, country):

    data_table_filter = df[df["Country / Economy"] == country]
    app.layout = dash_table.DataTable(data_table_filter.to_dict('records'), [{"name":i, "id":i} for i in df.columns])) 
