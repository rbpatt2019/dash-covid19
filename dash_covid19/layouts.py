# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table
import plotly.express as px
from dash_covid19.helper_components.navbar import navbar
from dash_covid19.helper_components.dropdown import make_dd


def init_layouts(dash_app, df, cols, date_idx):
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
                    dbc.Col(
                        dcc.Graph(
                            id="exp-main-scatter",
                            hoverData={"points": [{"customdata": "China"}]},
                        )
                    )
                ),
                html.Hr(),
                dbc.Row(
                    justify="around",
                    children=[
                        dbc.Col(
                            html.H5(
                                "Date Slider.",
                                id="exp-main-slider-head",
                                style={
                                    "textDecoration": "underline",
                                    "cursor": "pointer",
                                },
                            ),
                            width="auto",
                        ),
                        dbc.Tooltip(
                            "Slide through the dates to see how patterns"
                            " evolve over time.",
                            id="exp-main-slider-help",
                            target="exp-main-slider-head",
                        ),
                    ],
                ),
                dbc.Row(
                    dbc.Col(
                        dcc.Slider(
                            id="exp-main-slider",
                            min=min(date_idx),
                            max=max(date_idx),
                            value=max(date_idx),
                            marks={
                                val: str(date)
                                for val, date in zip(
                                    date_idx[::7], df.date.unique()[::7]
                                )
                            },
                        )
                    )
                ),
                html.Hr(),
                dbc.Row(
                    justify="around",
                    children=[
                        dbc.Col(
                            html.H5(
                                "X-axis Variable",
                                id="exp-dd-x-head",
                                style={
                                    "textDecoration": "underline",
                                    "cursor": "pointer",
                                },
                            ),
                            width="auto",
                        ),
                        dbc.Tooltip(
                            "Choose from columns in the dataset"
                            " which is to be plotted on the X-axis",
                            id="exp-dd-x-help",
                            target="exp-dd-x-head",
                        ),
                        dbc.Col(
                            html.H5(
                                "Y-axis Variable",
                                id="exp-dd-y-head",
                                style={
                                    "textDecoration": "underline",
                                    "cursor": "pointer",
                                },
                            ),
                            width="auto",
                        ),
                        dbc.Tooltip(
                            "Choose from columns in the dataset"
                            " which is to be plotted on the Y-axis",
                            id="exp-dd-y-help",
                            target="exp-dd-y-head",
                        ),
                    ],
                ),
                dbc.Row(
                    justify="around",
                    children=[
                        dbc.Col(make_dd(id="exp-dd-x", options=cols), width=2),
                        dbc.Col(
                            make_dd(id="exp-dd-y", options=cols, default_index=1),
                            width=2,
                        ),
                    ],
                ),
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
