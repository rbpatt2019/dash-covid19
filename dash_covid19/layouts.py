# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
import dash_table as table
from dash_covid19.app import data

layouts = {
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
