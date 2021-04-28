from app import db, User

def create_my_user(first_name, last_name, hobbies):
  """Simple user creation function"""
  db.session.add(
    User(
      first_name=first_name,
      last_name=last_name,
      hobbies=hobbies
      )
    )
  db.session.commit()

if __name__ == "__main__":
  create_my_user("Marlo", "Baguyos", "Movie")
  user = User.query.all()
  print(user)
  create_my_user("John", "Doe", "Golfing")
  user = User.query.filter_by(first_name="John").first()
  print(user)
  create_my_user("Mark", "Pogi", "Disco")
  user = User.query.filter_by(first_name="Mark").first()
  print(user)
