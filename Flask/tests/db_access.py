import unittest
from DBAccess import DBAccess

class testAuthentication(unittest.TestCase):

    def __init__(self):
        self.db = DBAccess()
    
    # Just need to know whether a recipe object has its URI as an attribute
    #   If we don't want to do that the alternative is to create the object here, 
    #   insert it into the db, grab it by id, then verify the id we gave it matches.
    def test_get_recipe_by_id(self):

        identifier = "6439ee7a028ed862258322b8"
        result = self.db.get_recipe_by_id(identifier)
        #print(result)
        self.assertEquals(result["_id"], identifier, f"Should be {identifier}")

    def test_get_recipe_by_id(self):

        identifier = "6439ee7a028ed862258322b1"
        result = self.db.get_recipe_by_id(identifier)
        self.assertEquals(result["_id"]), identifier, f

    # Dependant on get_recipe_by_id()
    def test_full_search(self):

        known = self.db.get_recipe_by_id("6439ee7a028ed862258322b8")
        results = self.db.full_search("blueberries")
    
        #Verify that full_search returns a list of recipe objects
        #print(type(results))
        for result in results:
            #print(result["title"])
            self.assertEquals(type(result), type(known), f"Should be {type(known)}")

    def test_recipe_display(self, page):
        recipe = self.db.get_recipe_by_id()
        #display =        #1. import html as some kind of object

        #2. grab attribute of that object and test against attribute in display
        #self.assertEquals(type(result), type(known), f"Should be {type(known)}")
    
