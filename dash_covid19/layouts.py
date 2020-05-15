# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table

from dash_covid19 import data

layouts = {
    "app": html.Div(
        [
            dcc.Tabs(
                id="navigation",
                value="explorer",
                children=[
                    dcc.Tab(id="nav-tab-1", label="Explorer", value="explorer",),
                    dcc.Tab(id="nav-tab-2", label="Data Table", value="data-table",),
                ],
            ),
            html.Div(id="page-content"),
        ]
    ),
    "data-table": html.Div(
        id="dt",
        children=[
            html.H5("Data Table", id="dt-header"),
            table.DataTable(
                id="dt-data",
                columns=[{"name": i, "id": i, "deletable": True} for i in data.columns],
                data=data.to_dict("records"),
                sort_action="native",
                filter_action="native",
                page_action="native",
                page_current=0,
                page_size=25,
            ),
        ],
    ),
    "explorer": html.Div(
        id="exp",
        children=[
            html.H5("Explorer", id="exp-header"),
            html.H6("Graph to go here", id="exp-graph"),
        ],
    ),
}
