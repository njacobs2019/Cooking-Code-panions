from flask import Flask, redirect, render_template, request
from .DBAccess import DBAccess
from . import app

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


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")