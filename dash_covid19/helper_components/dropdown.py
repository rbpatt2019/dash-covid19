# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def make_dd(id, label, placeholder="Select a variable", options=[], default_index=0):
    header = html.H5(
        label,
        id=id + "-head",
        style={"textDecoration": "underline", "cursor": "pointer",},
    )
    help = dbc.Tooltip(
        f"Choose from columns in the dataset which is to be plotted on {label}",
        id=id + "-help",
        target=id + "-head",
    )
    dd = dcc.Dropdown(
        id=id,
        placeholder=placeholder,
        persistence=True,
        persistence_type="session",
        clearable=False,
        options=[{"label": i, "value": i} for i in options],
        value=options[default_index],
    )
    return [header, help, dd]
