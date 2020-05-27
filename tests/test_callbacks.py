# -*- coding: utf-8 -*-
from time import sleep

import dash
from dash.testing.application_runners import import_app
from selenium.webdriver.common.keys import Keys

from dash_covid19 import columns


"""
dash_duo.driver.maximize_window() is necessary for accessing the dropdown
Otherwise, selenium cannot click on it.
"""


def test_dccb001_tab_navigation(dash_duo):
    app = import_app("wsgi")

    dash_duo.start_server(app)

    # Check defaults to explorer
    dash_duo.wait_for_element_by_id("exp-world-map")
    dash_duo.percy_snapshot("dccb001-graph")

    # # Check change correctly
    dash_duo.click_at_coord_fractions("#nav-tab-2", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("dt-data")
    dash_duo.percy_snapshot("dccb001-data-table")


def test_dccb002_dropdown(dash_duo):
    app = import_app("wsgi")

    dash_duo.start_server(app)

    dash_duo.wait_for_text_to_equal("#exp-dd-column", f"{columns[0]}")
    dash_duo.select_dcc_dropdown("#exp-dd-column", index=5)
    dash_duo.percy_snapshot("dccb002-graph")
