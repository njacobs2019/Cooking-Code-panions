# Cooking-Code-panions - A web-based recipe-sharing application

## Developers
  - Tyler Harwood
  - Nick
  - Kass Belaya
  - Tristan Cilley
  - Heath Miller

## General Overview

We intend to develop a web application called the “Cooking Companion”. Ultimately we want to create software that enables people to cook, share, and save recipes. The foundation of the application will be a database of recipes supplied by users. Users will be able to cultivate a list of personal recipes and search for new recipes by name, specific ingredients, or dietary restrictions. The app will be able to produce a detailed shopping list for all ingredients and cookware needed to complete the recipe. Once the user’s have everything needed to begin cooking, the application will provide step-by-step instructions to guide the cooking process.

## App Functionality
- A public and private recipe database
  - Create recipe pages for yourself or others
  - Add images
  - Process plain text into step by step instructions.

- Search Recipes
  - Filter results by tags:
  - Ingredients, appliances, allergies, creator, and any other way the user wants to describe their     dish. Functions like a hashtag.
  - Blacklist or whitelist
  - Ability to automatically generate the tags
  - Browse recipes without using search bar

- More:
  - Export required ingredients and tools
  - Share on social media
  - Follow other creators, easily filter for their recipes when searching
  - Step-by-step prompts for when all your hands are busy

# Getting started with Development
1. Navigate to the main directory of the repo (level that contains compose.yaml)
2. Run `docker compose build`.  This builds the required docker images for development
3. Run `docker compose up`.  This starts the containers and runs a local development server at http://localhost:3000
4. Run `docker compose down`. To shut down the container.
