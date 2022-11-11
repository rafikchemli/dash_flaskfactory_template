from flask import Flask
from waitress import serve
from config import Config, basedir
from flask_crontab import Crontab
import os

# extensions
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap()
crontab = Crontab()
 # setup env #

os.chdir(basedir)


def create_app(config_class=Config):
    print('step 1 create app')
    app = Flask(__name__)
    crontab.init_app(app)
    # configuration
    app.config.from_object(config_class)
    # register extensions
    bootstrap.init_app(app)

   



    with app.app_context():
        # register blueprints
        from app.main import bp as bp_main
        app.register_blueprint(bp_main)
        from app.dashapps import bp as bp_dashapps
        app.register_blueprint(bp_dashapps)
        # from app.auth import bp as bp_auth
        # app.register_blueprint(bp.auth)


        # process dash apps
        # dash app 1

        # @crontab.job(minute="*", hour="*")
        def scheduledApp(app):
            os.system("lsof -ti tcp: | xargs kill -9")

            from app.dashapps.dash_app_1 import add_dash as ad1
            app = ad1(app)
            # dash app 2
            from app.dashapps.dash_app_example import add_dash as ad2
            app = ad2(app)

            from app.dashapps.dash_app_3 import add_dash as ad3
            app = ad3(app)

            from app.dashapps.dash_app_4 import add_dash as ad4
            app = ad4(app)

            from app.main.dash_app_homepage import add_dash as adhome
            app = adhome(app)

            from app.main.dash_app_contacts import add_dash as adcontact
            app = adcontact(app)


            return app
        
        app = scheduledApp(app)
        return app

# if __name__ == "__main__":
#     serve(app.server,debug=True, port=8059)




