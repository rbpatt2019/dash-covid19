# -*- coding: utf-8 -*-
import plotly.express as px
from dash.dependencies import Input, Output
from dash_covid19.helper_components.graphs import line_plot


def init_callbacks(dash_app, layouts, data):
    """Initialise dash callbacks"""

    @dash_app.callback(
        [
            Output("page-content", "children"),
            Output("nav-bar-exp", "active"),
            Output("nav-bar-map", "active"),
            Output("nav-bar-dt", "active"),
        ],
        [Input("url", "pathname")],
    )
    def display_page(path):
        """Callback for update app page layout

        The try/else/finally block ensures that a 404 error is never thrown.
        When in doubt, redirect to the home page.

        The outputs to nav-bar-xxx 'active' are necessary as clicking on the cards
        on the hme page does not trigger the links to show active. These outputs
        guarantee that they will show 'active' no matter how they are triggered.

        active_lut contains the necessary booleean encodings for active links.
        active_lut['/'][0] is the exp link, while active_lut['/'][1] is dt
        """
        active_lut = {
            "/": (False, False, False),
            "/exp": (True, False, False),
            "/map": (False, True, False),
            "/dt": (False, False, True),
        }
        try:
            fmt = layouts[path]
            exp, map, dt = active_lut[path]
        except KeyError:
            fmt = layouts["/"]
            exp, map, dt = active_lut["/"]
        finally:
            return fmt, exp, map, dt

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
    def update_exp_main_scatter(x_axis, y_axis, x_log, y_log, date_val):
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
                margin=dict(t=50, b=50, l=50, r=150, pad=0, autoexpand=False),
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
    def update_exp_x_scatter(variable, hoverData, scale):
        country = hoverData["points"][0]["customdata"]
        data_sub = data[data["location"] == country]
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
    def update_exp_y_scatter(variable, hoverData, scale):
        country = hoverData["points"][0]["customdata"]
        data_sub = data[data["location"] == country]
        return line_plot(
            data_sub, variable=variable, title=f"<b>{country}</b>", scale=scale
        )

    @dash_app.callback(
        Output("map-scatter", "figure"),
        [
            Input("map-color-dd", "value"),
            Input("map-size-dd", "value"),
            Input("map-slider", "value"),
        ],
    )
    def update_map_scatter(size, color, date_val):
        date = data.date.unique()[date_val]
        data_sub = data[data["date"] == date]
        return px.scatter_mapbox(
            data_frame=data_sub,
            lat="lat",
            lon="lon",
            color=color,
            size=size,
            color_continuous_scale=px.colors.sequential.Plasma,
            mapbox_style="carto-darkmatter",
        )
