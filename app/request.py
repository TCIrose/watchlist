from app import app
import urllib.request, json
from .models import movie

Movie1 = movie.Movie

#Getting API key
api_key = app.config['MOVIE_API_KEY']

#Getting the movie base URL
base_url = app.config['MOVIE_API_BASE_URL']

movie_results = []
def get_movies(category):
    '''
    Function that gets the json response to our url request
    '''
    get_movies_url = base_url.format(category, api_key)
    


    with urllib.request.urlopen(get_movies_url) as url:
        get_movies_data = url.read()
        get_movies_response = json.loads(get_movies_data)

        #movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

    return movie_results

def process_results(movie_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
    movie_list: A list of dictionaries that contain movie details

    Returns :
    movie_results: A list of movie objects
    '''
    #movie_results = []
    for movie_item in movie_list:
        id1 = movie_item.get('id')
        title1 = movie_item.get('original_title')
        overview1 = movie_item.get('overview')
        poster1 = movie_item.get('poster_path')
        vote_average1 = movie_item.get('vote_average')
        vote_count1 = movie_item.get('vote_count')

        if poster1:
            movie_object = Movie1(id1, title1, overview1, poster1, vote_average1, vote_count1)
            movie_results.append(movie_object)



    return movie_results

def get_movie(id):
    '''
    function to get movie details using the movie id 
    Args:
        id = movie's id
    '''
    get_movie_details_url = base_url.format(id, api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        movie_details_data = url.read()
        movie_details_response = json.loads(movie_details_data)

        movie_object = None
        if movie_details_response:
            id2 = movie_details_response.get('id')
            title2 = movie_details_response.get('original_title')
            overview2 = movie_details_response.get('overview')
            poster2 = movie_details_response.get('poster')
            vote_average2 = movie_details_response.get('voter_average')
            vote_count2 = movie_details_response.get('voter_count')
            
            movie_object = Movie1(id2, title2, overview2, poster2, vote_average2, vote_count2)

    return movie_object