import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output
from scripts.load_data import load_data
from scripts.clean_data import clean_data

df1, df2, df3, df4, df5, df6 = load_data()
df_merged = clean_data(df1, df2, df3, df4, df5, df6)

app = Dash(__name__, server=False)

app.layout = html.Div([
    html.H1("Amazing Informative Dashboard"),
    dcc.Dropdown(
        id='metric-dropdown',
        options=[{'label': col, 'value': col} for col in df_merged.columns if df_merged[col].dtype in ['int64', 'float64']],
        value=df_merged.columns[0]
    ),
    dcc.Graph(id='main-graph'),
    dcc.Graph(id='secondary-graph')
])

@app.callback(
    Output('main-graph', 'figure'),
    Output('secondary-graph', 'figure'),
    Input('metric-dropdown', 'value')
)
def update_graphs(selected_metric):
    fig1 = px.bar(df_merged, x='full_name', y=selected_metric)
    fig2 = px.line(df_merged, x='timedata', y=selected_metric)
    return fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=True)

)
def update_graphs(selected_metric):
    fig1 = px.bar(df_merged, x='full_name', y=selected_metric)
    fig2 = px.line(df_merged, x='timedata', y=selected_metric)
    return fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=True)
