# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table
import plotly.express as px
from dash_covid19.helper_components.navbar import navbar
from dash_covid19.helper_components.dropdown import make_dd
from dash_covid19.helper_components.span_with_tooltip import make_col_span_tt


def init_layouts(dash_app, df, cols):
    """Initialise layouts and return default"""

    layouts = {
        "app": dbc.Container(
            fluid=True,
            children=[
                dcc.Location(id="url", refresh=False),
                dbc.Row(dbc.Col(navbar)),
                dbc.Row(dbc.Col(id="page-content")),
            ],
        ),
        "/exp": dbc.Container(
            id="exp",
            fluid=True,
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            html.Span(
                                "X-axis variable...",
                                id="exp-dd-x-head",
                                style={
                                    "textDecoration": "underline",
                                    "cursor": "pointer",
                                },
                            ),
                            width=6,
                        ),
                        dbc.Tooltip(
                            "Choose from columns in the dataset"
                            " which is to be plotted on the X-axis",
                            id="exp-dd-x-help",
                            target="exp-dd-x-head",
                        ),
                        dbc.Col(
                            html.Span(
                                "Y-axis variable...",
                                id="exp-dd-y-head",
                                style={
                                    "textDecoration": "underline",
                                    "cursor": "pointer",
                                },
                            ),
                            width=6,
                        ),
                        dbc.Tooltip(
                            "Choose from columns in the dataset"
                            " which is to be plotted on the Y-axis",
                            id="exp-dd-y-help",
                            target="exp-dd-y-head",
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(make_dd(id="exp-dd-x", options=cols), width=6),
                        dbc.Col(make_dd(id="exp-dd-y", options=cols), width=6),
                    ]
                ),
                # dbc.Row(dbc.Col(dcc.Graph(id="exp-world-map"))),
                # dbc.Row(dbc.Col(dcc.RangeSlider))
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
