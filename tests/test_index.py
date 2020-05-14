# -*- coding: utf-8 -*-
import dash
from dash.testing.application_runners import import_app


def test_dcin001_tab_navigation(dash_duo):
    app = import_app("dash_covid19.index")

    dash_duo.start_server(app)

    # Check defaults to explorer
    # wait to load, assert value, percy
    dash_duo.wait_for_contains_text("#exp-header", "Explorer")
    dash_duo.percy_snapshot("dcin001-graph")

    # # Check change correctly
    # # Click, wait, assert, percy
    dash_duo.click_at_coord_fractions("#nav-tab-2", 0.5, 0.5)
    dash_duo.wait_for_contains_text("#dt-header", "Data Table")
    dash_duo.percy_snapshot("dcin001-data-table")
