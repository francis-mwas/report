from flask import Blueprint
from .admin_views import Incidents

admin_blueprint = Blueprint('admin',__name__)