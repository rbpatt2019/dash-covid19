# -*- coding: utf-8 -*-
"""Dash app creation following Flask Application Factory methods

As Dash apps are, under the hood, Flask apps, it should be best practice to follow
established Flask recommendations, where possible. One of these is the factory method,
where necessary components are defined in submodule and linked to the app in a
create_app function. This has several advantages, including modular structure and
making the entry point script very clean.

Attributes
----------
data : pd.DataFrame
    The data to be plotted and displayed throughout the app. Collated by
    Our World in Data

    .. _

location : pd.DataFrame
    A data frame containing the latitude and longitude of the included countries.

    This is necessary for scatter_mapbox.

columns : List[str]
    Those columns taht are to be available for selection in the app.

    Here, the columns encoding date, iso code, country, continent, latitude,
    and longitude are excluded as it does not make sense to visualise these on
    the included plots (scatter and world map)
"""
from typing import Tuple

import dash
import dash_bootstrap_components as dbc
import flask
import pandas as pd

from dash_covid19.callbacks import init_callbacks
from dash_covid19.layouts import init_layouts

# Make sure data is global, as is needed by layouts
data = pd.read_csv(
    "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
)
data = data[~data.location.isin(["International", "World"])]

# Add lat/lon data
location = pd.read_csv("data/iso_lat_lon.csv")
data = pd.merge(data, location, how="left", on="iso_code", sort=False, validate="m:1")

# And sort by date
data = data.sort_values(by="date")

columns = data.columns[4:-2]


def create_app() -> Tuple[dash.dash.Dash, flask.app.Flask]:
    """Initialise the dash app

    This function is designed to be called in the wsgi entry point script to create
    the Dash app.

    Parameters
    ----------
    None

    Returns
    -------
    Tuple[dash.dash.Dash, flask.app.Flask]
        Containing two objects:

        app : dash.dash.Dash
            The created Dash app
        server : flask.app.Flask
            The Flask instance associated with the Dash app"""

    # Create app
    app = dash.Dash(
        __name__,
        external_stylesheets=[dbc.themes.SANDSTONE, "./assets/stylesheet.css"],
        suppress_callback_exceptions=True,
    )

    # Now that app is created, import callbacks and layouts
    app, layouts = init_layouts(app, data, columns)
    init_callbacks(app, layouts, data)

    # Create server instance
    server = app.server

    return app, server
