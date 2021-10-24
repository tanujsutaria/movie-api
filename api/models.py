from . import db

class Movie(db.Model):
    """Creates the elements of the movie table in the sqlite3 db"""
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    rating = db.Column(db.Integer)