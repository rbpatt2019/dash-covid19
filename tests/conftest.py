# -*- coding: utf-8 -*-
from datetime import date as date
from random import sample

import mimesis
import pandas as pd
import pytest
from selenium.webdriver.chrome.options import Options
from dash_covid19 import create_app


def pytest_setup_options():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return options


@pytest.fixture(scope="function")
def mock_app():
    """Use mimesis to create a fake dataset
    Then use that data to create a fake app

    This way, it doesn't call the real data (huge timesaver)
    And only creates the app once per test session

    It is hard coded to match the necessary columns for the app
    It will smaple form the first date in the dataset (2019-12-31) to today
    """

    g = mimesis.Generic("en", seed=0)

    dates = g.datetime.bulk_create_datetimes(date(2019, 12, 30), date.today(), days=1)
    dates.extend(dates)

    locations = [g.address.country(allow_random=True) for _ in range(len(dates))]
    continents = [g.address.continent() for _ in range(len(dates))]

    var = [g.random.uniform(0, 100000) for _ in range(len(dates))]
    var_2 = sample(var, len(var))
    var_3 = sample(var, len(var))

    lat = [g.address.latitude() for _ in range(len(dates))]
    lon = [g.address.longitude() for _ in range(len(dates))]

    m_data = pd.DataFrame(
        zip(dates, locations, continents, var, var_2, var_3, lat, lon),
        columns=[
            "date",
            "location",
            "continent",
            "var_1",
            "var_2",
            "var_3",
            "lat",
            "lon",
        ],
    )

    app, _ = create_app(df=m_data, cols=m_data.columns[3:-2],)
    return app
