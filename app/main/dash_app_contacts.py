

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from waitress import serve
import os

import random
from dash_bootstrap_components._components.CardBody import CardBody
from dash_bootstrap_components._components.CardGroup import CardGroup
from dash_bootstrap_components._components.Popover import Popover
from waitress import serve
import time

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from dash.dependencies import Input, Output
import dash_table
from dash.dependencies import Input, Output
from dash_table.Format import Format, Group, Scheme, Symbol
import glob
import werkzeug.serving
from datetime import datetime

# from sklearn.cluster import KMeans
import threading as Threading
import pickle
# must add this line in order for the app to be deployed successfully on Heroku



# change to app.layout if running as single page app instead
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])

APP_ID = 'dash_app_contacts'
URL_BASE = '/dash/dash_app_contacts/'
MIN_HEIGHT = 2000
# NAME_PROJECT='Project name example'
# PROJECT_DESCRIPTION= "this should be a short description of the project"


def add_dash(server):
    
    external_stylesheets = [
        dbc.themes.BOOTSTRAP,
    ]
    app = dash.Dash(
        server=server,
        url_base_pathname=URL_BASE,
        suppress_callback_exceptions=True,
        external_stylesheets=external_stylesheets,
        meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
    )


    app.layout= html.Div([
        dbc.Container([
            dbc.Row([
                dbc.Col(html.H1(children=''), className="mb-2")
            ]),
            dbc.Row([
                dbc.Col(html.H6(children=' : '), className="mb-4")
            ]),
            dbc.Row([
                dbc.Col(html.H6(children=''), className="mb-4")
            ]),
            dbc.Row([
                dbc.Col(html.H6(children=''), className="mb-4")
            ]),

        ])

        ])
    



    return server







