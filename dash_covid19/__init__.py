# -*- coding: utf-8 -*-
import pandas as pd
from dash import Dash

from dash_covid19.callbacks import init_callbacks
from dash_covid19.layouts import init_layouts

# Make sure data is global, as is needed by layouts
data = pd.read_csv(
    "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
)
data["date"] = pd.to_datetime(data["date"])
data = data.fillna(0)


def create_app():
    """Initialise the dash app"""

    # Create app
    app = Dash(
        __name__,
        external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"],
        suppress_callback_exceptions=True,
    )

    # Now that app is created, import callbacks and layouts
    app, layouts = init_layouts(app, data)
    init_callbacks(app, layouts)

    # Create server instance
    server = app.server

    return app, server
