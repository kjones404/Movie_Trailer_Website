#!/usr/bin/env python3

""" Project Movie Trailer website

This project is part of the Udacity Full Stack Nanodegree program.

"""


import json
from urllib.request import urlopen

import media
import fresh_tomatoes


def get_db_url(id,type):
    """Build database request url.

    Args:
        ID: TMDb movie ID
        Type: Selects database requested (moive or trailer)
    Behavior:
        Adds moive id, data type request, & api key string to url_start.
    Returns:
        Completed database url request.
    """
    tmdb_key = "api_key"  # add TMDb API Key (v3 auth) string here
    url_start = "https://api.themoviedb.org/3/movie/"
    if type == "movie":
        db_url = url_start + id + "?api_key=" + tmdb_key
    else:
        if type == "trailer":
            db_url = url_start + id + "/videos?api_key=" + tmdb_key
    return db_url

def get_db(id,type):
    """Use database url to pull json dictionary.

    Args:
        ID: TMDb movie ID
        Type: Select database requested (moive or trailer)
    Behavior:
        Call get_db_url to generate database url.
        Pull data through json request.
    Returns:
        Requested data.
    """
    db_url = get_db_url(id, type)
    data = json.load(urlopen(db_url))
    return data

def get_poster(poster_path):
    """Compete the file path for poster image.

    Args:
        poster_path: End of file path
    Behavior:
        Complete file path with url_start, poster_size, & poster_path.
    Returns:
        Completed moive poster url.
    """
    url_start = "https://image.tmdb.org/t/p/"
    poster_size = "w342"  # select image size
    url_poster = url_start + poster_size + poster_path
    return url_poster

def get_trailer(id):
    """Compete the file path for movie trailer.

    Args:
        ID: TMDb movie ID
    Behavior:
        Call get_db to pull movie trailer data.  Use data to generate moive
        trailer url.
    Returns:
        Completed moive trailer url.
    """
    trailer_data = get_db(id, "trailer")
    yt_key = trailer_data["results"][0]["key"]
    yt_url = "https://www.youtube.com/watch?v=" + yt_key
    return yt_url

def get_tmdb(movie_info):
    """Compile list used to generate moive class object.

    Args:
        movie_info: list containing TMDb movie ID
    Behavior:
        Use movie ID found in movie_info to call get_db and get movie data.
        Use moive data to start building & formating class variables.  Call
        get_poster to generate poster url.  Call get_trailer to generate
        trailer url.  Add variables to movie_info.
    Returns:
        Completed moive_info list.
    """
    id = movie_info[0]
    movie_data = get_db(id, "movie")
    obj_name = (movie_data["title"]).replace(" ","_").lower()
    title = movie_data["title"]
    year = movie_data["release_date"][:4]  # release_date formated YYYY-MM-DD
    summary = movie_data["overview"]
    poster_img = get_poster(movie_data["poster_path"])
    trailer = get_trailer(id)
    movie_info.extend([obj_name, title, year, summary, poster_img, trailer])
    return movie_info

def main():
    """Generate movie class object.  Generate website HTML.

    Args:
        none
    Behavior:
        Loops tmdb_id list and calls get_tmdb to pull data for each movie.
        Ceates a moive object for each movie.  Generates a list of movie
        objects.  Calls open_movies_page to generate website html.
    """
    tmdb_id = ["18", "245891", "118340", "2493", "43074", "1542"]
    movie_obj = []
    for id in tmdb_id:
        movie_info = [id]
        get_tmdb(movie_info)
        movie_info[1] = media.Movie(  # obj_name
            movie_info[2],  # title
            movie_info[3],  # year
            movie_info[4],  # summary
            movie_info[5],  # poster_img
            movie_info[6])  # trailer
        movie_obj.append(movie_info[1])  # obj_name
    fresh_tomatoes.open_movies_page(movie_obj)


if __name__ == '__main__':
     # will only be executed when ran directly
    main()
