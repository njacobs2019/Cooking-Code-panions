import os
from dotenv import load_dotenv
from pymongo import MongoClient


# Load environmental variables
load_dotenv()

# This class defines a database access object
class DBAccess:

    # Singleton instance
    _self = None

    # Singleton contructor, basically says that if you try
    # to contruct another instance, return a ref to the singleton.
    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    # Init method, just extends the 'class' class after its has 
    # already been created by python
    def __init__(self):
        # Connect to the MongoDB Atlas cluster
        mongodb_uri = os.environ.get('MONGODB_URI')
        client = MongoClient(mongodb_uri)
        self.db = client['cooking-code-panions']
        self.recipes_collection = self.db['recipes']
    
    def get_with_title(self, title):
        search_pattern = {
            "title": {
                "$regex": title,
                "$options": "i"  # This makes the search case-insensitive
            }
        }
        return self.recipes_collection.find(search_pattern)
    
    def get_first_recipe(self):
        # Get the first recipe from the database
        return self.recipes_collection.find_one()
    
    def get_random_recipe(self):
        # Get a random recipe from the database
        random_recipe = self.recipes_collection.aggregate([{ "$sample": { "size": 1 } }])
        return random_recipe.next()


if __name__=="__main__":
    db = DBAccess()

    result = db.get_first_recipe()

    print(result)