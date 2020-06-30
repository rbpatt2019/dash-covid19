# -*- coding: utf-8 -*-
"""Module: LED

This module contains a helper function for automating the process of creating an LED_
to display numeric data with an html.H5_ header tied to a dbc.Tooltip_ helper

.. _LED:
    https://dash.plotly.com/dash-daq/leddisplay

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


def make_led(
    id: str = "display", variable: str = "New Cases per Million"
) -> List[dash.development.base_component.ComponentMeta]:
    """Generate an LED display for numeric data tied to a header with a helper

    Notes
    -----
        This function returns a list, and is designed to be passed directly to the
        children argument of a Dash Component

    Parameters
    ----------
    id : str
        Component ID. Must be unique across app
    variable : str
        Axis this switch effects. Used to create help message

    Returns
    -------
    List[dash.development.base_component.ComponentMeta]
        List of the header, helper, and LED components

    Example
    -------
    >>> layout = dbc.Col(children=make_led())

    """
    header = html.H5(
        f"{variable}",
        id=id + "-head",
        style={"textDecoration": "underline", "cursor": "pointer",},
    )
    help = dbc.Tooltip(
        f"Current {variable} for selected country",
        id=id + "-help",
        target=id + "-head",
    )
    led = daq.LEDDisplay(id=id)
    return [header, help, led]
