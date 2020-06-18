# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import dash_table as table
from dash_covid19.helper_components.navbar import navbar
from dash_covid19.helper_components.dropdown import make_dd
from dash_covid19.helper_components.cards import exp_card, dt_card, code_card, info_card


def init_layouts(dash_app, df, cols, date_idx):
    """Initialise layouts and return default"""

    header = """### dash-covid19: Visualise Your World

        In these rapidly changing times, a good visualisation goes a long way towards
        understanding the complex situation. That's all this app attempts to: provide
        good visualisations, so you can review the facts for yourself. No conclusions,
        no opinions, just good data.

        The cards below provide brief summaries of the sections in the app. Click on
        one to get started! You can also navigate with the links at the top and can
        always return to this page by clicking on dash-covid19 in the top left.
        """

    layouts = {
        "app": dbc.Container(
            fluid=True,
            children=[
                dcc.Location(id="url", refresh=False),
                dbc.Row(dbc.Col(navbar)),
                dbc.Row(dbc.Col(id="page-content")),
            ],
        ),
        "/": dbc.Container(
            id="home",
            fluid=True,
            children=[
                dbc.Row(
                    justify="around",
                    style={"margin-top": "20px"},
                    children=dbc.Col(
                        dcc.Markdown(header, style={"text-align": "center"},),
                        width="auto",
                    ),
                ),
                dbc.Row(
                    justify="around",
                    style={"margin-top": "20px"},
                    children=[dbc.Col(exp_card, width=5), dbc.Col(dt_card, width=5)],
                ),
                dbc.Row(
                    justify="around",
                    style={"margin-top": "20px"},
                    children=[dbc.Col(code_card, width=5), dbc.Col(info_card, width=5)],
                ),
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
                                val: {
                                    "label": str(date),
                                    "style": {
                                        "writing-mode": "vertical-lr",
                                        "transform": "rotate(-45deg)",
                                        "transform-origin": "40% 30%",
                                        "white-space": "nowrap",
                                    },
                                }
                                for val, date in zip(
                                    date_idx[::7], df.date.unique()[::7]
                                )
                            },
                        ),
                        style={"margin-bottom": "35px"},
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
                            width=2,
                        ),
                        dbc.Tooltip(
                            "Choose from columns in the dataset"
                            " which is to be plotted on the X-axis",
                            id="exp-dd-x-help",
                            target="exp-dd-x-head",
                        ),
                        dbc.Col(
                            html.H5(
                                "X-axis: Log Scale?",
                                id="exp-scale-x-head",
                                style={
                                    "textDecoration": "underline",
                                    "cursor": "pointer",
                                },
                            ),
                            width=2,
                        ),
                        dbc.Tooltip(
                            "Click to enable a log scale for the X-axis"
                            ". Click again to return to linear.",
                            id="exp-scale-x-help",
                            target="exp-scale-x-head",
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
                            width=2,
                        ),
                        dbc.Tooltip(
                            "Choose from columns in the dataset"
                            " which is to be plotted on the Y-axis",
                            id="exp-dd-y-help",
                            target="exp-dd-y-head",
                        ),
                        dbc.Col(
                            html.H5(
                                "Y-axis: Log Scale?",
                                id="exp-scale-y-head",
                                style={
                                    "textDecoration": "underline",
                                    "cursor": "pointer",
                                },
                            ),
                            width=2,
                        ),
                        dbc.Tooltip(
                            "Click to enable a log scale for the Y-axis"
                            ". Click again to return to linear.",
                            id="exp-scale-y-help",
                            target="exp-scale-y-head",
                        ),
                    ],
                ),
                dbc.Row(
                    justify="around",
                    children=[
                        dbc.Col(make_dd(id="exp-dd-x", options=cols), width=2),
                        dbc.Col(daq.BooleanSwitch(id="exp-scale-x", on=False), width=2),
                        dbc.Col(
                            make_dd(id="exp-dd-y", options=cols, default_index=1),
                            width=2,
                        ),
                        dbc.Col(daq.BooleanSwitch(id="exp-scale-y", on=False), width=2),
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
