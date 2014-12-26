"""
Bounce backend
==============

main.py initializes the backend server for Bounce Messaging. This hosts the
static website, as well as the private REST API used by the mobile app.
"""

from flask import Flask

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

    return "<h2>Hello World! This is the Bounce website.</h2>"

@app.route("/multiply/<int:x>/<int:y>/")
def serve_their_username(x, y):
    """Just returns the username given.

    Args:
    	username: A string containing the requested username at the URL given.

    Returns:
    	An HTML response containing the username.
    """

    return "<h1>{}</h1>".format(x * y)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return e, 404
