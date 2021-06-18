"""
Running the `create_app` function to compile application
for Flask.
"""
from flask import Flask
from .app import DB

from .app import create_app
APP = create_app()