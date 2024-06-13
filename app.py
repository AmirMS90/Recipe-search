"""
    Usage of AI:
    Using codeium for commenting and autocomplete
"""

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

