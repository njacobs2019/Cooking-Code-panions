import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app.DBAccess import DBAccess

class testAuthentication(unittest.TestCase):

    def __init__(self):
        self.db = DBAccess()
    
    # Just need to know whether a recipe object has its URI as an attribute
    #   If we don't want to do that the alternative is to create the object here, 
    #   insert it into the db, grab it by id, then verify the id we gave it matches.
    def test_get_recipe_by_id(self):

        #For a recipe that does exist
        identifier = "6439ee7a028ed862258322b8"
        result = self.db.get_recipe_by_id(identifier)
        self.assertEquals(result["_id"], identifier, f"Should be {identifier}")

        #For a recipe that does not exist
        identifier = "6439ee7a028ed862258322c2"
        result = self.db.get_recipe_by_id(identifier)
        self.assertEquals(type(result), type(None), f"Should be {type(None)}")


    # Dependant on get_recipe_by_id()
    #Verifies that 
    def test_full_search(self):

        known = self.db.get_recipe_by_id("6439ee7a028ed862258322b8")
        results = self.db.full_search(known["title"])

        tokens = known["title"].split()
        containsKnown = False
    
        #Verify that full_search returns a list of recipe objects
        for result in results:
            self.assertEquals(type(result), type(known), f"Should be {type(known)}")

            if result["title"] == known["title"]:
                containsKnown = True

        self.assertTrue(constainsKnown)

    def test_recipe_display(self, page):
        recipe = self.db.get_recipe_by_id()
        #display =        #1. import html as some kind of object

        #2. grab attribute of that object and test against attribute in display
        #self.assertEquals(type(result), type(known), f"Should be {type(known)}")
    
