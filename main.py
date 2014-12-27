"""
Bounce backend
==============

main.py initializes the backend server for Bounce Messaging. This hosts the
static/templated website, as well as the private REST API used by the mobile app.
"""

from flask import Flask
from website.main import website_blueprint

app = Flask(__name__, static_folder="website/static", 
            template_folder="website/templates")
app.config["DEBUG"] = True

app.register_blueprint(website_blueprint)
