# -*- coding: utf-8 -*-
"""Helper Component: Simple Navbar

This module contains a predefined Navbar_ to be used for navigating the Dash App

.. _Navbar:
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
    color="primary",
    dark=True,
    children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem(
                    "Code", href="https://github.com/rbpatt2019/dash-covid19"
                ),
                dbc.DropdownMenuItem(
                    "Docs", href="https://dash-covid19.readthedocs.io/en/latest/"
                ),
                dbc.DropdownMenuItem(
                    "OWID",
                    href="https://github.com/owid/covid-19-data/tree/master/public/data",
                ),
            ],
            id="nab-bar-dd",
            nav=True,
            in_navbar=True,
            label="External",
        ),
        dbc.NavItem(dbc.NavLink("Overview", id="nav-bar-ovw", href="/ovw")),
        dbc.NavItem(dbc.NavLink("Explorer", id="nav-bar-exp", href="/exp")),
        dbc.NavItem(dbc.NavLink("World Map", id="nav-bar-map", href="/map")),
        dbc.NavItem(dbc.NavLink("Data", id="nav-bar-dt", href="/dt")),
        dbc.NavItem(dbc.NavLink("Pivot Table", id="nav-bar-pvt", href="/pvt")),
    ],
)
