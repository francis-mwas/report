from flask import Flask
from flask_restful import Resource, reqparse
from models.models import User, Users, Incident, incidents


class Incidents(Resource):
    def get(self):
            return {"Incidents": [incident.serializer() for incident in incidents]}


class Get_incident_by_id(Resource):
    def get(self, id):
        incident = Incident().get_incident_by_id(id)
        if not incident:
            return {"Message": "incident does not exit"}
        else:
            return {"Incident": incident.serializer()}





class All_users(Resource):
    def get(self):
        return {"Users": [user.serialize() for user in Users]}


class Get_users_by_email(Resource):
    def get(self, email):

        user = User().get_user_by_email(email)
        if user:
               return {"User": user.serialize()}

class Get_user_by_id(Resource):
    def get(self, id):
        user = User().get_user_by_id(id)
        if not user:
            return{"User does not exist"}
        else:
            return {"User": user.serialize()}


    
    
       

       
       
