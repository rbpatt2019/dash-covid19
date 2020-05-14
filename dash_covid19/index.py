# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from dash_covid19.app import app
from dash_covid19.layouts import layouts

app.layout = layouts["app"]


@app.callback(Output("page-content", "children"), [Input("navigation", "value")])
def display_page(value):
    return layouts[value]


if __name__ == "__main__":
    app.run_server(debug=True)
