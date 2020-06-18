# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    id="navbar",
    brand="dash-covid19",
    brand_href="/",
    fluid=True,
    color="primary",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Explorer", id="nav-bar-exp", href="/exp")),
        dbc.NavItem(dbc.NavLink("Data", id="nav-bar-dt", href="/dt")),
    ],
)
