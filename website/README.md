`/website/`
===========

This folder hosts the code for the landing page for Bounce. This landing page is found [here](http://getbounce.io/).

Table of contents
-----------------

###`/website/static/`

Hosts all static, non-templated content for the website. This includes:

* Stylesheets (pre-processed by Sass in `/website/templates/`)
* Javascript files
* Resources such as images
* Other files such as `humans.txt` and `robots.txt`

###`/website/templates/`

Hosts all pre-processed code and templated HTML code. This includes:

* The source templated Jade code for the website
* The processed HTML templates
* The SCSS code
* The Foundation SCSS dependencies.

###`/website/main.py`

Initializes the website and routes the URLs to the appropriate templates.

Exports flask `Blueprint`s which are registered in `/main.py`.