# -*- coding: utf-8 -*-
"""Module: Layouts

To comply with the Flask Application factory layout - as Dash apps are really just
Flask apps under the hood - this function initialises the layouts for the app.

As the app is multipage, each page layout is currently stored as a key: value pair
in a dictionary, facilitating easy page changing by using a callback that matches
the href to a key.

One could also write this as multiple, small dash apps, each registered to a route,
to take advantage of more standard Flask structure; however, since the app currently
implements no additional Flask features, there is not currently any plans to do so.
"""
from typing import Dict, List, Tuple, Any

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table
import pandas as pd

from dash_covid19.helper_components.cards import link_card
from dash_covid19.helper_components.dropdown import make_dd
from dash_covid19.helper_components.navbar import navbar
from dash_covid19.helper_components.slider import make_slider
from dash_covid19.helper_components.switch import make_log_switch


def init_layouts(
    dash_app: dash.dash.Dash, df: pd.DataFrame, cols: List[str]
) -> Tuple[dash.dash.Dash, Dict[str, Any]]:
    """Initialise layouts and return default

    This function is called with create_app() to initialise the app layout in
    accordance with Flask Application Factory principles.

    Parameters
    ----------
    dash_app : dash.dash.Dash
        A dash app instantiated with dash.Dash()
    df : pd.DataFrame
        The data to be used with the app
    cols : List[str]
        The columns from df that can be selected for plottint throught the app

    Returns
    -------
    Tuple
        Containing two objects:

        dash_app : dash.dash.Dash
            The passed in Dash app with the layouts initiated
        layouts : Dict[str, Any]
            The dictionary containing the various href: layout key pairs
    """

    header = """
        In these rapidly changing times, a good visualisation goes a long way towards
        understanding the complex situation. That's all this app attempts to provide:
        good visualisations, so you can review the facts for yourself. No conclusions,
        no opinions, just good data.

        The cards below provide brief summaries of the sections in the app. Click on
        one to get started! You can also navigate with the links at the top and can
        always return to this page by clicking on dash-covid19 in the top left.
        """

    layouts = {
        "app": dbc.Container(
            fluid=True,
            style={"height": "100vh"},
            className="bg-light",
            children=[
                dbc.Row(dbc.Col(dcc.Location(id="url", refresh=False))),
                dbc.Row(dbc.Col(navbar), style={"height": "8%"}),
                dbc.Row(id="page-content", style={"height": "92%"}, className="mt-0"),
            ],
        ),
        "/": dbc.Col(
            id="home",
            style={"height": "100%"},
            children=[
                dbc.Row(
                    justify="around",
                    style={"height": "15%"},
                    children=dbc.Col(
                        [
                            html.H3(
                                "dash-covid19: Visualise Your World",
                                style={"text-align": "center"},
                            ),
                            html.P(header, style={"text-align": "center"}),
                        ],
                        width=10,
                    ),
                ),
                dbc.Row(
                    justify="around",
                    style={"margin-top": "20px", "height": "20%"},
                    children=[
                        dbc.Col(
                            link_card(
                                id="exp-card",
                                title="Explore",
                                text="Explore correlations within the data across time, using cross-filtered scatter plots.",
                                href="/exp",
                            ),
                            width=4,
                        ),
                        dbc.Col(
                            link_card(
                                id="map-card",
                                title="World Map",
                                text="Observe regional and global trends across time, using an interactive Mapbox plot.",
                                href="/map",
                            ),
                            width=4,
                        ),
                        dbc.Col(
                            link_card(
                                id="dt-card",
                                title="Data Table",
                                text="Examine the raw data to develop a better understanding of its structure and distribution",
                                href="/dt",
                            ),
                            width=4,
                        ),
                    ],
                ),
                dbc.Row(
                    justify="around",
                    style={"margin-top": "20px", "height": "20%"},
                    children=[
                        dbc.Col(
                            link_card(
                                id="code-card",
                                title="Code",
                                text="This project is proudly open source. Feel free to report bugs and make contriubtions.",
                                href="https://github.com/rbpatt2019/dash-covid19",
                            ),
                            width=4,
                        ),
                        dbc.Col(
                            link_card(
                                id="info-card",
                                title="Info",
                                text="Learn more about the data and how it was collated by the wonderful team at OWID.",
                                href="https://github.com/owid/covid-19-data/tree/master/public/data",
                            ),
                            width=4,
                        ),
                    ],
                ),
            ],
        ),
        "/exp": dbc.Col(
            id="exp",
            style={"height": "100%"},
            children=[
                dbc.Row(
                    style={"height": "80%"},
                    children=[
                        dbc.Col(
                            children=[
                                dcc.Graph(
                                    id="exp-main-scatter",
                                    hoverData={"points": [{"customdata": "China"}]},
                                    style={"height": "90%"},
                                )
                            ]
                            + make_slider(df, "exp-main-slider"),
                            style={"height": "100%"},
                        ),
                        dbc.Col(
                            style={"height": "100%"},
                            width=4,
                            children=[
                                dcc.Graph(id="exp-x-scatter", style={"height": "40%"}),
                                dbc.Row(
                                    justify="around",
                                    style={"height": "10%"},
                                    className="mt-3",
                                    children=[
                                        dbc.Col(
                                            children=make_dd(
                                                "exp-dd-x",
                                                "X-axis Variable",
                                                options=cols,
                                            ),
                                            width=4,
                                        ),
                                        dbc.Col(
                                            children=make_log_switch(
                                                "exp-scale-x", "X-axis"
                                            ),
                                            width=4,
                                        ),
                                    ],
                                ),
                                dcc.Graph(
                                    id="exp-y-scatter",
                                    style={"margin-top": "20px", "height": "40%"},
                                ),
                                dbc.Row(
                                    justify="around",
                                    style={"height": "10%"},
                                    className="mt-3",
                                    children=[
                                        dbc.Col(
                                            children=make_dd(
                                                "exp-dd-y",
                                                "Y-axis Variable",
                                                options=cols,
                                                default_index=1,
                                            ),
                                            width=4,
                                        ),
                                        dbc.Col(
                                            children=make_log_switch(
                                                "exp-scale-y", "Y-axis"
                                            ),
                                            width=4,
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        "/map": dbc.Col(
            style={"height": "100%"},
            children=[
                dbc.Col(
                    style={"height": "100%"},
                    children=[
                        dcc.Graph(id="map-scatter", style={"height": "70%"},),
                        dbc.Row(
                            style={"height": "15%"},
                            children=dbc.Col(make_slider(df, "map-slider")),
                        ),
                        dbc.Row(
                            style={"height": "15%"},
                            justify="around",
                            children=[
                                dbc.Col(
                                    children=make_dd(
                                        "map-size-dd", "Marker Size", options=cols
                                    ),
                                    width=4,
                                ),
                                dbc.Col(
                                    children=make_dd(
                                        "map-color-dd",
                                        "Marker Colour",
                                        options=cols,
                                        default_index=1,
                                    ),
                                    width=4,
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        "/dt": dbc.Col(
            style={"height": "100%"},
            children=[
                table.DataTable(
                    id="dt-data",
                    columns=[{"name": i, "id": i} for i in df.columns],
                    data=df.to_dict("records"),
                    sort_action="native",
                    filter_action="native",
                    fixed_columns={"headers": True, "data": 4},
                    style_table={"minWidth": "100%"},
                    style_cell_conditional=[
                        {"if": {"column_id": "iso_code"}, "width": "1.75%"},
                    ],
                    style_data_conditional=[
                        {
                            "if": {"row_index": "odd"},
                            "backgroundColor": "rgb(223,223,221)",
                        }
                    ],
                    page_action="native",
                    page_current=0,
                    page_size=25,
                ),
            ],
        ),
    }

    dash_app.layout = layouts["app"]
    return dash_app, layouts
