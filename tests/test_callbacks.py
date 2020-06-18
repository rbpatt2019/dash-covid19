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
    dash_duo.driver.maximize_window()

    # Check defaults to explorer
    dash_duo.wait_for_element_by_id("exp-main-scatter")

    # Change to date table...
    dash_duo.click_at_coord_fractions("#nav-bar-dt", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("dt-data")
    dash_duo.percy_snapshot("dccb001-data-table")

    # Check change correctly
    dash_duo.click_at_coord_fractions("#nav-bar-exp", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("exp-main-scatter")
    dash_duo.percy_snapshot("dccb001-graph")


def test_dccb002_dropdown(dash_duo):
    app = import_app("wsgi")

    dash_duo.start_server(app)
    dash_duo.driver.maximize_window()

    # Wait for graph to prevent image "jumping"
    dash_duo.wait_for_element_by_id("exp-main-scatter")

    # Interact with all the things!
    dash_duo.select_dcc_dropdown("#exp-dd-x", index=3)
    dash_duo.select_dcc_dropdown("#exp-dd-y", index=9)
    dash_duo.click_at_coord_fractions("#exp-scale-x", 0.5, 0.5)
    dash_duo.click_at_coord_fractions("#exp-scale-y", 0.5, 0.5)
    dash_duo.click_at_coord_fractions("#exp-main-slider", 0.5, 0.1)

    # And confirm
    # Using wait_for here doesn't seem to catch data loading, so add short sleep instead
    sleep(2)
    dash_duo.percy_snapshot("dccb002-graph")
