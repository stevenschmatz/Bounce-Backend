"""Initializes the Bounce API."""

# Silences ndb warnings
# pylint: disable=F0401
# pylint: disable=E1101

import re

from flask import Blueprint, request, make_response, jsonify, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from google.appengine.ext import ndb

from api.users.user import User

users_blueprint = Blueprint("users_blueprint", __name__)

MINIMUM_PASSWORD_LENGTH = 8

USERNAME_REGEX = """
    ^(?![_.-])      # no {'_', '-', '.'} at beginning
    (?!.*[_.-]{2})  # no combination of two of {'-', '_', '.'} in a row
    [a-zA-Z0-9._-]  # allowed characters
    +(?<![_.-])$    # no {'_', '-', '.'} at end
    """

def username_is_valid(username):
    """Determines if the format of a username is correct.

    Validates usernames according to the regex above.

    Args:
        username:   A string containing the username.

    Returns:
        A boolean, representing whether the username has appropriate characters.
    """

    return re.search(USERNAME_REGEX, username, re.VERBOSE) != None

def username_available(username):
    """Determines if a username is available.

    If the username is already registered, username_available returns
    false, else true.

    Args:
        username:   A string of the username.

    Returns:
        A boolean, representing whether the username is available or not.
    """

    return len(User.query(User.username == username).fetch()) == 0

def password_is_valid(password):
    """Determines whether a password is valid.

    No passwords less than eight characters are allowed.

    Args:
        password:   A string of the password.

    Returns:
        A boolean, representing whether the password is valid or not.
    """

    return len(password) >= MINIMUM_PASSWORD_LENGTH

@users_blueprint.route("/api/v1/users", methods=["POST"])
def create_user():
    """Creates a new user, if and only if the following criteria are satisfied:
    *   The username does not already exist.
    *   The phone number is not already registered.
    *   The password is at least 8 characters long.

    Args:
        request:    A JSON object of the username, password, and phone number.
                    The phone number is used for account verification and for
                    fetching user accounts for a contact list.

    Returns:
        A tuple of the following:

    		* 	A JSON object specifying an error, if any.
    		* 	An HTTP status that is 400 if there was an error, and 201 if
    			the account creation was successful.
            *   An HTTP header specifying the URI of the created user.
    """

    username = request.form["username"]
    password = request.form["password"]

    if not username_is_valid(username):
        return (jsonify({"Error": "Username has the inappropriate characters."}),
                400)
    elif not username_available(username):
        return (jsonify({"Error": "Username is already taken."}),
                400)
    elif not password_is_valid(password):
        return (jsonify({"Error": "Bad password."}),
                400)
    else:
        pass_hash = generate_password_hash(password)
        user_to_insert = User(username=username, password_hash=pass_hash)
        user_id = user_to_insert.put()

        return ("Well done!",
                201,
                {
                    "id": user_id.id()
                })

@users_blueprint.route('/api/v1/users/<int:id>', methods=["GET"])
def get_user(id):
    """Gets information about the user for the given ID."""
    user = User.get_by_id(id)

    if user == None:
        return (jsonify({"Error": "User not found."}), 404)
    else:
        return user.username
