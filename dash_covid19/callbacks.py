# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output


def init_callbacks(dash_app, layouts, data):
    """Initialise dash callbacks"""

    @dash_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def display_page(path):
        try:
            fmt = layouts[path]
        except KeyError:
            fmt = layouts["/exp"]
        finally:
            return fmt

    @dash_app.callback(
        Output("exp-main-scatter", "figure"),
        [
            Input("exp-dd-x", "value"),
            Input("exp-dd-y", "value"),
            Input("exp-scale-x", "on"),
            Input("exp-scale-y", "on"),
            Input("exp-main-slider", "value"),
        ],
    )
    def update_world_map(x_axis, y_axis, x_log, y_log, date_val):
        date = data.date.unique()[date_val]
        data_sub = data[data["date"] == date]
        return {
            "data": [
                dict(
                    x=data_sub[data_sub["continent"] == continent][x_axis],
                    y=data_sub[data_sub["continent"] == continent][y_axis],
                    text=data_sub[data_sub["continent"] == continent]["location"],
                    customdata=data_sub[data_sub["continent"] == continent]["location"],
                    mode="markers",
                    marker={
                        "size": 10,
                        "opacity": 0.8,
                        "line": {"width": 0.5, "color": "white"},
                    },
                    name=continent,
                )
                for continent in sorted(data_sub["continent"].unique())
            ],
            "layout": dict(
                xaxis={
                    "title": x_axis.capitalize(),
                    "type": "log" if x_log else "linear",
                },
                yaxis={
                    "title": y_axis.capitalize(),
                    "type": "log" if y_log else "linear",
                },
                hovermode="closest",
            ),
        }
