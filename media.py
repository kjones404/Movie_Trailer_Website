import webbrowser

# Create Class Movie to store movie title, release date, rating, poster image, and trailer
class Movie(object):
    def __init__(self, movie_title, movie_date, movie_summary, poster_image, trailer_youtube):
        """ creates a movie object with title, date, rating, poster image, and trailer
        Args:
            movie_title (str): Holds the title of the movie_title.
            movie_date (str): Holds the movie release date.
            movie_rating (str): Holds the movie rating.
            poster_image (str): Holds the url of the poster image.
            trailer_youtube (str): holds the url of the movie trailer on youtube.com
        Returns:
            a movie object"""
        self.title = movie_title
        self.date = movie_date
        self.summary = movie_summary
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
