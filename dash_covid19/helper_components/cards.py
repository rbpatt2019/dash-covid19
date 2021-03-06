# -*- coding: utf-8 -*-
"""Module: Cards

A frequently occuring use of the dash_bootstrap_components card_ is to provide a
description and a link. This module provides a helper function to automate this
case.

.. _card: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/

"""
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


def link_card(
    uid: str = "link-card",
    title: str = "A Card!",
    text: str = "This is interesting!",
    href: str = "/somewhere",
) -> dash.development.base_component.ComponentMeta:
    """Helper function for making a dbc card with a link button

    Parameters
    ----------
    uid : str
        Card identifier, must be unique across app
    title : str
        Card title
    text : str
        Body text for card
    href : str
        Link for button. Can be relative or absolute

    Returns
    -------
    dash.development.base_component.ComponentMeta
        Contains a title, body text, and a button serving as a hyperlink

    Examples
    --------
    >>> example_card = link_card(uid='exp-card', title='Example Card', text='Have you been to my github?', href='https://github.com/rbpatt2019')

    """

    return dbc.Card(
        id=uid,
        body=True,
        outline=False,
        color="secondary",
        inverse=True,
        style={"height": "100%"},
        children=[
            html.H4(title, className="card-title", style={"text-align": "center"}),
            html.P(text, className="card-text", style={"text-align": "center"}),
            dbc.Button(
                "Let's go!", id=uid + "-button", href=href, block=True, color="primary",
            ),
        ],
    )
