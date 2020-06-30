# -*- coding: utf-8 -*-
"""Dash app creation following Flask Application Factory methods

As Dash apps are, under the hood, Flask apps, it should be best practice to follow
established Flask recommendations, where possible. One of these is the factory method,
where necessary components are defined in submodule and linked to the app in a
create_app function. This has several advantages, including modular structure and
making the entry point script very clean.
"""
from typing import List, Tuple

import dash
import dash_bootstrap_components as dbc
import flask
import pandas as pd

from dash_covid19.callbacks import init_callbacks
from dash_covid19.layouts import init_layouts
from dash_covid19.data import init_data


def create_app(testing: bool = False) -> Tuple[dash.dash.Dash, flask.app.Flask]:
    """Initialise the dash app

    This function is designed to be called in the wsgi entry point script to create
    the Dash app.

    Note
    ----
    The option to specify parameters exists solely for testing.
    When called in the entry point, defaults should be used

    Parameters
    ----------
    df : pd.DataFrame
        The data to be used in the app
    cols : List[str]
        The columns that will be selectable

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
        external_stylesheets=[dbc.themes.SPACELAB, "./assets/stylesheet.css"],
        suppress_callback_exceptions=True,
    )

    # Get data
    df, cols = init_data(testing=testing)

    # Now that app is created, import callbacks and layouts
    app, layouts = init_layouts(app, df, cols)
    init_callbacks(app, layouts, df)

    # Create server instance
    server = app.server

    return app, server
