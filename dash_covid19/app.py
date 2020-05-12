# -*- coding: utf-8 -*-
import dash
import dash_html_components as html
import dash_table as table
import pandas as pd

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

data = pd.read_csv(
    "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
)


app.layout = html.Div(
    [
        table.DataTable(
            id="data-table",
            columns=[{"name": i, "id": i, "deletable": True} for i in data.columns],
            data=data.to_dict("records"),
            sort_action="native",
            filter_action="native",
            page_action="native",
            page_current=0,
            page_size=25,
        ),
    ]
)


if __name__ == "__main__":
    app.run_server(debug=True)
