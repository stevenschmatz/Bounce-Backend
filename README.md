Bounce Messaging
================

Bounce Messaging is a location-based messaging and social app. It is currently under construction, and more information can be found at [our landing page](http://getbounce.io/).

If you're interested in contributing, please shoot me an email at [my personal address](mailto:stevenschmatz@gmail.com), and we can get in touch.

Table of contents
-----------------

###`/api/`

Hosts the private REST API for the mobile app. This interacts with Google Cloud Platform. More documentation can be found in `/api/README.md`.

###`/website/`

Hosts the code for the [templated website](http://getbounce.io/). Again, more documentation can be found at `/website/README.md`.

###`/lib/`

Stores the [Flask](http://flask.pocoo.org/) and [Werkzeug](http://werkzeug.pocoo.org/) libraries. These are required by the application and are used to make a web application, alongside Google Cloud Platform and Google App Engine. 

###Application Files

* `main.py`: Initializes the blueprints for the website files, hosted in `/website/`, as well as the REST API hosted in `/api/`.

###Other Files

These files are dependencies of Google App Engine:

* `app.yaml`: Configures the application and describes its dependencies.
* `appengine_config.py`: Gets loaded when a new application instance is created.
* `requirements.txt`: Describes the versions of libraries that are required by the application.