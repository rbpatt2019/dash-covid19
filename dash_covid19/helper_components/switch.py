# -*- coding: utf-8 -*-
"""Helper Function: Make Log Switch

This module contains a helper function for automating the process of creating a switch
to convert an axis scale between linear and log with an html.H5 header tied to a
dbc.Tooltip helper

.. _daq.BooleanSwitch
    https://dash.plotly.com/dash-daq/booleanswitch

.. _html.H5
    https://dash.plotly.com/dash-html-components/h5

.. _dbc.Tooltip
    https://dash-bootstrap-components.opensource.faculty.ai/docs/components/tooltip/

"""
from typing import List

import dash
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_html_components as html


def make_log_switch(
    id: str = "switch", axis: str = "X-axis"
) -> List[dash.development.base_component.ComponentMeta]:
    """Generate a Boolean switch for axis scale tied to a header with a helper

    Notes
    -----
        This function returns a list, and is designed to be passed directly to the
        children argument of a Dash Component

    Parameters
    ----------
    id : str
        Component ID. Must be unique across app
    axis : str
        Axis this switch effects. Used to create help message

    Returns
    -------
    List[dash.development.base_component.ComponentMeta]
        List of the header, helper, and switch components

    Example
    -------
    >>> dbc.Col(children=make_log_switch())

    """
    header = html.H5(
        f"{axis}: Log Scale?",
        id=id + "-head",
        style={"textDecoration": "underline", "cursor": "pointer",},
    )
    help = dbc.Tooltip(
        f"Click to enable a log scale for the {axis}. Click again to return to linear.",
        id=id + "-help",
        target=id + "-head",
    )
    switch = daq.BooleanSwitch(id=id, on=False)
    return [header, help, switch]
