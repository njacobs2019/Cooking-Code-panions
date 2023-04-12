from DBAccess import DBAccess

db = DBAccess()
recipe = db.get_random_recipe()

print(recipe)