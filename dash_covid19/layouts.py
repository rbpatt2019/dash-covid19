# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table
from dash_covid19.app import data

layouts = {
    "app": html.Div(
        [
            dcc.Tabs(
                id="navigation",
                value="explorer",
                parent_className="nav-tabs",
                className="nav-tabs-container",
                children=[
                    dcc.Tab(
                        label="Explorer",
                        value="explorer",
                        className="nav-tab",
                        selected_className="nav-tab--selected",
                    ),
                    dcc.Tab(
                        label="Data Table",
                        value="data-table",
                        className="nav-tab",
                        selected_className="nav-tab--selected",
                    ),
                ],
            ),
            html.Div(id="page-content"),
        ]
    ),
    "data-table": html.Div(
        [
            html.H5("Data Table"),
            table.DataTable(
                id="data-table",
                columns=[{"name": i, "id": i, "deletable": True} for i in data.columns],
                data=data.to_dict("records"),
                sort_action="native",
                filter_action="native",
                page_action="native",
                page_current=0,
                page_size=25,
            ),
        ]
    ),
    "explorer": html.Div([html.H5("Explorer"), html.H6("## Graph to go here")]),
}
