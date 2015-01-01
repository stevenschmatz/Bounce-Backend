"""Initializes the Bounce API."""

from api.users.main import users_blueprint

def register_all_blueprints(app):
    """A convenience function that registers all API blueprints to app."""
    app.register_blueprint(users_blueprint)
