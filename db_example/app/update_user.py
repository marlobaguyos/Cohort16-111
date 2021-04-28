from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import db, User

admin = User.query.filter_by(first_name='Mark').first()
admin.hobbies = 'my_new_email@example.com'
db.session.commit()


# db.session.query(User).filter(User.id==5).update(dict(hobbies='ang pogi mo'))
# db.session.commit()

# admin = User.query.filter(User.id==5).update(dict(hobbies='ang pogi mo'))
# db.session.commit()

# db.session.query(User).filter(User.id==5).update(dict(hobbies='ang pogi mo'))
# db.session.commit()
# print(user.hobbies)


# print(admin)
# pinrt(admin.hobbies)
# admin.hobbies = 'Ang Pogi Mo'
# db.session.commit()


# db.session.query(User).filter(User.id==3).update()

# db.session.commit()

  # admin = User.query.filter_by(username='admin').update(dict(email='my_new_email@example.com')))
  # db.session.commit()