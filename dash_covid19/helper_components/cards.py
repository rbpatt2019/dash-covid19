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

    return dbc.Card(
        id=id,
        children=dbc.CardBody(
            [
                html.H4(title, className="card-title", style={"text-align": "center"}),
                html.P(text, className="card-text",),
                dbc.Button("Let's go!", id=id + "-button", href=href, block=True),
            ],
        ),
    )


exp_card = link_card(
    id="exp-card",
    title="Explore",
    text="Explore correlations within the data and how they evolve over time using "
    "interactive scatter plots",
    href="/exp",
)

dt_card = link_card(
    id="dt-card",
    title="View",
    text="View the raw data to develop a deeper undestanding of the numberrs in "
    "the graphs",
    href="/dt",
)
