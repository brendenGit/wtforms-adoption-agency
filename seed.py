from models import Pet, db
from app import app

db.drop_all()
db.create_all()

Pet.query.delete()

Izzy = Pet(name='Izzy',
           species='Cat',
           photo_url='https://shorturl.at/sCMX1',
           age=15,
           notes='A very cute orange cat. RIP.',
           available=False)

Sage = Pet(name='Sage',
           species='Dog',
           photo_url='https://shorturl.at/cqDF6',
           age=3,
           notes='A very cute, large, white, fluffy dog. V sleepy too.')

Kinnick = Pet(name='Kinnick',
           species='Dog',
           photo_url='https://shorturl.at/dlN05',
           age=7,
           notes='A very wild and energetic dog. A bit crazy too.')

db.session.add(Izzy)
db.session.add(Sage)
db.session.add(Kinnick)

db.session.commit()