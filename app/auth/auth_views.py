from flask import Flask
from flask_restful import Resource, reqparse

from models.models import User, Users

from utils import validators


class Sign_up(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('firstname', type=str, required=True)
    parser.add_argument('lastname', type=str, required=True)
    parser.add_argument('othernames', type=str, required=True)
    parser.add_argument('email', type=str, required=True)
    parser.add_argument('phoneNumber', type=str, required=True)
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('is_admin', type=bool, required=True)

    def post(self):
        data = Sign_up.parser.parse_args()
        firstname = data['firstname']
        lastname = data['lastname']
        othernames = data['othernames']
        email = data['email']
        phoneNumber = data['phoneNumber']
        username = data['username']
        is_admin = data['is_admin']

        validate = validators.Validation()
        if not validate.validate_username(username):
            return {"Message": "username can only contain alphanumeric characters only and a minimum of 4 characters"}, 400
        if not validate.validate_phone_number(phoneNumber):
            return {"Message": "please put valid phone number"}, 400
        
        if not validate.validate_input_strings(firstname):
            return {"Message": "Please enter valid firstname"}, 400
        if not validate.validate_input_strings(lastname):
            return {"Message": "Please enter valid lastname"}, 400
        if not validate.validate_input_strings(othernames):
            return {"Message": "Please enter valid names"}, 400
        # if not validate.validate_if_is_admin(is_admin):
        #     return {"Message": "is admin must be either true or false"}, 400
        if User().get_user_by_email(email):
            return {"Message": f"A user with {email} already exists"}, 400
        if User().get_user_by_username(username):
            return {"Message": f"{username} already taken, please try another"}, 400

        user = User(firstname, lastname, othernames, email,
                    phoneNumber, username, bool(is_admin))
        Users.append(user)

        return {"Message": f"{user.username} created successfully"}, 201

