"""
Bounce backend
==============

main.py initializes the backend server for Bounce Messaging. This hosts the
static website, as well as the private REST API used by the mobile app.
"""

from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
def serve_static_website():
    """Serves the static HTML landing page.

    Serves the website from /app/static.

    Args:
    	none

    Returns:
    	A sample HTML response.
    """

    return render_template("index.html")

@app.route("/multiply/<int:first_value>/<int:second_value>/")
def serve_their_username(first_value, second_value):
    """Just returns the username given.

    Args:
    	username: A string containing the requested username at the URL given.

    Returns:
    	An HTML response containing the username.
    """

    return "<h1>{}</h1>".format(first_value * second_value)

@app.errorhandler(404)
def page_not_found(error):
    """Return a custom 404 error."""
    return error, 404
