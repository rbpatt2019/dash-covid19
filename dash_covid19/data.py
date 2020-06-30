# -*- coding: utf-8 -*-
"""Module: Data

To comply with the Flask Application factory layout - as Dash apps are really just
Flask apps under the hood - this function initialises the data for the app.

"""
from typing import List, Tuple

import pandas as pd


def init_data(testing: bool = False) -> Tuple[pd.DataFrame, List[str]]:
    """Initialise data and return default

    This function is called with create_app() to initialise the app data in
    accordance with Flask Application Factory principles.

    Note
    ----
        The parameters exist only for the sake of specifying reduced, mock data during testing
        When called in the wsgi entry point, the defaults should be used

    Parameters
    ----------
    testing : bool
        Whether to use mock data

    Returns
    -------
    Tuple
        Containing two objects:

        data : pd.DataFrame
            The data to be used within the app
        columns : List[str]
            Which columns are to be selectable throughout the app
    """

    if testing:
        data = pd.read_csv("data/testing_data.csv", index_col=0)
        columns = data.columns[3:-2]
    else:
        data = pd.read_csv(
            "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
        )
        data = data[~data.location.isin(["International", "World"])]

        location = pd.read_csv("data/iso_lat_lon.csv")
        data = pd.merge(
            data, location, how="left", on="iso_code", sort=False, validate="m:1"
        )
        data = data.sort_values(by="date")

        columns = data.columns[4:-2]

    return data, columns
