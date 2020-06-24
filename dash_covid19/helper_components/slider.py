# -*- coding: utf-8 -*-
import dash_core_components as dcc


def make_slider(df, id):
    date_idx = range(len(df.date.unique()))
    return dcc.Slider(
        id=id,
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
