# -*- coding: utf-8 -*-
import pandas as pd
from dash import Dash


def create_app():
    """Initialise the dash app"""

    # Read in data
    data = pd.read_csv(
        "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    )

    # Create app
    app = Dash(
        __name__,
        external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"],
        suppress_callback_exceptions=True,
    )

    # Now that app is created, import callbacks and layouts
    from dash_covid19.layouts import layouts

    app.layout = layouts["app"]

    import dash_covid19.callbacks

    # Create server instance
    server = app.server

    return app, server
