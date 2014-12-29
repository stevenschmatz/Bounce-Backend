"""Initializes the Bounce website."""

from flask import Blueprint, render_template

website_blueprint = Blueprint('website_blueprint', __name__)

@website_blueprint.route("/")
def serve_index_html():
    """Serves the static HTML landing page.

    Serves the website from /website/static/html.

    Args:
        none

    Returns:
        The rendered template of the HTML frontend of the website.
    """

    return render_template("html/index.html")

@website_blueprint.route("/api/")
def api():
    """Serves the root page for the API.

    Executes the template from /website/static/html

    Args:
        none

    Returns:
        The rendered template of the HTML API landing page.
    """

    return render_template("html/api.html")

@website_blueprint.errorhandler(404)
def page_not_found(error):
    """Return a custom 404 error.

    Args:
        none

    Returns:
        A tuple of the HTML response, and the error code.
    """

    return error, 404
