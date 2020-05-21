from flask import render_template
from app import app
from .request import get_movies

#views

@app.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''

    #Getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = "Home - welcome to the Best Movie Review Website Online"
    return render_template('index.html', title = title, popular = popular_movies )#first message = in html doc, second html = views file

#dynamic routes
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html', id = movie_id)

