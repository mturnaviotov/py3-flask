from flask import Blueprint

employees_controller = Blueprint('employees_controller', __name__,template_folder='./templates', static_folder='static')

from . import page