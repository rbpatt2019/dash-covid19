# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    id="navbar",
    brand="dash-covid19",
    brand_href="#",
    fluid=True,
    color="dark",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Explorer", href="/exp")),
        dbc.NavItem(dbc.NavLink("Data Table", href="/dt")),
    ],
)
