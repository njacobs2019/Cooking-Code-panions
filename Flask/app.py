from flask import Flask, redirect, render_template, request
from DBAccess import DBAccess
from search import Search

app = Flask(__name__)


@app.route("/")
def tasks():
    return render_template("home.html")

@app.route("/search", methods=["GET"])
def search():

    db = DBAccess()
    searchbar_input = request.args.get("searchbar")

    search_results = db.full_search(searchbar_input)
    
    return render_template("search_results.html", results=search_results, search_term=searchbar_input)

        

@app.route("/recipe", methods=["GET"])
def recipe():
    
    identifier = request.args.get("id")
    db = DBAccess()
    recipe = db.get_recipe_by_id(identifier)
    return render_template("recipe_page.html", recipe=recipe)


# /recipe?id=6439ee7a028ed8622583235c

@app.route("/login")
def login():
    return render_template("login.html")