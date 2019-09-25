import argparse
import json

def get_matching_meals(meal_data, food_ids):
	try:
		lst = []
		if not meal_data or not food_ids:
			response = "Meal or food data missing(cannot be blank)"
			return response

		for y in meal_data:
			food =[z['food_id'] for z in y['foods']]
			if all(item in food for item in food_ids):
				lst.append(y['meal_id'])

		response = lst
		if response:
			return response
		else:
			response = "No matching data found"
			return response
	except KeyError as e:
		msg="key %s is missing" % str(e)
		return msg
	except Exception as e:
		return str(e)


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Meal project')
    p.add_argument('-i', metavar='meal_data', type=str, help='pyhton json', required=True)
    p.add_argument('-f', nargs='+', help='id list is required', required=True, type=int)
    args = p.parse_args()

    meal_data = {}
    food_ids = args.f
    with open(args.i) as file:
    	data = json.load(file)
    	meal_data = data['MEAL_DATA']

    response = get_matching_meals(meal_data, food_ids)
    print(response)