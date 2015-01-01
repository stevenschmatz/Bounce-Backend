"""
Provides the structure for a Bounce user, so that it can interact with
Google's NDB Datastore.
"""

# Silences ndb import warning
# pylint: disable=F0401

from google.appengine.ext import ndb

class User(ndb.Model):
    """Models an individual Bounce user:

    *   Credentials
    *   Time joined
    *   Friends

    Parent key:
        None

    Child keys:
        *   Post
        *   Groups
    """

    username = ndb.StringProperty()
    password_hash = ndb.StringProperty(indexed=False)

    time_joined = ndb.DateTimeProperty(auto_now_add=True)
    last_activity_time = ndb.DateTimeProperty(auto_now=True)

    # List of strings where string is friend username
    friends = ndb.StringProperty(repeated=True)
