# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

counts = {"clicks": 0}

app.layout = html.Div(
    [html.Div("My test layout", id="out"), html.Button("click me", id="click-me")]
)


@app.callback(Output("out", "children"), [Input("click-me", "n_clicks")])
def on_click(n_clicks):
    if n_clicks is None:
        raise PreventUpdate

    counts["clicks"] += 1
    return "Clicked: {}".format(n_clicks)


if __name__ == "__main__":
    app.run_server(debug=True)
