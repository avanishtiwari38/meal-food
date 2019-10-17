import unittest
import os
import json
from solution import get_matching_meals
# import solution

class MeallistTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.expected = []
        self.food_ids = []
        self.meallist = [
                            {
                                "meal_id": 1,
                                "foods": [
                                    {
                                        "food_id": 1,
                                        "food_name": "Idli"
                                    },
                                    {
                                        "food_id": 10,
                                        "food_name": "Sambar"
                                    }
                                ]
                            },
                            {
                                "meal_id": 2,
                                "foods": [
                                    {
                                        "food_id": 1,
                                        "food_name": "Idli"
                                    },
                                    {
                                        "food_id": 11,
                                        "food_name": "Chutney"
                                    }
                                ]
                            },
                            {
                                "meal_id": 3,
                                "foods": [
                                    {
                                        "food_id": 1,
                                        "food_name": "Idli"
                                    },
                                    {
                                        "food_id": 10,
                                        "food_name": "Sambar"
                                    },
                                    {
                                        "food_id": 11,
                                        "food_name": "Chutney"
                                    }
                                ]
                            },
                            {
                                "meal_id": 4,
                                "foods": [
                                    {
                                        "food_id": 2,
                                        "food_name": "Dosa"
                                    },
                                    {
                                        "food_id": 10,
                                        "food_name": "Sambar"
                                    }
                                ]
                            }
                        ]


    def test_meallist_get_meal(self):
        self.food_ids = [1]
        rv = get_matching_meals(self.meallist, self.food_ids)
        self.expected = [1,2,3]
        self.assertCountEqual(rv, self.expected, "success")


    def test_meallist_get_combo(self):
        self.food_ids = [1, 10]
        self.expected = [1,3]
        rv = get_matching_meals(self.meallist, self.food_ids)
        self.assertCountEqual(rv, self.expected, "success")

    def test_meallist_get_3combo(self):
        self.food_ids = [1, 10, 11]
        self.expected = [3]
        rv = get_matching_meals(self.meallist, self.food_ids)
        self.assertCountEqual(rv, self.expected, "success")

    def test_meallist_get_empty(self):
        self.food_ids = []
        self.expected = "Meal or food data missing(cannot be blank)"
        rv = get_matching_meals(self.meallist, self.food_ids)
        self.assertCountEqual(rv, self.expected, "success")

    def test_meallist_get_no_output(self):
        self.food_ids = [110]
        self.expected = "No matching data found"
        rv = get_matching_meals(self.meallist, self.food_ids)
        self.assertCountEqual(rv, self.expected)

    def test_meallist_get_no_keyError(self):
        self.food_ids = [1]
        self.meallist[0]['food'] = self.meallist[0].pop('foods')
        self.expected = "key 'foods' is missing"
        rv = get_matching_meals(self.meallist, self.food_ids)
        self.assertCountEqual(rv, self.expected)

    def test_meallist_get_no_otherids(self):
        self.food_ids = [2]
        self.expected = [4]
        rv = get_matching_meals(self.meallist, self.food_ids)
        self.assertCountEqual(rv, self.expected)

    def test_meallist_get_no_keyError_foodid(self):
        self.food_ids = [1]
        self.meallist[0]['foods'][0]['food_i'] = self.meallist[0]['foods'][0].pop('food_id')
        self.expected = "key 'food_id' is missing"
        rv = get_matching_meals(self.meallist, self.food_ids)
        self.assertCountEqual(rv, self.expected)

    def test_meallist_get_no_keyError_mealid(self):
        self.food_ids = [1]
        self.meallist[0]['meal_i'] = self.meallist[0].pop('meal_id')
        self.expected = "key 'meal_id' is missing"
        rv = get_matching_meals(self.meallist, self.food_ids)
        self.assertCountEqual(rv, self.expected)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()