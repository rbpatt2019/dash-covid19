# -*- coding: utf-8 -*-
import dash
from dash import Dash
from dash.testing.application_runners import import_app

from dash_covid19 import data
from dash_covid19.layouts import init_layouts


def test_dcly001_init_layout(dash_duo):
    app = Dash(__name__)

    app, layouts = init_layouts(app, data)

    assert app.layout == layouts["app"]
    assert type(app) == dash.dash.Dash

    assert list(layouts.keys()) == ["app", "explorer", "data-table"]
