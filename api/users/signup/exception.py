"""Implements the exceptions for the user signup."""

from flask import jsonify

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
    	"""Makes a dict of the responses"""
        response_values = dict(self.payload or ())
        response_values['message'] = self.message
        return response_values
