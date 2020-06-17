# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc


def log_axis_btn_grp(id="log-axis-btn-grp"):
    """Helper function to create a button grp for scaling axes

    :param id: str, ID of button group. Must be unique across app
        :note: The children buttons inherit from this, with + -log and + -linear

    :returns grp: dbc.ButtonGroup, containing two dbc.Buttons, linear and log"""

    grp = dbc.ButtonGroup(
        id=id,
        children=[
            dbc.Button("Linear", id=id + "-linear"),
            dbc.Button("Log", id=id + "-log"),
        ],
    )
    return grp
