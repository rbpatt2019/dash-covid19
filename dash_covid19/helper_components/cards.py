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


exp_card = link_card(
    id="exp-card",
    title="Explorer",
    text="Explore correlations within the data and how they evolve over time using "
    "interactive scatter plots",
    href="/exp",
)

dt_card = link_card(
    id="dt-card",
    title="Data",
    text="View the raw data to develop a deeper undestanding of the numberrs in "
    "the graphs",
    href="/dt",
)

code_card = link_card(
    id="code-card",
    title="Code",
    text="This project is proudly open source, so you can view the code yourself. "
    "Feel free to report any bugs or improvements!",
    href="https://github.com/rbpatt2019/dash-covid19",
)

info_card = link_card(
    id="info-card",
    title="Info",
    text="Learn more about the data, including its source, units, and how it was "
    "collated by the wonderful people of OWID",
    href="https://github.com/owid/covid-19-data/tree/master/public/data",
)
