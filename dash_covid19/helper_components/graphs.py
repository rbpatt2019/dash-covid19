# -*- coding: utf-8 -*-
def line_plot(df, variable="total_cases", title=f"<b>China</b>", scale=False):
    """Helper function for creating line plots

    :param df: pd.DataFrame containing data to be plotted
    :param variable: str, variable to be plotted on y-axis
    :param title: str, text to be used for plot title

    :returns: dict, formatted for plotting with plotly"""
    return {
        "data": [dict(x=df["date"], y=df[variable], mode="lines",)],
        "layout": dict(
            annotations=[
                {
                    "x": 0,
                    "y": 1,
                    "yanchor": "bottom",
                    "xref": "paper",
                    "yref": "paper",
                    "showarrow": False,
                    "text": title,
                }
            ],
            margin=dict(r=0, l=60, t=20, b=50, pad=0, autoexpand=False),
            xaxis={"title": "Date"},
            yaxis={
                "title": variable.capitalize(),
                "type": "log" if scale else "linear",
            },
            hovermode="closest",
        ),
    }
