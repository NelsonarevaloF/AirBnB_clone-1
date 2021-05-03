#!/usr/bin/python3
"""This module starts a Flask web application that will be served
   in 'http://0.0.0.0:5000/'"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays string"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays string"""
    return "HBNB"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
