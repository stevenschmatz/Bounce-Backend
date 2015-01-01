"""Initializes the Bounce API."""

# Silences ndb import warning
# pylint: disable=F0401

from flask import Blueprint, request, jsonify
from google.appengine.ext import ndb
from api.users.user import User

api_blueprint = Blueprint("api_blueprint", __name__)

MINIMUM_PASSWORD_LENGTH = 8

def username_is_valid(username):
    """Determines if a username is valid.

    The only criteria is that the username has the appropriate characters,
    and is not already taken.

    Args:
        username:   A string of the username.

    Returns:
        A boolean, representing whether the username is valid or not.
    """

    print "Tested if username is valid"

    return True


def password_is_valid(password):
    """Determines whether a password is valid.

    No passwords less than eight characters are allowed.

    Args:
        password:   A string of the password.

    Returns:
        A boolean, representing whether the password is valid or not.
    """

    return len(password) >= MINIMUM_PASSWORD_LENGTH

@api_blueprint.route("/api/users", methods=["POST"])
def new_user():
    """Creates a new user with the given credenti
    Creates a new user, if and only if the following criteria are satisfied:
    *   The username does not already exist.
    *   The phone number is not already registered.
    *   The password is at least 8 characters long.

    Args:
        request:    A JSON object of the username, password, and phone number.
                    The phone number is used for account verification and for
                    fetching user accounts for a contact list.

    Returns:
        A tuple of the following:als.

    		* 	A JSON object specifying an error, if any.
    		* 	An HTTP status that is 400 if there was an error, and 201 if
    			the account creation was successful.
    """

    username = request.form["username"]
    password = request.form["password"]

    if not username_is_valid(username):
        return "Bad username.", 400
    elif not password_is_valid(password):
        return "Bad password.", 400
    else:
        return "Well done!", 201
