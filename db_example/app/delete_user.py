from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db, User

db.session.query(User).filter(User.id==3).delete()
db.session.commit()
