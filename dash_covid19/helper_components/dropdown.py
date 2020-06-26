# -*- coding: utf-8 -*-
"""Helper Function: Make Dropdown Menu

This function automates the process of creating dcc.Dropdown with an
html.H5 header and a dbc.Tooltip tied to the header.

.. _dcc.Dropdown
    link

.. _html.H5
    link

.. _dbc.Tooltip
    link

"""
from typing import List

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def make_dd(
    id: str = "dd",
    label: str = "Dropdown Menu",
    placeholder: str = "Select a variable",
    options: List[str] = ["default"],
    default_index: int = 0,
) -> List[dash.development.base_component.ComponentMeta]:
    """Generate a Dropdown menu with a header tied to a tooltip

    Notes
    -----
        This function returns a list, and is designed to be passed directly to the
        children argument of a Dash Component

    Parameters
    ----------
    id : str
        Component ID. Must be unique across app.
    label : str
        Label for Dropdown menu
    placeholder : str
        Default text for Dropdown
    options : List[str]
        Possible selections
    default_index : int
        Which selection to default to

    Returns
    -------
    List[dash.development.base_component.ComponentMeta]
        List of the header, helper, and dropdown components

    Example
    -------
    >>> dbc.Col(children=make_dd())

    """
    header = html.H5(
        label,
        id=id + "-head",
        style={"textDecoration": "underline", "cursor": "pointer",},
    )
    help = dbc.Tooltip(
        f"Choose from columns in the dataset which is to be plotted on {label}",
        id=id + "-help",
        target=id + "-head",
    )
    dd = dcc.Dropdown(
        id=id,
        placeholder=placeholder,
        persistence=True,
        persistence_type="session",
        clearable=False,
        options=[{"label": i, "value": i} for i in options],
        value=options[default_index],
    )
    return [header, help, dd]
