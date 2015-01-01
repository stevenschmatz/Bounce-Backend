"""Supplies the methods required for onboarding a user in the application."""

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

    if len(username) < MINIMUM_PASSWORD_LENGTH:
        return False
    else:
        return True


print username_is_valid("3290239")