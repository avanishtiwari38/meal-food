import os

from flask import Flask
from flask_restful import Api
from flask import Blueprint

# flask app config
flask_app = Flask(__name__, instance_relative_config=True)


api_bp = Blueprint('api', __name__)
api = Api(api_bp)

flask_app.register_blueprint(api_bp, url_prefix='/api')

# initialise blueprints
api.init_app(api_bp)

basedir = os.path.join(flask_app.root_path)

# delibrately added in the end to avoid circular dependencies
from app import urls