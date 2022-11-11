from flask import Flask, render_template, session, request, redirect, url_for, current_app
from flask_login import current_user, login_required

from app.dashapps import bp
from app.dashapps import dash_app_1 as dash_app_1_obj
from app.dashapps import dash_app_example as dash_app_2_obj
from app.dashapps import dash_app_3 as dash_app_3_obj
from app.dashapps import dash_app_4 as dash_app_4_obj
# from app.dashapps import dash_app_homepage as dash_app_homepage_obj



@bp.route("/dash_app_1")
def dash_app_1():
    return render_template('dashapps/dash_app.html', dash_url=dash_app_1_obj.URL_BASE)


@bp.route("/dash_app_2")
def dash_app_2():
    return render_template('dashapps/dash_app.html', dash_url=dash_app_2_obj.URL_BASE)

@bp.route("/dash_app_3")
def dash_app_3():
    return render_template('dashapps/dash_app.html', dash_url=dash_app_3_obj.URL_BASE)

@bp.route("/dash_app_4")
def dash_app_4():
    return render_template('dashapps/dash_app.html', dash_url=dash_app_4_obj.URL_BASE)






