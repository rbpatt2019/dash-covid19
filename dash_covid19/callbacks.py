# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output

from dash_covid19.layouts import layouts


@app.callback(Output("page-content", "children"), [Input("navigation", "value")])
def display_page(value):
    return layouts[value]
