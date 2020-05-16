# -*- coding: utf-8 -*-
import dash
from dash.testing.application_runners import import_app


def test_dccb001_tab_navigation(dash_duo):
    app = import_app("wsgi")

    dash_duo.start_server(app)

    # Check defaults to explorer
    dash_duo.wait_for_element("exp-world-map")
    dash_duo.percy_snapshot("dcin001-graph")

    # # Check change correctly
    dash_duo.click_at_coord_fractions("#nav-tab-2", 0.5, 0.5)
    dash_duo.wait_for_element("#dt-data")
    dash_duo.percy_snapshot("dcin001-data-table")
