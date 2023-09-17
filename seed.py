from models import Pet, db
from app import app


db.drop_all()
db.create_all()

User.query.delete()

brenden = User(first_name='Brenden', last_name='Arias')
sage = User(first_name='Sage', last_name='Arias-Hart', profile_picture='https://cf.ltkcdn.net/dogs/puppies/images/orig/326566-1600x1066-guide-great-pyrenees-puppies.jpg')
meghan = User(first_name='Meghan', last_name='Hart')

db.session.add(brenden)
db.session.add(sage)
db.session.add(meghan)

db.session.commit()