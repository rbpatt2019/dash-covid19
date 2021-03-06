# -*- coding: utf-8 -*-
"""Module: Switch

This module contains a helper function for automating the process of creating a switch_
to convert an axis scale between linear and log with an html.H5_ header tied to a
dbc.Tooltip_ helper

.. _switch:
    https://dash.plotly.com/dash-daq/booleanswitch

.. _html.H5:
    https://dash.plotly.com/dash-html-components/h5

.. _dbc.Tooltip:
    https://dash-bootstrap-components.opensource.faculty.ai/docs/components/tooltip/

"""
from typing import List

import dash
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_html_components as html


def make_log_switch(
    uid: str = "switch", axis: str = "X-axis"
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
    >>> layout = dbc.Col(children=make_log_switch())

    """
    header = html.H5(
        f"{axis}: Log Scale?",
        id=uid + "-head",
        style={"textDecoration": "underline", "cursor": "pointer",},
    )
    info = dbc.Tooltip(
        f"Click to enable a log scale for the {axis}. Click again to return to linear.",
        id=uid + "-help",
        target=uid + "-head",
    )
    switch = daq.BooleanSwitch(id=uid, on=False)
    return [header, info, switch]
