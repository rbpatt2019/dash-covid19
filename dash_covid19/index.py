# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_covid19.callbacks
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_covid19.app import app
from dash_covid19.layouts import layouts

app.layout = html.Div(
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
)


@app.callback(Output("page-content", "children"), [Input("navigation", "value")])
def display_page(value):
    if value in layouts.keys():
        return layouts[value]
    else:
        return layouts["404"]


if __name__ == "__main__":
    app.run_server(debug=True)
