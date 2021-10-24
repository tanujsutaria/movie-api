from flask import Blueprint,jsonify,request
from . import db
from .models import Movie

main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_movie():
    """POST request to add a movie"""
    movie_data = request.get_json()
    new_movie = Movie(title=movie_data['title'],
                    rating=movie_data['rating'])
    db.session.add(new_movie)
    db.session.commit()
    return 'Done',201

@main.route('/movies', methods=['GET'])
def get_movies():
    """GET Request to get all movies in the database"""
    movies = []
    movies_list = Movie.query.all()
    for movie in movies_list:
        movies.append({'title':movie.title, 'rating':movie.rating})
    return jsonify({'movies':movies})