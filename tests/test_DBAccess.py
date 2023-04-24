import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app.DBAccess import DBAccess
from bson.objectid import ObjectId

class testAuthentication(unittest.TestCase):
    def setUp(self):
        self.db = DBAccess()
    
    def test_get_recipe_by_existing_id(self):
        """
        Retrieve recipe that is known to exist
        """
        identifier = "6439ee7a028ed862258322b8"
        result = self.db.get_recipe_by_id(identifier)
        self.assertEqual(result["_id"], ObjectId(identifier), f"Should be {identifier}")

    def test_get_recipe_by_nonexisting_id(self):
        """
        Retrieve recipe that is known not to exist
        """
        identifier = "6439ee7a028ed882258322c8"
        result = self.db.get_recipe_by_id(identifier)
        self.assertEqual(type(result), type(None), f"Should be {type(None)}")

    def test_full_search_(self):
        """
        Verify that full_search returns  a list of recipe objects
        """
        known_recipe = self.db.get_recipe_by_id("6439ee7a028ed862258322b8")
        search_results = self.db.full_search(known_recipe["title"])
    
        for recipe in search_results:
            self.assertEqual(type(recipe), type(known_recipe), f"Should be {type(known_recipe)}")

    def test_get_with_title(self):
        """
        Searches for a recipe with a specific title and checks that
        the recipe that is returned has that title
        """
        title = "Pumpkin Pancakes"
        recipe = list(self.db.get_with_title(title))[0]
        self.assertEqual(title, recipe["title"], "The titles must match")

    def test_get_first_recipe(self):
        """
        Checks to make sure that get_first_recipe returns a recipe and it has a title
        """

        recipe = self.db.get_first_recipe()
        self.assertIsInstance(recipe, dict, "The recipe must be a dictionary")

if __name__ == "__main__":
    unittest.main()