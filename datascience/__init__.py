from flask import Flask
from flask.ext.cache import Cache
import os

app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
basedir = os.path.abspath(os.path.dirname(__file__))
import datascience.views
