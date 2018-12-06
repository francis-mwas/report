# installing dependancies.
from flask import Flask
from flask_restful import Api


"""blueprints"""
from .admin import admin_blueprint as admin_blp
from .auth import auth_blueprint as auth_blp
from .incidents import incident_blueprint as incidents_blp

# module imports
from .incidents.incidents import Post_incidents, Get_specific_incident

from .auth.auth_views import Sign_up

from .admin.admin_views import Incidents, All_users, Get_users_by_email, Get_user_by_id, Get_incident_by_id

# create instance of our application.


def create_app():
    app = Flask(__name__)

    admin = Api(admin_blp)
    app.register_blueprint(admin_blp, url_prefix='/api/v1')

    auth = Api(auth_blp)
    app.register_blueprint(auth_blp, url_prefix='/ap1/v1')

    incidents = Api(incidents_blp)
    app.register_blueprint(incidents_blp, url_prefix='/api/v1')



    """ admin endpoints """
    """get all users"""
    admin.add_resource(All_users, '/users')
    """get all incidents"""
    admin.add_resource(Incidents, '/api/v1/incidents')
    """ get user by email """
    admin.add_resource(Get_users_by_email, '/users/<string:email>')
    """ get user by id """
    admin.add_resource(Get_user_by_id, '/users/<int:id>')
    """ update the incident status """ 
    incidents.add_resource(Get_incident_by_id, '/incidents/<int:id>')

    # auth enpoints.
    """ create users """
    auth.add_resource(Sign_up, '/users')


    # incidents endpoints.
    """create incidents"""
    incidents.add_resource(Post_incidents, '/incidents')
    """ user gets incidents by id """
    incidents.add_resource(Get_specific_incident, '/incidents/<int:id>')

    return app
