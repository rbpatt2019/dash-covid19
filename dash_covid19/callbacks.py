# -*- coding: utf-8 -*-
"""Module: Callbacks

To comply with the Flask Application factory layout - as Dash apps are really just
Flask apps under the hood - this function initialises the callbacks for the app.

"""
from typing import Any, Dict, List, Tuple, Union

import dash
import pandas as pd
import plotly
import plotly.express as px
from dash.dependencies import Input, Output

from dash_covid19.helper_components.graphs import line_plot


def init_callbacks(
    dash_app: dash.dash.Dash, layouts: Dict[str, Any], df: pd.DataFrame
) -> None:
    """Initialise callbacks

    This function is called with create_app() to initialise the app callbacks in
    accordance with Flask Application Factory principles.

    Parameters
    ----------
    dash_app : dash.dash.Dash
        A dash app instantiated with dash.Dash()
    layouts : Dict[str, Any]
        Dictionary containung href: layout pairs
    df : pd.DataFrame
        The data to be used with the app

    Returns
    -------
    None
    """

    @dash_app.callback(
        [
            Output("page-content", "children"),
            Output("nav-bar-ovw", "active"),
            Output("nav-bar-exp", "active"),
            Output("nav-bar-map", "active"),
            Output("nav-bar-dt", "active"),
        ],
        [Input("url", "pathname")],
    )
    def display_page(path: str) -> Tuple[Any, bool, bool, bool, bool]:
        """Callback for update app page layout

        The try/else block ensures that a 404 error is never thrown.
        When in doubt, redirect to the home page.

        The outputs to nav-bar-xxx 'active' are necessary as clicking on the cards
        on the hme page does not trigger the links to show active. These outputs
        guarantee that they will show 'active' no matter how they are triggered.

        Parameters
        ----------
        path : str
            The href to be checked for page changing

        Returns
        -------
        Tuple[Any, bool, bool, bool]
            Containing 4 objects:

            fmt : Any
                The page layout
            ovw : bool
            exp : bool
            mp : bool
            dt : bool
                The active state of the navigation links
        """
        active_lut = {
            "/": (False, False, False, False),
            "/ovw": (True, False, False, False),
            "/exp": (False, True, False, False),
            "/map": (False, False, True, False),
            "/dt": (False, False, False, True),
        }
        try:
            fmt = layouts[path]
            ovw, exp, mp, dt = active_lut[path]
        except KeyError:
            fmt = layouts["/"]
            ovw, exp, mp, dt = active_lut["/"]
        return fmt, ovw, exp, mp, dt

    @dash_app.callback(
        [
            Output("ovw-ncpm", "value"),
            Output("ovw-tcpm", "value"),
            Output("ovw-ndpm", "value"),
            Output("ovw-tdpm", "value"),
        ],
        [Input("ovw-dd", "value")],
    )
    def update_summary_LEDs(country: str) -> Tuple[float, ...]:
        """Callback for updating summary displays

        Parameters
        ----------
        country : str
            Country whose data will be displayed

        Returns
        -------
        Tuple[float, ...]
            Containing 4 values:
                ovw-ncpm
                ovw-tcpm
                ovw-ndpm
                ovw-tdpm
        """
        df_sub = df[df["location"] == country].sort_values("date", ascending=False)
        df_sub = df_sub.loc[
            df_sub.index[[0]],
            [
                "new_cases_per_million",
                "total_cases_per_million",
                "new_deaths_per_million",
                "total_deaths_per_million",
            ],
        ].round(3)
        return tuple(df_sub.to_numpy()[0])

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
    def update_exp_main_scatter(
        x_axis: str, y_axis: str, x_log: bool, y_log: bool, date_val: int
    ) -> Dict[str, Any]:
        """Callback for updating the main scatter plot

        As dcc.Slider still struggles with dates, the call back passes in an int that
        encodes a unique date. This int is then matched to its date for filtering.

        Parameters
        ----------
        x_axis : str
            Variable for x-axis of scatter plot
        y_ayis : str
            Variable for y-axis of scatter plot
        x_log : bool
            Whether or not a log scale is to be used for the x-axis
        y_log : bool
            Whether or not a log scale is to be used for the y-axis
        date_val : int
            A unique integer encoding the actual date

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the plotly settings to be updated

            The first key is 'data', and its value is a list of dictionaries, each
            representing a different continent, encoded by colour

            The second key is 'laayout', and its value is a dictionary containing
            settings for the plot
        """
        date = df.date.unique()[date_val]
        df_sub = df[df["date"] == date]
        return {
            "data": [
                dict(
                    x=df_sub[df_sub["continent"] == continent][x_axis],
                    y=df_sub[df_sub["continent"] == continent][y_axis],
                    text=df_sub[df_sub["continent"] == continent]["location"],
                    customdata=df_sub[df_sub["continent"] == continent]["location"],
                    mode="markers",
                    marker={
                        "size": 10,
                        "opacity": 0.8,
                        "line": {"width": 0.5, "color": "white"},
                    },
                    name=continent,
                )
                for continent in sorted(df_sub["continent"].unique())
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
    def update_exp_x_scatter(
        variable: str,
        hoverData: Dict[str, List[Dict[str, Union[float, str]]]],
        scale: bool,
    ) -> Dict[str, Any]:
        """Callback for updating the x-axis scatter plot

        This callback takes the variable from the x-axis of the main scatter plot and
        plots it against time. The country data displayd is updated by the hoverData
        trigger from the main plot.

        Parameters
        ----------
        Variable : str
            Variable to be plotted against time
        hoverData : str
            Country to be plotted. From main scatter plot.
        scale : bool
            Whether or not a log scale is to be used

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the plotly settings to be updated

            The first key is 'data', and its value is a list of dictionaries, each
            representing a different continent, encoded by colour

            The second key is 'laayout', and its value is a dictionary containing
            settings for the plot
        """
        country = hoverData["points"][0]["customdata"]
        df_sub = df[df["location"] == country]
        return line_plot(
            df_sub, variable=variable, title=f"<b>{country}</b>", scale=scale
        )

    @dash_app.callback(
        Output("exp-y-scatter", "figure"),
        [
            Input("exp-dd-y", "value"),
            Input("exp-main-scatter", "hoverData"),
            Input("exp-scale-y", "on"),
        ],
    )
    def update_exp_y_scatter(
        variable: str,
        hoverData: Dict[str, List[Dict[str, Union[float, str]]]],
        scale: bool,
    ) -> Dict[str, Any]:
        """Callback for updating the y-axis scatter plot

        This callback takes the variable from the y-axis of the main scatter plot and
        plots it against time. The country data displayd is updated by the hoverData
        trigger from the main plot.

        Parameters
        ----------
        Variable : str
            Variable to be plotted against time
        hoverData : str
            Country to be plotted. From main scatter plot.
        scale : bool
            Whether or not a log scale is to be used

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the plotly settings to be updated

            The first key is 'data', and its value is a list of dictionaries, each
            representing a different continent, encoded by colour

            The second key is 'laayout', and its value is a dictionary containing
            settings for the plot
        """
        country = hoverData["points"][0]["customdata"]
        df_sub = df[df["location"] == country]
        return line_plot(
            df_sub, variable=variable, title=f"<b>{country}</b>", scale=scale
        )

    @dash_app.callback(
        Output("map-scatter", "figure"),
        [
            Input("map-color-dd", "value"),
            Input("map-size-dd", "value"),
            Input("map-slider", "value"),
        ],
    )
    def update_map_scatter(
        color: str, size: str, date_val: int
    ) -> plotly.graph_objects.Figure:
        """Callback for updating the Mapbox plot

        This callback updates which variables are representing size and colour for the
        points on the map, as well as updating the point with respect to date.

        As dcc.Slider still struggles with dates, the call back passes in an int that
        encodes a unique date. This int is then matched to its date for filtering.

        Parameters
        ----------
        color : str
            Which variable is to represent colour
        size : str
            Which variable is ro represent size
        date_val : int
            Integer encoding a unique date time

        Returns
        -------
        plotly.graph_objects.Figure
            The scatter_mapbox to be rendered
        """
        date = df.date.unique()[date_val]
        df_sub = df[df["date"] == date].fillna(0)
        return px.scatter_mapbox(
            data_frame=df_sub,
            lat="lat",
            lon="lon",
            color=color,
            size=size,
            hover_name="location",
            zoom=1,
            color_continuous_scale=px.colors.sequential.Plasma,
            mapbox_style="carto-positron",
        )
