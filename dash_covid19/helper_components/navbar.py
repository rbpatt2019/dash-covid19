# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    id="navbar",
    brand="dash-covid19",
    brand_href="https://github.com/rbpatt2019/dash-covid19",
    brand_external_link=True,
    fluid=True,
    color="secondary",
    dark=False,
    children=[
        dbc.NavItem(dbc.NavLink("Explorer", href="/exp")),
        dbc.NavItem(dbc.NavLink("Data Table", href="/dt")),
    ],
)
