# Cooking-Code-panions - A web-based recipe-sharing application

We intend to develop a web application called the “Cooking Companion”. Ultimately we want to create software that enables people to cook, share, and save recipes. The foundation of the application will be a database of recipes supplied by users. Users will be able to cultivate a list of personal recipes and search for new recipes by name, specific ingredients, or dietary restrictions. The app will be able to produce a detailed shopping list for all ingredients and cookware needed to complete the recipe. Once the user’s have everything needed to begin cooking, the application will provide step-by-step instructions to guide the cooking process.

## App Functionality
- A public and private recipe database
  - Create recipe pages for yourself or others
  - Add images
  - Process plain text into step by step instructions.

- Search Recipes
  - Filter results by tags:
  - Ingredients, appliances, allergies, creator, and any other way the user wants to describe their dish. Functions like a hashtag.
  - Blacklist or whitelist
  - Ability to automatically generate the tags
  - Browse recipes without using search bar

- More:
  - Export required ingredients and tools
  - Share on social media
  - Follow other creators, easily filter for their recipes when searching
  - Step-by-step prompts for when all your hands are busy

# Running Cooking Code-panion

1. Clone or fork the repository
2. Create a Python virtual environment with Python 3.11
3. Install dependencies
```
pip install -r requirements.txt
```
4. Install the database access credentials.  The production database is hosted on MongoDB Atlas.  To properly authenticate with the database, place the credential file in `app/.env` and make sure the file name is `.env`.
5. Run the following command from inside the app folder to start the Flask server.
```
flask run
```

# Getting started with Development

1. This project uses Python 3.11, create a conda environment called `flask`
```
conda create --name flask python=3.11
```
2. Run this to install Python dependencies (when at base directory):  
```
pip install -r requirements.txt
```
3. Run this to start the Flask development server (it refreshes when files are changed):
```
flask --debug run
```

# Developers
  - Tyler Harwood
  - Nick Jacobs
  - Kass Belaya
  - Tristan Cilley
  - Heath Miller