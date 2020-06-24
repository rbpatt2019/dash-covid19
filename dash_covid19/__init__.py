# -*- coding: utf-8 -*-
import os

import dash_bootstrap_components as dbc
import pandas as pd
from dash import Dash
from flask_caching import Cache

from dash_covid19.callbacks import init_callbacks
from dash_covid19.layouts import init_layouts

# Make sure data is global, as is needed by layouts
data = pd.read_csv(
    "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
)
data = data[~data.location.isin(["International", "World"])].sort_values(by="date")

columns = data.columns[4:]
date_idx = range(len(data.date.unique()))


def create_app(data=data, columns=columns, date_idx=date_idx):
    """Initialise the dash app"""

    # Create app
    app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.SANDSTONE, "./assets/stylesheet.css"],
        suppress_callback_exceptions=True,
    )

    # Now that app is created, import callbacks and layouts
    app, layouts = init_layouts(app, data, columns, date_idx)
    init_callbacks(app, layouts, data)

    # Create server instance
    server = app.server

    # And add caching
    cache = Cache(
        server,
        config={
            "CACHE_TYPE": "redis",
            "CACHE_REDIS_URL": os.environ.get("REDIS_URL", ""),
        },
    )

    return app, server, cache
