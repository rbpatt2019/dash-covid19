# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import dash_table as table

from dash_covid19.helper_components.cards import code_card, dt_card, exp_card, info_card
from dash_covid19.helper_components.dropdown import make_dd
from dash_covid19.helper_components.navbar import navbar
from dash_covid19.helper_components.slider import make_slider


def init_layouts(dash_app, df, cols):
    """Initialise layouts and return default"""

    header = """
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
                    style={"margin-top": "20px"},
                    children=dbc.Col(
                        [
                            html.H3(
                                "dash-covid19: Visualise Your World",
                                style={"text-align": "center"},
                            ),
                            html.P(header, style={"text-align": "center"}),
                        ],
                        width=8,
                    ),
                ),
                dbc.Row(
                    justify="around",
                    style={"margin-top": "20px"},
                    children=[dbc.Col(exp_card, width=4), dbc.Col(dt_card, width=4)],
                ),
                dbc.Row(
                    justify="around",
                    style={"margin-top": "20px"},
                    children=[dbc.Col(code_card, width=4), dbc.Col(info_card, width=4)],
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
                                ),
                                html.H5(
                                    "Date Slider.",
                                    id="exp-main-slider-head",
                                    className="mt-3",
                                    style={
                                        "textDecoration": "underline",
                                        "cursor": "pointer",
                                    },
                                ),
                                dbc.Tooltip(
                                    "Slide through the dates to see how patterns"
                                    " evolve over time.",
                                    id="exp-main-slider-help",
                                    target="exp-main-slider-head",
                                ),
                                make_slider(df, "exp-main-slider"),
                            ],
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
                                            children=[
                                                html.H5(
                                                    "X-axis Variable",
                                                    id="exp-dd-x-head",
                                                    style={
                                                        "textDecoration": "underline",
                                                        "cursor": "pointer",
                                                    },
                                                ),
                                                make_dd(id="exp-dd-x", options=cols),
                                            ],
                                            width=4,
                                        ),
                                        dbc.Tooltip(
                                            "Choose from columns in the dataset"
                                            " which is to be plotted on the X-axis",
                                            id="exp-dd-x-help",
                                            target="exp-dd-x-head",
                                        ),
                                        dbc.Col(
                                            children=[
                                                html.H5(
                                                    "X-axis: Log Scale?",
                                                    id="exp-scale-x-head",
                                                    style={
                                                        "textDecoration": "underline",
                                                        "cursor": "pointer",
                                                    },
                                                ),
                                                daq.BooleanSwitch(
                                                    id="exp-scale-x", on=False
                                                ),
                                            ],
                                            width=4,
                                        ),
                                        dbc.Tooltip(
                                            "Click to enable a log scale for the X-axis"
                                            ". Click again to return to linear.",
                                            id="exp-scale-x-help",
                                            target="exp-scale-x-head",
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
                                            children=[
                                                html.H5(
                                                    "Y-axis Variable",
                                                    id="exp-dd-y-head",
                                                    style={
                                                        "textDecoration": "underline",
                                                        "cursor": "pointer",
                                                    },
                                                ),
                                                make_dd(
                                                    id="exp-dd-y",
                                                    options=cols,
                                                    default_index=1,
                                                ),
                                            ],
                                            width=4,
                                        ),
                                        dbc.Tooltip(
                                            "Choose from columns in the dataset"
                                            " which is to be plotted on the Y-axis",
                                            id="exp-dd-y-help",
                                            target="exp-dd-y-head",
                                        ),
                                        dbc.Col(
                                            children=[
                                                html.H5(
                                                    "Y-axis: Log Scale?",
                                                    id="exp-scale-y-head",
                                                    style={
                                                        "textDecoration": "underline",
                                                        "cursor": "pointer",
                                                    },
                                                ),
                                                daq.BooleanSwitch(
                                                    id="exp-scale-y", on=False
                                                ),
                                            ],
                                            width=4,
                                        ),
                                        dbc.Tooltip(
                                            "Click to enable a log scale for the Y-axis"
                                            ". Click again to return to linear.",
                                            id="exp-scale-y-help",
                                            target="exp-scale-y-head",
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
        # "/map": dbc.Col(
        #     style={"height": '100%'},
        #     children=[],
        # ),
        "/dt": dbc.Col(
            style={"height": "100%"},
            # className='d-flex justify-content-center',
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
