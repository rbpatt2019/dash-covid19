# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table
import plotly.express as px
from dash_covid19.helper_components.navbar import navbar


def init_layouts(dash_app, df, cols):
    """Initialise layouts and return default"""

    layouts = {
        "app": html.Div(
            children=[
                dcc.Location(id="url", refresh=False),
                dbc.Row(dbc.Col(navbar)),
                dbc.Row(dbc.Col(html.Div(id="page-content"))),
            ],
        ),
        "/exp": dbc.Container(
            id="exp",
            fluid=True,
            children=[
                dcc.Dropdown(
                    id="exp-dd-column",
                    placeholder="Select a variable...",
                    persistence=True,
                    persistence_type="session",
                    clearable=False,
                    options=[{"label": i, "value": i} for i in cols],
                    value=cols[0],
                ),
                dcc.Graph(id="exp-world-map"),
            ],
        ),
        "/dt": dbc.Container(
            id="dt",
            fluid=True,
            children=[
                table.DataTable(
                    id="dt-data",
                    columns=[
                        {"name": i, "id": i, "deletable": True} for i in df.columns
                    ],
                    data=df.to_dict("records"),
                    sort_action="native",
                    filter_action="native",
                    page_action="native",
                    page_current=0,
                    page_size=25,
                ),
            ],
        ),
    }

    dash_app.layout = layouts["app"]
    return dash_app, layouts
