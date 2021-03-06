# -*- coding: utf-8 -*-
"""
Functions for testing the callbacks in the app

A mock app is used to prevent repeatedly downloading the data from OWID
as well as to speed up tests

dash_duo.driver.maximize_window() is necessary for accessing the dropdown
Otherwise, selenium cannot click on it.
"""
from time import sleep

import dash


def test_dccb001_data_table(dash_duo, mock_app):
    """Test that navigating to data table opens expected page"""
    dash_duo.start_server(mock_app)
    dash_duo.driver.maximize_window()

    # Check defaults to home
    dash_duo.wait_for_element_by_id("exp-card")

    # Change to date table...
    dash_duo.click_at_coord_fractions("#nav-bar-dt", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("dt-data")
    dash_duo.percy_snapshot("dccb001-data-table")


def test_dccb002_interactive_scatter(dash_duo, mock_app):
    """Test that navigating to scatter plot opens expected page
    and that the callbacks are triggered appropriately"""
    dash_duo.start_server(mock_app)
    dash_duo.driver.maximize_window()

    # Check defaults to home
    dash_duo.wait_for_element_by_id("exp-card")
    dash_duo.click_at_coord_fractions("#nav-bar-exp", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("exp-main-scatter")

    # Interact with all the things!
    dash_duo.click_at_coord_fractions("#exp-scale-x", 0.5, 0.5)
    dash_duo.click_at_coord_fractions("#exp-scale-y", 0.5, 0.5)
    dash_duo.click_at_coord_fractions("#exp-main-slider", 0.5, 0.1)
    dash_duo.select_dcc_dropdown("#exp-dd-x", index=1)
    dash_duo.select_dcc_dropdown("#exp-dd-y", index=2)

    # And confirm
    dash_duo.percy_snapshot("dccb002-scatter")


def test_dccb003_interactive_map(dash_duo, mock_app):
    """Test that navigating to map opens expected page
    and that the callbacks are triggered appropriately"""
    dash_duo.start_server(mock_app)
    dash_duo.driver.maximize_window()

    # Check defaults to home
    dash_duo.wait_for_element_by_id("exp-card")
    dash_duo.click_at_coord_fractions("#nav-bar-map", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("map-scatter")

    # Interact with all the things!
    dash_duo.click_at_coord_fractions("#map-slider", 0.5, 0.1)
    dash_duo.select_dcc_dropdown("#map-size-dd", index=1)
    dash_duo.select_dcc_dropdown("#map-color-dd", index=2)

    # And confirm
    # This never seems to load in time, so adding explicit wait
    sleep(1)
    dash_duo.percy_snapshot("dccb003-map")


def test_dccb004_overview_leds(dash_duo, mock_app):
    """Test that navigating to Overviews opens expected page
    and that the callbacks are triggered appropriately"""
    dash_duo.start_server(mock_app)
    dash_duo.driver.maximize_window()

    # Check defaults to home
    dash_duo.wait_for_element_by_id("exp-card")
    dash_duo.click_at_coord_fractions("#nav-bar-ovw", 0.5, 0.5)
    dash_duo.wait_for_element_by_id("ovw-ncpm")

    # Interact with all the things!
    dash_duo.select_dcc_dropdown("#ovw-dd", index=1)

    # And confirm
    # This never seems to load in time, so adding explicit wait
    dash_duo.percy_snapshot("dccb004-ovw")
