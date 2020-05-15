# -*- coding: utf-8 -*-
import pandas as pd
from dash import Dash

app = Dash(__name__)


def mock_data(nrows=2, ncols=2):
    """Create a mock dataframe for testing"""
    data = {str(i): range(nrows) for i in range(ncols)}
    df = pd.DataFrame(data=data)
    return df
