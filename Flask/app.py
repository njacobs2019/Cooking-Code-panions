from flask import Flask, redirect, render_template, request
from DBAccess import DBAccess

app = Flask(__name__)


@app.route("/")
def tasks():

    #Uncomment when db is working for everyone. -Tyler
    #db = DBAccess()
    #recipe = db.get_random_recipe()
    #return render_template("recipe_page.html", recipe=recipe)

    #For now you can just render individual templates you've made with this. -Tyler
    return render_template("bigSearch.html")

# @app.route("/add", methods=["GET", "POST"])
# def add():
#     if request.method == "GET":
#         return render_template("add.html")
#     else:
#         todo = request.form.get("task")
#         todos.append(todo)
#         return redirect("/")
