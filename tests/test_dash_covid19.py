# -*- coding: utf-8 -*-
import dash
from dash.testing.application_runners import import_app


def test_dcap001_table_pagination(dash_duo):
    app = import_app("dash_covid19.app")

    dash_duo.start_server(app)

    # Check table loads
    # Elect not to use percy here as data will change daily...
    # As all other features are implemented natively, elect not to test
    dash_duo.wait_for_element_by_id("data-table", timeout=10)
