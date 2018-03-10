from urllib.request import urlopen
import json

import media
import fresh_tomatoes


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

def get_tmdb(movie_info):
    id = movie_info[0]
    movie_data = get_db(id, "movie")
    obj_name = (movie_data["title"]).replace(" ","_").lower()
    title = movie_data["title"]
    year = movie_data["release_date"][:4]
    summary = movie_data["overview"]
    poster_img = get_poster(movie_data["poster_path"])
    trailer = get_trailer(id)
    movie_info.extend([obj_name, title, year, summary, poster_img, trailer])
    return(movie_info)

def main():
    tmdb_id = ["18", "245891", "118340", "2493", "43074", "1542"]
    movie_obj = []
    for id in tmdb_id:
        movie_info = [id]
        get_tmdb(movie_info)
        movie_info[1] = media.Movie(
            movie_info[2],
            movie_info[3],
            movie_info[4],
            movie_info[5],
            movie_info[6])
        movie_obj.append(movie_info[1])
    fresh_tomatoes.open_movies_page(movie_obj)

if __name__ == '__main__':
    main()
