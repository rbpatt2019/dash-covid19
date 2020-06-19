# -*- coding: utf-8 -*-
import dash
from dash.testing.application_runners import import_app

from dash_covid19 import data, columns, date_idx
from dash_covid19.layouts import init_layouts


def test_dcly001_init_layout(mimesis_data):
    app = dash.Dash(__name__)

    app, layouts = init_layouts(
        app,
        mimesis_data,
        mimesis_data.columns[4:],
        range(len(mimesis_data["date"].unique())),
    )

    assert app.layout == layouts["app"]
    assert type(app) == dash.dash.Dash

    assert list(layouts.keys()) == ["app", "/", "/exp", "/dt"]
