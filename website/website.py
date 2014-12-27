"""Initializes the Bounce website."""

from flask import Blueprint, render_template

website_blueprint = Blueprint('website_blueprint', __name__)

@website_blueprint.route("/")
def serve_website():
    """Serves the static HTML landing page.

    Serves the website from /app/static.

    Args:
      none

    Returns:
      A sample HTML response.
    """

    return render_template("html/index.html")
