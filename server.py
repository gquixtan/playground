from flask import Flask, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
# import os
# import twilio_text
# from model import connect_to_db, db, User, Text


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABCD"

app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Renders homepage."""


    return render_template("index.html")


@app.route("/about")
def about():
    """Renders about page."""


    return render_template("about.html")


@app.route("/contact")
def contact():
    """Renders contact page."""


    return render_template("contact.html")


@app.route("/services")
def services():
    """Renders services page """


    return render_template("services.html")





if __name__ == "__main__": #pragma: no cover
    app.run(port=5000, host='0.0.0.0')
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)
    app.run(host='0.0.0.0')
