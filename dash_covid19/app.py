# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div(
    [
        dcc.Tabs(
            [
                dcc.Tab(
                    label="App",
                    children=[
                        dcc.Markdown(
                            """
                            # Welcome!

                            Things are still in the early stages here.
                            Eventually, you'll see a fancy Dash app that displays an interactive
                            version of the WHO's Covid-19 data. Crossfiltering, interactive
                            plots, the whole kit and kaboodle.

                            Stay tuned for more updates!
                            """
                        )
                    ],
                ),
                dcc.Tab(
                    label="Docs",
                    children=[
                        dcc.Markdown(
                            """
                            # Welcome!

                            Eventually, the documentation for the app interface will go here.
                            It will explain the graph types, and what the different filters
                            do. This might move into it's own app, if things get big. We'll see!
                            """
                        )
                    ],
                ),
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
