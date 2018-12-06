from flask import Blueprint
from .incidents import Post_incidents

incident_blueprint = Blueprint('incidents', __name__)
