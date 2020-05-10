# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
from dash.testing.application_runners import import_app
from dash_covid19 import __version__


def test_dcap001_btn_click(dash_duo):
    app = import_app("dash_covid19.app")

    dash_duo.start_server(app)

    # Wait for button to initialise
    btn = dash_duo.wait_for_element_by_css_selector("#click-me")

    # Click it and check output
    btn.click()
    dash_duo.wait_for_text_to_equal("#out", "Clicked: 1")

    # Should increment when clicked multiple times
    btn.click()
    dash_duo.wait_for_text_to_equal("#out", "Clicked: 2")

    assert dash_duo.get_logs() == [], "browser console should contain no error"
    dash_duo.percy_snapshot("dcap001-layout")
