from flask import Flask, redirect, render_template, request
from DBAccess import DBAccess
from search import Search

app = Flask(__name__)


@app.route("/")
def tasks():
    return render_template("bigSearch.html")

@app.route("/search", methods=["GET"])
def search():

    db = DBAccess()
    searchbar_input = request.args.get("searchbar")

    print(searchbar_input)

    #search_payload = Search(searchbar_input)

    if searchbar_input is not None:
        recipes = db.get_with_title(searchbar_input)
        return render_template("recipe_page.html", recipe=recipes[0])
        

@app.route("/recipe")
def recipe():
    db = DBAccess()
    recipe = db.get_random_recipe()
    return render_template("recipe_page.html", recipe=recipe)


@app.route("/login")
def login():
    return render_template("login.html")