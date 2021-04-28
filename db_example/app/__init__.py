#!/user/bin/env python3
#-*- coding: utf8 -*-
"""Sample app"""
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydb.db"
db = SQLAlchemy(app)

from app.database import *

@app.route("/about/<int:uid>")
def about(uid):
  user = User.query.filter_by(id=uid).first()
  return {
    "first_name": user.first_name,
    "last_name": user.last_name,
    "hobbies": user.hobbies
  }

@app.route('/agent')
def agent():
  user_agent = request.headers.get("User-Agent")
  return "<p>Your user agent is %s</p>" % user_agent
