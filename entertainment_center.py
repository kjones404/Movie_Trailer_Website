import media
import fresh_tomatoes
from urllib.request import urlopen
import json

movies_id = [18, 245891, 118340, 2493, 43074, 1542]


def get_db_url(id,type):
    tmdb_key = "api_key"
    url_start = "https://api.themoviedb.org/3/movie/"
    if type == "movie":
        db_url = url_start + id + "?api_key=" + tmdb_key
    else:
        if type == "trailer":
            db_url = url_start + id + "/videos?api_key=" + tmdb_key
    return db_url

def get_db(id,type):
    db_url = get_db_url(id, type)
    data = json.load(urlopen(db_url))
    return data

def get_poster(poster_path):
    url_start = "https://image.tmdb.org/t/p/"
    poster_size = "w342"
    url_poster = url_start + poster_size + poster_path
    return url_poster

def get_trailer(id):
    trailer_data = get_db(id, "trailer")
    yt_key = trailer_data["results"][0]["key"]
    yt_url = "https://www.youtube.com/watch?v=" + yt_key
    return yt_url

def get_tmdb(id):
    movie_data = get_db(id, "movie")
    obj_name = (movie_data["title"]).replace(" ","_").lower()
    title = movie_data["title"]
    year = movie_data["release_date"][:4]
    summary = movie_data["overview"]
    poster_img = get_poster(movie_data["poster_path"])
    trailer = get_trailer(id)


# call on class movie to assign moives vaules to its variable
fifth_element = media.Movie(
    "The Fifth Element",
    "1997",
    "PG-13",
    "https://upload.wikimedia.org/wikipedia/en/6/65/Fifth_element_poster_%281997%29.jpg",
    "https://www.youtube.com/watch?v=LiaKTWUiAYA")

john_wick = media.Movie(
    "John Wick",
    "2014",
    "R",
    "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg",
    "https://www.youtube.com/watch?v=cQ5qjJJlH4A")

guardians_galaxy = media.Movie(
    "Guardians of the Galaxy",
    "2014",
    "PG-13",
    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
    "https://www.youtube.com/watch?v=dOyJqGtP-wU")

princess_bride = media.Movie(
    "The Princess Bride",
    "1987",
    "PG",
    "https://upload.wikimedia.org/wikipedia/en/d/db/Princess_bride.jpg",
    "https://www.youtube.com/watch?v=E28KDhsJ65U")

ghostbusters = media.Movie(
    "Ghostbusters",
    "1984",
    "PG",
    "https://upload.wikimedia.org/wikipedia/en/2/2f/Ghostbusters_%281984%29_theatrical_poster.png",
    "https://www.youtube.com/watch?v=Tt7XYt2hQZI")

office_space = media.Movie(
    "Office Space",
    "1999",
    "R",
    "https://upload.wikimedia.org/wikipedia/en/8/8e/Office_space_poster.jpg",
    "https://www.youtube.com/watch?v=dMIrlP61Z9s")

# organize movies in a list
movies = [fifth_element, john_wick, guardians_galaxy, princess_bride, ghostbusters, office_space]

# use fresh_tomatoes.py to create a movie trailer website for the items found in the movies list
fresh_tomatoes.open_movies_page(movies)
