from . import db

class Movie(db.Model):
    id = db.Column(db.Integer, primay_key = True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer )
