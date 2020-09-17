# -*- coding: utf-8 -*-
"""Module: Graphs

This module contains a helper function for outputting a plotly line graph_ for use in
a Dash interactive callback_

.. _graph:
    https://plotly.com/python/line-charts/

.. _callback:
    https://dash.plotly.com/basic-callbacks

"""
from typing import Any, Dict

import pandas as pd


def line_plot(
    df: pd.DataFrame,
    variable: str = "total_cases",
    title: str = "<b>China</b>",
    scale: bool = False,
) -> Dict[str, Any]:
    """Helper function for creating line plots in a Dash Callback

    Notes
    -----
        This function returns a dictionary of Plotly settings, and is designed to
        be returned from a Dash Callback that outputs to a dcc.Graph figure

    Parameters
    ----------
    df : pd.DataFrame
        Containing the data to be plotted. As the x-axis is time,
        there must be a 'date' column
    variable : str
        Variable to be plotted on y-axis. Must be in df.columns
    title : str
        Text to be used for plot title

    Returns
    -------
    Dict[str, Any]
        A dictionary containing Plotly settings

    Raises
    ------
    AttributeError
        If 'data' or variable not in df.columns

    Examples
    --------
    >>> settings = line_plot(pd.DataFrame([['2020-06-26', 1], ['2020-06-25', 10]], columns=['date', 'total_cases']))

    """
    return {
        "data": [dict(x=df["date"], y=df[variable], mode="lines",)],
        "layout": dict(
            annotations=[
                {
                    "x": 0,
                    "y": 1,
                    "yanchor": "bottom",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "text": title,
                }
            ],
            margin=dict(r=0, l=60, t=20, b=50, pad=0, autoexpand=False),
            xaxis={"title": "Date"},
            yaxis={
                "title": variable.capitalize(),
                "type": "log" if scale else "linear",
            },
            hovermode="closest",
        ),
    }
