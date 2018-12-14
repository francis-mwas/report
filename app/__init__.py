# installing dependancies.
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from instance.config import app_config


"""blueprints"""
from .admin import admin_blueprint as admin_blp
from .auth import auth_blueprint as auth_blp
from .incidents import incident_blueprint as incidents_blp

# module imports
from .incidents.incidents import Post_incidents, Get_specific_incident

from .auth.auth_views import Sign_up, Login

from .admin.admin_views import Incidents, All_users, Get_users_by_email, Get_user_by_id, Get_incident_by_id

# create instance of our application.

jwt = JWTManager()
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    jwt.init_app(app)

    admin = Api(admin_blp)
    app.register_blueprint(admin_blp, url_prefix='/api/v1')

    auth = Api(auth_blp)
    app.register_blueprint(auth_blp, url_prefix='/api/v1')

    incidents = Api(incidents_blp)
    app.register_blueprint(incidents_blp, url_prefix='/api/v1')

    """ admin endpoints """
    """get all users"""
    admin.add_resource(All_users, '/users')
    """get all incidents"""
    admin.add_resource(Incidents, '/incidents')
    """ get user by email """
    admin.add_resource(Get_users_by_email, '/users/<string:email>')
    """ get user by id """
    admin.add_resource(Get_user_by_id, '/users/<int:id>')
    """ update the incident status by id"""
    incidents.add_resource(Get_incident_by_id, '/incidents/<int:id>')

    # auth enpoints.
    """ create account and login"""
    auth.add_resource(Sign_up, '/users')
    auth.add_resource(Login, '/login')

    # incidents endpoints.
    """create incidents"""
    incidents.add_resource(Post_incidents, '/incidents')
    """ user gets incidents by id """
    incidents.add_resource(Get_specific_incident, '/incidents/<int:id>')

    return app
