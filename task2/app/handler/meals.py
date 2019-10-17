from flask_restful import Resource, reqparse
from flask import request, jsonify, abort, redirect

from app import flask_app
from app import api
import sys
sys.path.append('../')
from task1.solution import get_matching_meals
from task1 import meal_data
import json
		

class Meals(Resource):
	"""docstring for Urlapi"""
	def post(self):
		try:
			request_data = request.get_json()
			# meal_data = request_data['MEAL_DATA']
			food_ids  = request_data['food_ids']
			path = '../task1/meal_data.py'

			with open(path) as file:
				data = json.load(file)
				meal_data_data = data

			response = get_matching_meals(meal_data_data, food_ids)
			if isinstance(response, list):
				return jsonify(data=response, status=200)
			else:
				response = jsonify(msg=response, status=400)
				response.status_code = 400
				return response
		except KeyError as e:
			return jsonify(status=400, msg="key %s is missing" % str(e))
		except Exception as e:
			return jsonify(status=400, msg=str(e))
