#!/user/bin/env python3
# -*- coding: utf8 -*-
"""HTTP route  definitions"""

from app import app # From our app package import the app variable
@app.route("/")
def index():
  return "Hello, world!"
@app.route("/about")
def about():
  me = {
    "first_name": "Marlo",
    "last_name": "Baguyos",
    "hobbies": "DIY stuff"
  }
  return me