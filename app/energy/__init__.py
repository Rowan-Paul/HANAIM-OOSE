from flask import Blueprint
bp = Blueprint('energy', __name__)
from . import routes
