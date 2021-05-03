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


@app.route("/c/<text>", strict_slashes=False)
def show_c_var(text):
    """display C followed by the value of the text variable and
    replace underscore _ symbols with a space"""
    str_without_sym = text.replace('_', ' ')
    return 'C %s' % str_without_sym


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def show_python_var(text="is cool"):
    """display Python , followed by the value of the text
    variable (replace underscore _ symbols with a space"""
    str_without_sym = text.replace('_', ' ')
    return 'Python %s' % str_without_sym


if __name__ == "__main__":
    app.run(host="0.0.0.0")
