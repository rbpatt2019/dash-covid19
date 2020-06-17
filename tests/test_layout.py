# -*- coding: utf-8 -*-
import dash
from dash.testing.application_runners import import_app

from dash_covid19 import data, columns
from dash_covid19.layouts import init_layouts


def test_dcly001_init_layout(dash_duo):
    app = dash.Dash(__name__)

    app, layouts = init_layouts(app, data, columns)

    assert app.layout == layouts["/"]
    assert type(app) == dash.dash.Dash

    assert list(layouts.keys()) == ["/", "/exp", "/dt"]
