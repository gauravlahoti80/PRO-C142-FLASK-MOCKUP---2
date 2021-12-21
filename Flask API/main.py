from logging import debug
import csv
from os import read
from flask import jsonify, Flask, request

app = Flask(__name__)
all_movies = []
liked_movies = []
disliked_movies = []

with open('movies.csv', encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]


@app.route('/displaymovies')
def displayMovies():
    return jsonify({
        'data': all_movies[0],
        'status': 'success'
    })


@app.route('/showlikedmovies')
def showLikedMovies():
    liked_movies.append(all_movies[0])
    return jsonify({
        'data': all_movies[0],
        'status': 'successful'
    })

@app.route('/dislikedmovies')
def dislikedMovies():
    disliked_movies.append(all_movies[0])
    return jsonify({
        'data' : all_movies[0],
        'status' : 'successful' 
    })

if (__name__ == '__main__'):
    app.run(debug=True)
