# -*- coding: utf-8 -*-
import plotly.express as px
from dash.dependencies import Input, Output


def init_callbacks(dash_app, layouts, data):
    """Initialise dash callbacks"""

    @dash_app.callback(Output("page-content", "children"), [Input("url", "pathname")])
    def display_page(path):
        return layouts.get(path, "/exp")

    @dash_app.callback(
        Output("exp-world-map", "figure"), [Input("exp-dd-column", "value")]
    )
    def update_world_map(value):
        figure = px.scatter_geo(
            data,
            locations="iso_code",
            hover_name="location",
            size=value,
            animation_frame=data[["date"]].astype(str),
            projection="eckert4",
            height=750,
            title=f"World Map: {value}",
        )
        return figure
