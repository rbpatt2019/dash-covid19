# -*- coding: utf-8 -*-
from dash.dependencies import Input, Output


def init_callbacks(dash_app, layouts):
    """Initialise dash callbacks"""

    @dash_app.callback(
        Output("page-content", "children"), [Input("navigation", "value")]
    )
    def display_page(value):
        return layouts[value]
