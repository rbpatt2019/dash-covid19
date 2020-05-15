# -*- coding: utf-8 -*-
import dash
from dash.testing.application_runners import import_app
from dash_covid19.layouts import init_layouts
from tests.mock_app import mock_data


def test_dcly001_init_layout(dash_duo):
    app = import_app("tests.mock_app")
    df = mock_data()

    app, layouts = init_layouts(app, df)

    assert app.layout == layouts["app"]
    assert type(app) == dash.dash.Dash

    assert list(layouts.keys()) == ["app", "data-table", "explorer"]
