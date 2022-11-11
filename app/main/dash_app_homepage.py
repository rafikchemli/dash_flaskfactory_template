
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from waitress import serve
import dash_auth
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




# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])

# VALID_USERNAME_PASSWORD_PAIRS = {
# 'admin': 'password'
# }
# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
#     )


APP_ID = 'dash_app_homepage'
URL_BASE = '/dash/dash_app_homepage/'
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




    first_card = dbc.Card(
        dbc.CardBody(
            [
                html.H5("", className="card-title"),
                html.P("Analysis and tools for optimisation of Viral lysis buffer"),
                dbc.Button("Go to project", color="primary", href='http://server:/dash/dash_app_1/'),
            ]
        )
    )



    second_card = dbc.Card(
        dbc.CardBody(
            [
                html.H5("cfDNA Extraction", className="card-title"),
                html.P(
                    "Optimization of cfDNA extraction"
                ),
                dbc.Button("Go to project", color="primary", href='http://server:/dash/dash_app_2/'),
            ]
        )
    )


    third_card = dbc.Card(
        dbc.CardBody(
            [
                html.H5("Placeholder", className="card-title"),
                html.P(
                    "Example project containing example layout"
                ),
                dbc.Button("Go to project", color="primary", href='http://server:/dash/dash_app_3/'),
            ]
        )
    )

    fourth_card = dbc.Card(
        dbc.CardBody(
            [
                html.H5("Pathogen", className="card-title"),
                html.P(
                    "Optimization of Pathogen kit"
                ),
                dbc.Button("Go to project", color="primary", href='http://server:/dash/dash_app_4/'),
            ]
        )
    )    


    Menu = dbc.Container(
                            [
                            dbc.Col([ 
                                dbc.Row([html.H1('Projects')],justify="center", align="center", className="h-10",style= {"top": 10}),
                                # html.Hr(),
                                first_card, 
                                second_card,
                                # third_card,
                                fourth_card,
                                
                                
                                ])
                            
                            ],style={"height": "100vh"} )
                                    # html.Hr(),
                                    # dbc.Row('hello'), fluid=True)


    app.layout=Menu


    return server







