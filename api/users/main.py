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

@users_blueprint.route("/api/v1/users", methods=["PUT"])
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

    DEV_BAD_USER_MSG = ("Username has inappropriate characters. "
                        "The username must match the following regex: "
                        "^(?![_.-])(?!.*[_.-]{2})[a-zA-Z0-9._-]+(?<![_.-])$. "
                        "That is, the allowed characters are alphanumeric, "
                        "with {., _, -} allowed in the middle of the string.")

    USER_BAD_USER_MSG = ("The username has inappropriate characters. "
                         "Please use numbers, letters, underscores, and "
                         "hyphens.")

    DEV_USERNAME_TAKEN_MSG = ("The username has already been taken.")

    USER_USERNAME_TAKEN_MSG = ("Sorry! Looks like someone got that awesome username "
                               "before you. Try again.")

    DEV_BAD_PASS_MSG = ("The password was not a minimum of 8 characters.")

    USER_BAD_PASS_MSG = ("Your password is weak. Try something a bit longer.")

    username = request.form["username"]
    password = request.form["password"]

    if not username_is_valid(username):
        return (jsonify(status=400,
                        developer_message=DEV_BAD_USER_MSG,
                        user_message=USER_BAD_USER_MSG),
                400)
    elif not username_available(username):
        return (jsonify(status=400,
                        developer_message=DEV_USERNAME_TAKEN_MSG,
                        user_message=USER_USERNAME_TAKEN_MSG),
                400)
    elif not password_is_valid(password):
        return (jsonify(status=400,
                        developer_message=DEV_BAD_PASS_MSG,
                        user_message=USER_BAD_PASS_MSG),
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
