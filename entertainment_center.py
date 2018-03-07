import media
import fresh_tomatoes

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
