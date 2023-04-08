import os
from dotenv import load_dotenv
from pymongo import MongoClient


# Load environmental variables
load_dotenv()

# This class defines a database access object
class DBAccess:
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


if __name__=="__main__":
    db = DBAccess()

    result = db.get_first_recipe()

    print(result)