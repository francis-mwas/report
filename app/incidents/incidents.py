from flask_restful import Resource, reqparse
from models.models import Incident, incidents, User, Users

from utils import validators

class Post_incidents(Resource):

    parsing = reqparse.RequestParser(bundle_errors=True)

    parsing.add_argument("created_by",type=str ,required=True)
    parsing.add_argument("Type", type=str, required=True)
    parsing.add_argument("location", type=str, required=True)
    parsing.add_argument("status", type=str, required=True)
    parsing.add_argument("image", type=str, required=True)
    parsing.add_argument("comment", type=str, required=True)

    def post(self):
        data = Post_incidents.parsing.parse_args()

        created_by = data['created_by']
        Type = data['Type']
        location = data['location']
        status = data['status']
        image = data['image']
        comment = data['comment']

        validate = validators.Validation()

        if not validate.validate_input_strings(created_by):
            return {"Message": "Please enter valid name"}, 400
        if not validate.validate_input_strings(Type):
            return {"Message": "Please enter valid type"}, 400
        # if not validate.validate_input_strings(location):
        #     return {"Message": "Enter valid location"}, 400
        if not validate.validate_input_strings(status):
            return {"Message": "Enter valid status"}, 400
        if not validate.validate_input_strings(comment):
            return {"Message": "Enter comment correctly"}, 400
        if status !='draft':
            return {"Message": "status must be equal to draft by default"}, 400
        

        incident = Incident(created_by, Type, location, status,
                            image, comment)

        print(f"{incident.Type}")

        incidents.append(incident)

        return {"incidents": "Incident created successfully"}, 201


class Get_specific_incident(Resource):

    parsing = reqparse.RequestParser()
    parsing.add_argument("created_by", type=str,
                         required=True, help="This field is required")
    parsing.add_argument("Type", type=str, required=True,
                         help="This field is required")
    parsing.add_argument("location", type=str, required=True,
                         help="This field is required")
    parsing.add_argument("status", type=str, required=True,
                         help="This field is required")
    parsing.add_argument("image", type=str, required=True,
                         help="This field is required")
    parsing.add_argument("comment", type=str, required=True,
                         help="This field is required")


    """ get specific incident """
    def get(self, id):
        incident = Incident().get_incident_by_id(id)
        if not incident:
            return {"Message": "incident does not exit"}
        else:
            return {"Incident": incident.serializer()}


    """ deleting specific incident """
    def delete(self, id):
        delete_incident = Incident().get_incident_by_id(id)
        if not delete_incident:
            return {"message": "incident does not exist"}, 404
        else:
            incidents.remove(delete_incident)
            return {"Message":"Incident deleted successfully"}, 200
    """ updating specific incident """
    def patch(self, id):
   
        data = Get_specific_incident.parsing.parse_args()

        created_by = data['created_by']
        Type = data['Type']
        location = data['location']
        status = data['status']
        image = data['image']
        comment = data['comment']

        specific_incident = Incident().get_incident_by_id(id)
       

        if not specific_incident:
            return {"message": "This incident does not exist"}, 404
        else:
            specific_incident.created_by = created_by
            specific_incident.Type = Type
            specific_incident.location = location
            specific_incident.status = status
            specific_incident.image = image
            specific_incident.comment = comment

            return {"Incident": specific_incident.serializer()}, 200




   
