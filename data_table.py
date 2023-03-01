from dash import Dash, dash_table
from final_project.dashboard import app

def build_data_table(df, country):

    data_table_filter = df[df["Country / Economy"] == country]
    
    app.layout = dash_table.DataTable(
    columns=[
        {'name': 'Country', 'id': 'country', 'type': 'text'}
    ],
    data=data_table_filter.to_dict('records'),
    filter_action='native',

    style_table={
        'height': 400,
    },
    style_data={
        'width': '150px', 'minWidth': '150px', 'maxWidth': '150px',
        'overflow': 'hidden',
        'textOverflow': 'ellipsis',
    }
)