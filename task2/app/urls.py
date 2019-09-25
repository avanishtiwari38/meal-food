from app.handler.meals import Meals
from app import api


api.add_resource(Meals, '/get_matching_meals')
# api.add_resource(Urlapi, '/create')