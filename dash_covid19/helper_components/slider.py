# -*- coding: utf-8 -*-
"""Module: Slider

This module contains a helper function automate the process of creating a dcc.Slider_
with an html.H5_ header tied to a dbc.Tooltip_ helper

.. _dcc.Slider:
    https://dash.plotly.com/dash-core-components/slider

.. _html.H5:
    https://dash.plotly.com/dash-html-components/h5

.. _dbc.Tooltip:
    https://dash-bootstrap-components.opensource.faculty.ai/docs/components/tooltip/

"""
from typing import List

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd


def make_slider(
    df: pd.DataFrame, uid: str = "slider", header: str = "Date Slider",
) -> List[dash.development.base_component.ComponentMeta]:
    """Generate a date slider with a header tied to a tooltip helper

    Dash sliders still struggle with dates. To get around this, the function creates
    an integer index from the unique values of the date columns, and assigns the
    actual dates as labels. As such, any callback using this function needs to convert
    from the index back to the actual date before filtering.

    Notes
    -----
        This function returns a list, and is designed to be passed directly to the
        children argument of a Dash Component

    Parameters
    ----------
    df : pd.DataFrame
        Data containing a 'date' column
    uid : str
        Component ID. Must be unique across app
        Default text for Dropdown
    header : str
        Component header

    Returns
    -------
    List[dash.development.base_component.ComponentMeta]
        List of the header, helper, and slider components

    Raises
    ------
    AttributeError
        If there is no column 'data' in df

    Example
    -------
    >>> layout = dbc.Col(children=make_slider(pd.DataFrame([['2020-06-26', 1], ['2020-06-25', 10]], columns=['date', 'var'])))

    """
    date_idx = range(len(df.date.unique()))
    header = html.H5(
        header,
        id=uid + "-head",
        className="mt-3",
        style={"textDecoration": "underline", "cursor": "pointer",},
    )
    tooltip = dbc.Tooltip(
        "Slide through the dates to see how patterns evolve over time",
        id=uid + "-help",
        target=uid + "-head",
    )
    slider = dcc.Slider(
        id=uid,
        min=min(date_idx),
        max=max(date_idx),
        value=max(date_idx),
        marks={
            val: {
                "label": str(date),
                "style": {
                    "writing-mode": "vertical-lr",
                    "transform": "rotate(-45deg)",
                    "transform-origin": "40% 30%",
                    "white-space": "nowrap",
                },
            }
            for val, date in zip(date_idx[::7], df.date.unique()[::7])
        },
    )
    return [header, tooltip, slider]
