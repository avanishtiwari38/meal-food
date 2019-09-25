from flask_restful import Resource, reqparse
from flask import request, jsonify, abort, redirect

from app import flask_app
from app import api
		

class Meals(Resource):
	"""docstring for Urlapi"""
	def post(self):
		try:
			request_data = request.get_json()
			meal_data = request_data['MEAL_DATA']
			food_ids  = request_data['food_ids']

			lst = []
			if not meal_data or not food_ids:
				response = jsonify(msg="Meal or food data missing(cannot be blank)", status=400)
				response.status_code = 400
				return response

			for y in meal_data:
				food =[z['food_id'] for z in y['foods']]
				if all(item in food for item in food_ids):
					lst.append(y['meal_id'])

			response = lst
			if response:
				return jsonify(data=response, status=200)
			else:
				response = jsonify(msg="No matching data found", status=400)
				response.status_code = 400
				return response
		except KeyError as e:
			return jsonify(status=400, msg="key %s is missing" % str(e))
		except Exception as e:
			return jsonify(status=400, msg=str(e))
