# A bit of a circular import, but because our app is starting off simple:
# First, create the app using the 2 lines below
from flask import Flask
app = Flask(__name__)

# Import all of the python files we want from our directory name
# These files can in turn import app from the __init__.py file
# and therefore add routes and methods as we want
from flaskr import views, random, echo