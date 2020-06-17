# -*- coding: utf-8 -*-
import dash_core_components as dcc


def make_dd(id="dd", placeholder="Select a variable", options=[], default_index=0):
    """Helper function for creating a dcc.Dropdown menu
    :param id: str, Id of components. Must be unique across the app
    :param placeholder: str, What to show before a selection is made
    :param options: list-like, Options for dropwdown

    :returns dd: A dcc.Dropwdown component
    """
    dd = dcc.Dropdown(
        id=id,
        placeholder=placeholder,
        persistence=True,
        persistence_type="session",
        clearable=False,
        options=[{"label": i, "value": i} for i in options],
        value=options[default_index],
    )
    return dd
