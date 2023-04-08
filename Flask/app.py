from flask import Flask, redirect, render_template, request
from DBAccess import DBAccess

app = Flask(__name__)


@app.route("/")
def tasks():
    db = DBAccess()
    recipe = db.get_first_recipe()
    return render_template("recipe_page.html", recipe=recipe)

# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "GET":
#         return render_template("add.html")
#     else:
#         todo = request.form.get("task")
#         todos.append(todo)
#         return redirect("/")
