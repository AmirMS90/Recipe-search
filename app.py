"""
    Usage of AI:
    Using codeium for commenting and autocomplete
"""

import requests
from flask import Flask, request, render_template

app = Flask(__name__)


def get_data_from_api(url):
    # Make a GET request to the API
    response = requests.get(url)

    # Check that the request was successful
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()
        return data
    else:
        return None


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