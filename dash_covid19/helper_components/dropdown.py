# -*- coding: utf-8 -*-
"""Module: Dropdown

This function automates the process of creating dcc.Dropdown_ with an
html.H5_ header and a dbc.Tooltip_ tied to the header.

.. _dcc.Dropdown:
    https://dash.plotly.com/dash-core-components/dropdown

.. _html.H5:
    https://dash.plotly.com/dash-html-components/h5

.. _dbc.Tooltip:
    https://dash-bootstrap-components.opensource.faculty.ai/docs/components/tooltip/

"""
from typing import List, Union

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def make_dd(
    uid: str = "dd",
    label: str = "Dropdown Menu",
    placeholder: str = "Select a variable",
    options: Union[None, List[str]] = None,
    default_index: int = 0,
) -> List[dash.development.base_component.ComponentMeta]:
    """Generate a Dropdown menu with a header tied to a tooltip

    Notes
    -----
        This function returns a list, and is designed to be passed directly to the
        children argument of a Dash Component

    Parameters
    ----------
    uid : str
        Component ID. Must be unique across app.
    label : str
        Label for Dropdown menu
    placeholder : str
        Default text for Dropdown
    options : Union[None, List[str]]
        Possible selections
    default_index : int
        Which selection to default to

    Returns
    -------
    List[dash.development.base_component.ComponentMeta]
        List of the header, helper, and dropdown components

    Example
    -------
    >>> layout = dbc.Col(children=make_dd())

    """
    if options is None:
        options = ["Default"]

    header = html.H5(
        label,
        id=uid + "-head",
        style={
            "textAlign": "center",
            "textDecoration": "underline",
            "cursor": "pointer",
        },
    )
    info = dbc.Tooltip(
        f"Choose from columns in the dataset which is to be plotted on {label}",
        id=uid + "-help",
        target=uid + "-head",
    )
    dd = dcc.Dropdown(
        id=uid,
        placeholder=placeholder,
        persistence=True,
        persistence_type="session",
        clearable=False,
        options=[{"label": i, "value": i} for i in options],
        value=options[default_index],
    )
    return [header, info, dd]
