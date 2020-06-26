# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_daq as daq
import dash_html_components as html


def make_log_switch(id, axis):
    header = html.H5(
        f"{axis}: Log Scale?",
        id=id + "-head",
        style={"textDecoration": "underline", "cursor": "pointer",},
    )
    help = dbc.Tooltip(
        f"Click to enable a log scale for the {axis}. Click again to return to linear.",
        id=id + "-help",
        target=id + "-head",
    )
    switch = daq.BooleanSwitch(id=id, on=False)
    return [header, help, switch]
