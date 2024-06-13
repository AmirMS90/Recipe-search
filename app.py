"""
    Usage of AI:
    Using codeium for commenting and autocomplete
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/SearchByName", methods=["Get","POST"])
def SearchByName():
    if request.method == "POST":
        #TODO: Implement search by name
        return "TODO"
    return render_template("SearchByName.html")

@app.route("/SearchByIngredient", methods=["Get","POST"])
def SearchByIngredient():
    if request.method == "POST":
        #TODO: Implement search by ingridient
        return "TODO"
    return render_template("SearchByIngredient.html")