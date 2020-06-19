# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output
from dash_covid19.helper_components.graphs import line_plot
import plotly.graph_objects as go


def init_callbacks(dash_app, layouts, data):
    """Initialise dash callbacks"""

    @dash_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def display_page(path):
        try:
            fmt = layouts[path]
        except KeyError:
            fmt = layouts["/"]
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
            "layout": go.Layout(
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

    @dash_app.callback(
        Output("exp-x-scatter", "figure"),
        [
            Input("exp-dd-x", "value"),
            Input("exp-main-scatter", "hoverData"),
            Input("exp-scale-x", "on"),
        ],
    )
    def update_x_scatter(variable, hoverData, scale):
        country = hoverData["points"][0]["customdata"]
        data_sub = data[data["location"] == country]
        title = f"<b>{country}</b>"
        return line_plot(
            data_sub, variable=variable, title=f"<b>{country}</b>", scale=scale
        )

    @dash_app.callback(
        Output("exp-y-scatter", "figure"),
        [
            Input("exp-dd-y", "value"),
            Input("exp-main-scatter", "hoverData"),
            Input("exp-scale-y", "on"),
        ],
    )
    def update_y_scatter(variable, hoverData, scale):
        country = hoverData["points"][0]["customdata"]
        data_sub = data[data["location"] == country]
        title = f"<b>{country}</b>"
        return line_plot(
            data_sub, variable=variable, title=f"<b>{country}</b>", scale=scale
        )
