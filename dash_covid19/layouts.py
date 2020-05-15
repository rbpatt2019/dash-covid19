# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table


def init_layouts(dash_app, df):
    """Initialise layouts and return default"""

    # Might move this
    # Hack as dcc.Slider does not support pd.dateTime or str
    x_dates = list(range(len(df["date"].dt.date.unique())))
    dict_dates = {
        x: date.strftime("%Y-%m-%d")
        for x, date in list(zip(x_dates, sorted(df["date"].dt.date.unique())))[::7]
    }

    layouts = {
        "app": html.Div(
            [
                dcc.Tabs(
                    id="navigation",
                    value="explorer",
                    vertical=True,
                    children=[
                        dcc.Tab(id="nav-tab-1", label="Explorer", value="explorer",),
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
        "explorer": html.Div(
            id="exp",
            children=[
                dcc.Graph(id="exp-world-map"),
                dcc.Slider(
                    id="exp-date-slider",
                    min=x_dates[0],
                    max=x_dates[-1],
                    value=x_dates[0],
                    marks=dict_dates,
                    step=None,
                ),
            ],
            style={"width": "90%", "display": "inline-block"},
        ),
    }

    dash_app.layout = layouts["app"]
    return dash_app, layouts
