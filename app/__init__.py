from flask import Flask
from .config import DevConfig
<<<<<<< HEAD
from flask_bootstrap import Bootstrap
=======
from app import views
from app import error
>>>>>>> c8a8b58661071f089157b914c0b99409fa0aa8b9

#Initializing application
app = Flask(__name__, instance_relative_config = True)

#Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing flask extensions
bootstrap = Bootstrap(app)

from app import views
from app import error