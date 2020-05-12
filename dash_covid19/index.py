# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_covid19.callbacks
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_covid19.app import app
from dash_covid19.layouts import layout_data_table, layout_explorer

app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/apps/data-table":
        return layout_data_table
    elif pathname == "/apps/explorer":
        return layout_explorer
    else:
        return "404"


if __name__ == "__main__":
    app.run_server(debug=True)
