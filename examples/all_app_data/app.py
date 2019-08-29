import dash
import dash_html_components as html
import dash_design_kit as ddk
import dash_core_components as dcc
import dash_table
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import pandas as pd

import tasks

def get_timestamps():
    start = "Start: " + tasks.r_get_run_start_time()
    finish = "Finish: " + tasks.r_get_run_finish_time()
    return html.Div(children=[html.P(start), html.P(finish)])

def get_app_data_df():
    app_data = tasks.r_get_app_data()
    df = pd.DataFrame(data=app_data)
    return df

def layout():
    df = get_app_data_df()
    return ddk.App(
    show_editor=True,
    children=[
        ddk.Card(
            children=[
                ddk.CardHeader(title="GraphQL Query"),
                dash_table.DataTable(
                    id="graphql-table",
                    columns=[{"name": col, "id": col} for col in df.columns],
                    data=df.to_dict("records"),
                    style_cell={
                        "whiteSpace": "no-wrap",
                        "overflow": "hidden",
                        "textOverflow": "ellipsis",
                        "maxWidth": 0,
                    },
                ),
            ]
        ),
        ddk.Card(
            children=[
                html.Button("Update Table", id="redis-table-button", n_clicks=0),
                html.Button("Check Timestamps", id="redis-time-button", n_clicks=0),
                html.Button(
                    "GraphQL Query (Manual)", id="redis-long-query", n_clicks=0
                ),
            ]
        ),
        html.Div(id="timestamp"),
        dcc.Interval(id="check-query-finished", n_intervals=0, interval=5 * 1000),
    ],
)

app = dash.Dash(__name__)

server = app.server

app.layout = layout()


@app.callback(
    [Output("graphql-table", "columns"), 
    Output("graphql-table", "data")],
    [Input("redis-table-button", "n_clicks")],
)
def update_table(n_clicks):
    if n_clicks >= 1:
        df_table = get_app_data_df()
        return [{"name": col, "id": col} for col in df_table.columns], df_table.to_dict("records")
    raise dash.exceptions.PreventUpdate


@app.callback(
    Output("timestamp", "children"),
    [
        Input("redis-long-query", "n_clicks"),
        Input("redis-time-button", "n_clicks"),
        Input("check-query-finished", "n_intervals"),
    ],
)
def update_query_status(n_clicks_query, n_clicks_time, n_intervals):
    ctx = dash.callback_context
    if "redis-long-query" in ctx.triggered[0]["prop_id"]:
        start = "Start: " + tasks.r_get_run_start_time()
        tasks.update_data()
    return get_timestamps()

if __name__ == "__main__":
    app.run_server(debug=True)
