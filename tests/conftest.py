# -*- coding: utf-8 -*-
import pytest
import dash
from dash_covid19 import create_app
from selenium.webdriver.chrome.options import Options


def pytest_setup_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return options


@pytest.fixture()
def mock_app() -> dash.dash.Dash:
    """Create a test app using mocked data"""
    app, _ = create_app(testing=True)
    return app
