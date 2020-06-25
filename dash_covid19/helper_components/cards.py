# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_html_components as html


def link_card(
    id="link-card", title="A Card!", text="This is interesting!", href="/somewhere"
):
    """Helper function for making a link card

    :param id: str, Card identifier, must be unique across app
    :param title: str, Card title
    :param text: str, Body text for card
    :param href: str, link for button

    :returns: dbc.Card
    """

    return (
        dbc.Card(
            id=id,
            body=True,
            outline=False,
            color="secondary",
            inverse=True,
            style={"height": "100%"},
            children=[
                html.H4(title, className="card-title", style={"text-align": "center"}),
                html.P(text, className="card-text", style={"text-align": "center"}),
                dbc.Button(
                    "Let's go!",
                    id=id + "-button",
                    href=href,
                    block=True,
                    color="primary",
                ),
            ],
        ),
    )
