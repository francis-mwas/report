from flask import Blueprint
from .auth_views import Sign_up

auth_blueprint = Blueprint('auth',__name__)
