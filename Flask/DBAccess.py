import os
from dotenv import load_dotenv
from pymongo import MongoClient
from bson.objectid import ObjectId


# Load environmental variables
load_dotenv()

# This class defines a database access object
class DBAccess:

    # Singleton instance
    _self = None

    # Singleton constructor, basically says that if you try
    # to construct another instance, return a ref to the singleton.
    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

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
    
    def get_recipe_by_id(self, identifier: str):
        recipe_id = ObjectId(identifier)
        return self.recipes_collection.find_one({"_id": recipe_id})

    def full_search(self, search_text):
        pipeline = [
                    {
                        "$search": {
                            "index": "full_text",
                            "text": {
                                "query": search_text,
                                "path": {
                                    "wildcard": "*"
                                }
                            }
                        }
                    },
                    {
                        "$addFields": {
                            "searchScore": {"$meta": "searchScore"}
                        }
                    },
                    {
                        "$sort": {
                            "searchScore": -1
                        }
                    },
                    {
                        "$limit": 10
                    }
                ]

        return list(self.recipes_collection.aggregate(pipeline))

def test_get_recipe_by_id():
    db = DBAccess()
    identifier = "6439ee7a028ed862258322b8"
    result = db.get_recipe_by_id(identifier)
    print(result)

def test_full_search():
    db = DBAccess()
    results = db.full_search("blueberries")
    print(type(results))

    for result in results:
        print(result["title"])


if __name__=="__main__":
    # test_get_recipe_by_id()
    test_full_search()