# -*- coding: utf-8 -*-
import pandas as pd
from dash import Dash

app = Dash(__name__)


def mock_data():
    """Create a mock dataframe for testing"""
    data = {"date": ["2020-03-01", "2020-03-02"], "number": [1, 2]}
    df = pd.DataFrame(data=data)
    return df
