import media
import fresh_tomatoes
import requests
import api_key
from random import shuffle


def get_movie_id(key, title):
    """
    Uses the The Movie Database api to search for an english-language,
    non-adult movie by its title and return its id.

    key: str. Api key for The Movie Database
    title: str. The title of the movie whose id you want
    """

    # the required values to insert after the generic request url
    payload = {"api_key": key, "language": "en-US", "query": title,
               "page": "1", "include_adult": "false"}

    # returns a json object from TMDB's search and decodes it into a Python
    # object, and assigns that to json_data
    json_data = requests.get("https://api.themoviedb.org/3/search/movie?",
                             params=payload).json()

    # returns the value of the "id" attribute
    return json_data["results"][0]["id"]


def make_movie(key, title):
    """
    Uses the The Movie Database api to get information for an
    english-language, non-adult movie based on its title and returns those
    details as a python object

    key: str. Api key for The Movie Database
    title: str. The title of the movie whose information you want
    """

    movie_id = get_movie_id(key, title)

    # the values to insert after the generic request url
    payload = {"api_key": key, "language": "en-US",
               "append_to_response": "videos"}

    # returns a json object from TMDB's Get Details and decodes it into a
    # Python object, and assigns that to json_data
    json_data = requests.get("https://api.themoviedb.org/3/movie/" +
                             str(movie_id) + "?", params=payload).json()

    return json_data


def get_movie_objects(key, titles):
    """
    Takes a list of movie names, and returns a list of movie objects with
    information about each of the movies named in the original list

    titles: list of strings. List of movie titles
    """
    movie_objects = []

    for title in titles:
        movie = make_movie(key, title)
        movie_objects.append(movie)

    return movie_objects

# get api key
my_key = api_key.key

# titles of movies we want to display
favorite_movies = ["Lady Bird", "Coco", "I, Tonya", "Moonrise Kingdom",
                   "Midnight in Paris", "Fantastic Mr. Fox",
                   "The Shape of Water", "A Serious Man", "Love Actually",
                   "Isle of Dogs", "The Grand Budapest Hotel",
                   "Call Me by Your Name", "The King's Speech", "La La Land",
                   "The Big Short", "Birdman", "Her", "American Hustle"]

# randomize the order so the page isn't the same everytime it's created
shuffle(favorite_movies)

# get list of movie objects; one for each favorite movie
movies = get_movie_objects(my_key, favorite_movies)

# generate fresh_tomatoes.html for my favorite movies
fresh_tomatoes.open_movies_page(movies)
