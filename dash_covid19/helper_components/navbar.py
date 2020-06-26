# -*- coding: utf-8 -*-
"""Helper Component: Simple Navbar

This module contains a predefined Navbar to be used for navigating the Dash App

.. _dbc.NavbarSimple
    https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/

Attributes
----------
navbar: dash.development.base_component.ComponentMeta
    A dbc.NavbarSimple. The brand_href returns you to home, while the other NavItems
    navigate various pages, both internal and external, relevant to the app.

"""
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    id="navbar",
    brand="dash-covid19",
    brand_href="/",
    fluid=True,
    color="secondary",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Explorer", id="nav-bar-exp", href="/exp")),
        dbc.NavItem(dbc.NavLink("World Map", id="nav-bar-map", href="/map")),
        dbc.NavItem(dbc.NavLink("Data", id="nav-bar-dt", href="/dt")),
        dbc.NavItem(
            dbc.NavLink(
                "Code",
                id="nav-bar-code",
                href="https://github.com/rbpatt2019/dash-covid19",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Info",
                id="nav-bar-info",
                href="https://github.com/owid/covid-19-data/tree/master/public/data",
            )
        ),
    ],
)
