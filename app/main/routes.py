from flask import render_template

from app.main import bp
from app.main import dash_app_homepage as dash_app_homepage_obj
from app.main import dash_app_contacts as dash_app_contacts_obj

import functools
import json
import os

import flask


app = flask.Flask(__name__)



@bp.route("/")
@bp.route("/index")
@bp.route("/homepage")
def dash_app_index():
    # if google_auth.is_logged_in():
    return render_template('dashapps/dash_app.html', dash_url=dash_app_homepage_obj.URL_BASE)
    # return render_template('auth/login.html', dash_url="login")


@bp.route("/contacts")
def dash_app_contacts():
    return render_template('dashapps/dash_app.html', dash_url=dash_app_contacts_obj.URL_BASE)