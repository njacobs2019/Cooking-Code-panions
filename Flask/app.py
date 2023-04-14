from flask import Flask, redirect, render_template, request
from DBAccess import DBAccess

app = Flask(__name__)


@app.route("/")
def tasks():
    return render_template("bigSearch.html")

@app.route("/recipe")
def recipe():
    db = DBAccess()
    recipe = db.get_random_recipe()
    return render_template("recipe_page.html", recipe=recipe)
    
