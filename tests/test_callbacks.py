# -*- coding: utf-8 -*-
from time import sleep
import dash


"""
dash_duo.driver.maximize_window() is necessary for accessing the dropdown
Otherwise, selenium cannot click on it.
"""


def test_dccb001_tab_navigation(dash_duo, mock_app):
    dash_duo.start_server(mock_app)
    dash_duo.driver.maximize_window()

    # Check defaults to home
    dash_duo.wait_for_element_by_id("exp-card")

    # Check chage to graph
    dash_duo.click_at_coord_fractions("#nav-bar-exp", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("exp-main-scatter")
    dash_duo.percy_snapshot("dccb001-graph")

    # Change to date table...
    dash_duo.click_at_coord_fractions("#nav-bar-dt", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("dt-data")
    dash_duo.percy_snapshot("dccb001-data-table")


def test_dccb002_interactive_graph(dash_duo, mock_app):
    dash_duo.start_server(mock_app)
    dash_duo.driver.maximize_window()

    # Wait for graph to prevent image "jumping"
    dash_duo.wait_for_element_by_id("nav-bar-exp")
    dash_duo.click_at_coord_fractions("#nav-bar-exp", 0.5, 0.5)

    # Interact with all the things!
    dash_duo.click_at_coord_fractions("#exp-scale-x", 0.5, 0.5)
    dash_duo.click_at_coord_fractions("#exp-scale-y", 0.5, 0.5)
    dash_duo.click_at_coord_fractions("#exp-main-slider", 0.5, 0.1)
    dash_duo.select_dcc_dropdown("#exp-dd-x", index=1)
    dash_duo.select_dcc_dropdown("#exp-dd-y", index=2)

    # And confirm
    dash_duo.percy_snapshot("dccb002-graph")
