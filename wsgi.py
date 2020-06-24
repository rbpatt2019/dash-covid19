# -*- coding: utf-8 -*-
from dash_covid19 import create_app

app, server = create_app()

if __name__ == "__main__":
    app.run_server(debug=True)
