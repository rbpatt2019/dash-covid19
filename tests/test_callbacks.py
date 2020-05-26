# -*- coding: utf-8 -*-
import dash
from dash.testing.application_runners import import_app

from dash_covid19 import columns


def test_dccb001_tab_navigation(dash_duo):
    app = import_app("wsgi")

    dash_duo.start_server(app)

    # Check defaults to explorer
    dash_duo.wait_for_element_by_id("exp-world-map")
    dash_duo.percy_snapshot("dcin001-graph")

    # # Check change correctly
    dash_duo.click_at_coord_fractions("#nav-tab-2", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("dt-data")
    dash_duo.percy_snapshot("dcin001-data-table")


def test_dccb002_dropdown(dash_duo):
    app = import_app("wsgi")

    dash_duo.start_server(app)

    dd = dash_duo.wait_for_element_by_id("exp-dd-column")
    assert columns[0] in dd.text
