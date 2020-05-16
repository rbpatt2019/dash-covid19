# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table
import plotly.express as px


def init_layouts(dash_app, df):
    """Initialise layouts and return default"""

    layouts = {
        "app": html.Div(
            [
                dcc.Tabs(
                    id="navigation",
                    value="explorer",
                    vertical=True,
                    children=[
                        dcc.Tab(id="nav-tab-1", label="Explorer", value="explorer"),
                        dcc.Tab(
                            id="nav-tab-2", label="Data Table", value="data-table",
                        ),
                    ],
                    parent_style={"float": "left"},
                    style={"width": "90%"},
                ),
                html.Div(id="page-content"),
            ]
        ),
        "explorer": html.Div(
            id="exp",
            children=[
                dcc.Graph(
                    id="exp-world-map",
                    figure=px.scatter_geo(
                        df,
                        locations="iso_code",
                        hover_name="location",
                        size="total_cases",
                        animation_frame=df[["date"]].astype(str),
                        projection="eckert4",
                        height=750,
                        title="Total Cases of Covid-19 over Time",
                    ),
                ),
            ],
            style={"width": "90%", "display": "inline-block"},
        ),
        "data-table": html.Div(
            id="dt",
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
            style={"width": "50%", "display": "inline-block"},
        ),
    }

    dash_app.layout = layouts["app"]
    return dash_app, layouts
