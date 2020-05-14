# -*- coding: utf-8 -*-

import dash_covid19.callbacks
from dash_covid19.app import app
from dash_covid19.layouts import layouts

app.layout = layouts["app"]

server = app.server

if __name__ == "__main__":
    app.run_server(debug=True)
