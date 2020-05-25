from flask import render_template
from app import app
from .request import get_movies, get_movie

#views

@app.route('/')
def index():
    '''
    view root page that returns the index page and its data
    '''

    #Getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    upcoming_movie = get_movies('upcoming')
    now_showing_movie = get_movies('now_playing')
    title = "Home - welcome to the Best Movie Review Website Online"
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing_movie)#first message = in html doc, second html = views file

#dynamic routes
@app.route('/movie/<int:id>')
def movie(id):
    '''
    View movie page function that returns the movie details page and its data
    '''
    movie = get_movie(id)
    title = f'{movie.title}'
    
    return render_template('movie.html', title = title, movie = movie)

