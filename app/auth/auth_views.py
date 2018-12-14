from flask import Flask
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import datetime

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
    parser.add_argument('password', type=str, required=True)
    parser.add_argument('is_admin', type=bool, required=True)

    def post(self):
        data = Sign_up.parser.parse_args()
        firstname = data['firstname']
        lastname = data['lastname']
        othernames = data['othernames']
        email = data['email']
        phoneNumber = data['phoneNumber']
        username = data['username']
        password  = data['password']
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
                    phoneNumber, username,password, bool(is_admin))
        Users.append(user)

        return {"Message": f"{user.username} created successfully"}, 201

class Login(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="This field cannot be empty, please fill the field")
    parser.add_argument('password', type=str, required=True, help="The password field is required, please fill the field")

    def post(self):
        login_data = Login.parser.parse_args()

        username = login_data['username']
        password = login_data['password']

        validations = validators.Validation()
        if not validations.validate_username(username):
            return {"Message": "username can only contain alphanumeric characters only and a minimum of 4 characters"}, 400
        if not validations.validate_password(password):
            return {"Message": "password field should start with a capital letter"
                    " and include a number"}, 400
        user = User().get_user_by_username(username)
        
        if user and check_password_hash(user.pwhash, password):
            expires = datetime.timedelta(minutes=20)
            access_token = create_access_token(user.username, expires_delta=expires)
            return {'token': access_token, 'message': 'successfully logged in'}, 200
        return {'message': 'user does not exist on this server'}, 404


    

