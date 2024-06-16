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


@app.route("/SearchByName", methods=["Get", "POST"])
def SearchByName():
    """
    This function is a route handler for the "/SearchByName" endpoint. It handles both GET and POST requests.

    Parameters:
    - None

    Returns:
    - If the request method is POST, it retrieves the "name" value from the request form and makes a GET request to the TheMealDB API with the name as a query parameter. It then checks if the response contains any meals and returns the filtered results if there are any. Otherwise, it renders the "apology.html" template with an error code of 404.
    - If the request method is not POST, it renders the "SearchByName.html" template.
    """
    if request.method == "POST":
        searched = request.form.get("name")
        if not searched.strip():
            return render_template("apology.html", error=400, message="Please enter a name")
        filteredResults = get_data_from_api(
            f"http://www.themealdb.com/api/json/v1/1/search.php?s={searched}"
        )
        if not filteredResults or not filteredResults["meals"]:
            return render_template("apology.html", error=404)
        return render_template("results.html", results=filteredResults["meals"])
    return render_template("SearchByName.html")


@app.route("/SearchByIngredient", methods=["Get", "POST"])
def SearchByIngredient():
    """
    Searches for recipes by ingredient using the TheMealDB API.

    This function is a route handler for the "/SearchByIngredient" endpoint. It handles both GET and POST requests.

    Parameters:
    - None

    Returns:
    - If the request method is POST, it retrieves the "ingredient" value from the request form and makes a GET request to the TheMealDB API with the ingredient as a query parameter. It then checks if the response contains any meals and returns the filtered results if there are any. Otherwise, it renders the "apology.html" template with an error code of 404.
    - If the request method is not POST, it renders the "SearchByIngredient.html" template.
    """
    if request.method == "POST":
        searched = request.form.get("ingredient")
        if not searched.strip():
            return render_template("apology.html", error=400, message="Please enter an ingredient")
        filteredResults = get_data_from_api(
            f"http://www.themealdb.com/api/json/v1/1/filter.php?i={searched}"
        )
        if not filteredResults or not filteredResults["meals"]:
            return render_template("apology.html", error=404)
        return render_template("results.html", results=filteredResults["meals"])
    return render_template("SearchByIngredient.html")


@app.route("/meal/<id>")
def meal(id):
    """
    Retrieves a specific meal from TheMealDB API based on the provided meal ID.

    Parameters:
        id (str): The ID of the meal to retrieve.

    Returns:
        flask.Response: The rendered "meal.html" template with the meal data passed as a context variable.
    """
    resultmeal = get_data_from_api(
        f"http://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
    )["meals"][0]
    return render_template("meal.html", meal=resultmeal)
