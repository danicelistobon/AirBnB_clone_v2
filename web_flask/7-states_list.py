#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """display Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """display HBNB
    """
    return "HBNB"


@app.route("/c/<text>")
def c_text(text):
    """display "C " followed by the value of the text variable
    """
    return "C " + text.replace("_", " ")


@app.route("/python/")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """display "Python " followed by the value of the text variable
    """
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>")
def number(n):
    """display "n is a number" only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """display a HTML page only if n is an integer
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    """display a HTML page only if n is an integer
    """
    if (n % 2 == 0):
        text = "even"
        return render_template("6-number_odd_or_even.html", n=n, text=text)
    else:
        text = "odd"
        return render_template("6-number_odd_or_even.html", n=n, text=text)


@app.route("/states_list")
def states_list(n):
    """display a HTML page
    """
    return render_template('7-states_list.html', states=storage.all("State"))


@app.teardown_appcontext
def teardown_appcontext(self):
    """display a HTML page
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
