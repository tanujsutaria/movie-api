from flask import Blueprint,jsonify

main = Blueprint('main', __name__)

@main.route('/add_movie', methods=['POST'])
def add_movie():

    return 'Done',201

@main.route('/movies', methods=['GET'])
def get_movies():
    movies = []
    return jsonify({'movies':movies}) 