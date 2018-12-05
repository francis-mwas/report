# installing dependancies.
from flask import Flask
from flask_restful import Api

# module imports
from .incidents.incidents import Post_incidents, Get_specific_incident

from .auth.auth_views import Sign_up

from .admin.admin_views import Incidents, All_users, Get_users_by_email, Get_user_by_id, Get_incident_by_id

# create instance of our application.
def create_app():
    app = Flask(__name__)
    api = Api(app)

    """create incidents"""
    api.add_resource(Post_incidents, '/api/v1/incidents')
    """ create users """
    api.add_resource(Sign_up, '/api/v1/users')
    """get all users"""
    api.add_resource(All_users, '/api/v1/users')
    """get all incidents"""
    api.add_resource(Incidents, '/api/v1/incidents')
    """ get user by email """
    api.add_resource(Get_users_by_email, '/api/v1/users/<string:email>')
    """ get user by id """
    api.add_resource(Get_user_by_id, '/api/v1/users/<int:id>')
    """get incident by id"""
    api.add_resource(Get_incident_by_id, '/api/v1/incidents/<int:id>')
    """ user get incidents by id """
    api.add_resource(Get_specific_incident, '/api/v1/incidents/<int:id>')
    

    return app
