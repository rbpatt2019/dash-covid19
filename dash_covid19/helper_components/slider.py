# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


def make_slider(
    df,
    slider_id,
    header="Date Slider",
    tooltip="Slide through the dates to see how patterns evolve over time",
):
    date_idx = range(len(df.date.unique()))
    header = html.H5(
        header,
        id=slider_id + "-head",
        className="mt-3",
        style={"textDecoration": "underline", "cursor": "pointer",},
    )
    tooltip = dbc.Tooltip(tooltip, id=slider_id + "-help", target=slider_id + "-head",)
    slider = dcc.Slider(
        id=slider_id,
        min=min(date_idx),
        max=max(date_idx),
        value=max(date_idx),
        marks={
            val: {
                "label": str(date),
                "style": {
                    "writing-mode": "vertical-lr",
                    "transform": "rotate(-45deg)",
                    "transform-origin": "40% 30%",
                    "white-space": "nowrap",
                },
            }
            for val, date in zip(date_idx[::7], df.date.unique()[::7])
        },
    )
    return [header, tooltip, slider]
