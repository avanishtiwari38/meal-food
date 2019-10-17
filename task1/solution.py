import argparse
import json

filename = 'meal_data.py'

def get_matching_meals(meal_data, food_ids):
	try:
		food_ids = set(food_ids)

		lst = []
		if not meal_data or not food_ids:
			response = "Meal or food data missing(cannot be blank)"
			return response

		for y in meal_data:
			if len(y['foods']) >= len(food_ids):
				food =set([z['food_id'] for z in y['foods']])
				if food.issuperset(food_ids) :
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
    # p.add_argument('-i', metavar='meal_data', type=str, help='pyhton json', required=True)
    p.add_argument('-f', nargs='+', help='id list is required', required=True, type=int)
    args = p.parse_args()

    meal_data = {}
    food_ids = args.f
    with open(filename) as file:
    	data = json.load(file)
    	meal_data = data

    response = get_matching_meals(meal_data, food_ids)
    print(response)