"""Initializes the Bounce API."""

from flask import Blueprint, render_template

api_blueprint = Blueprint("api_blueprint", __name__)

@api_blueprint.route("/api/users/signup")
def users_signup():
    """"""
    return "Hello"
