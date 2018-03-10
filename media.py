""" Create Class Movie

Movie holds: movie title, release date, summary, poster image, and trailer.

"""


class Movie(object):
    def __init__(self, movie_title, movie_date, movie_summary, poster_image,
                 trailer_youtube):
        """ Creates a movie object
        Args:
            movie_title (str): Holds the title of the movie_title.
            movie_date (str): Holds the movie release year.
            movie_summary (str): Holds the movie summary.
            poster_image (str): Holds the url of the poster image.
            trailer_youtube (str): holds the url of the movie trailer
        Returns:
            a movie object
        """
        self.title = movie_title
        self.date = movie_date
        self.summary = movie_summary
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
