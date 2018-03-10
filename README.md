# Movie Trailer Website

This project is for the Udacity Full Stack nanodegree program. The goal of this project is to create a movie trailer website with the use of 3 files:

* entertainment_center.py
* media.py
* fresh_tomatoes.py

** entertainment_center.py:** Creates multiple instances of the Movie class and then calls on fresh_tomatoes.py to generate the movie trailer website.

** media.py:** Creates the data structure for the Movie class. This includes data such as movie title, release year, plot summary, poster, and trailer hosted by YouTube.

** fresh_tomatoes.py:** Uses the class objects obtained from entertainment_center.py to generate the movie trailer website.

## Before You Get Started

* This code was created using python 3.6.4. Please make sure you have the correct version of python installed before attempting to run this program. For more information on how to download python please check [Beginners Guide to Download Python](https://wiki.python.org/moin/BeginnersGuide/Download).

* This program also gathers it's movie information from The Movie Database API. In order to use this code you will need to first obtain an API Key from TMDb. To find more information about their API please check [TMDb API Overview](https://www.themoviedb.org/documentation/api).

## Getting Started

After you download the repository, you will need to update entertainment_center.py with your API key from TMDb.

Within the *get_db_url()* function you will find the following line of code:
```
tmdb_key = "api_key"  # add TMDb API Key (v3 auth) string here
```
Update *tmdb_key* to your TMDb API key and save changes. After you have updated entertainment_center.py, navigate to this repository and run entertainment_center.py.

## Modify the Program

### Movie List
To change the list of movies you will need the Movie ID from TMDb. For more details on how to find the Movie ID [Click Here.](https://developers.themoviedb.org/3/getting-started/search-and-query-for-details)

Once you have the ID of a movie you would like to add to the program you will need to open entertainment_center.py and find the *main()* function.
```
tmdb_id = ["18", "245891", "118340", "2493", "43074", "1542"]
```
When you find *tmdb_id* update the list to contain the new Movie ID.
