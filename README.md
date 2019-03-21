# Project 3 - SQLAlchemy database in Flask - Pengwei Cui

In this project, I write a small Flask application that includes a database to hold data about movies. 

My movie database contains four tables and my Flash application has four routes. Each of those routes has some specific uses.

All my codes are included in file SI507_project3.py.


## SI507_project3.py

### Four tables in my database

There are four tables in my database. 

The first table is Movie. This table stores the information of movies, including movie titles, movies' IMDB ratings, distributor's ID, major genres and director's ID.

The second table is Rating. This table stores the information of movies' ratings, including movie titles, MPAA ratings and IMDB ratings. Table Movie and table Rating have a one to one relationship.

The third table is Distributor. This table contains the information of distributors, including distributor names and their headquarter locations. Table Distributor and table Movie have a one to many relationship.

The last table is Director. This table contains the information of directors, including director names and their nationalities. Table Director and table Movie also have a one to many relationship.

### Four routes in my Flash application

I designed four routes in my Flash application.

The first route is the home page. It shows how many movies were stored in my database.

My second route is used to add new movies. You need to enter specific paths in order to add new movies in the Movie table.

The third route is used to show all movies' information in my database.

The last route is designed for adding new directors in our database. You also need to enter specific URLs to add new directors.

## Templates

There are two html files in the templates folder. These two html files are used to display contents for the first and third routes.

## How to run my Flash application

1) cd to the place you saved our files, and then type at the command prompt:
python SI507_project3.py runserver

2) Without doing anything else, in a web a browser, type in and check out this URL: "http://127.0.0.1:5000/" 

Since you haven't stored any movies in the database.

It should display:

0 movies saved.



3) Change the ULR to : "http://127.0.0.1:5000/movie/new/<title>/<IMDB_rating>/<distributor_name>/<major_genre>/<director_name>/". 

Change <title>, <IMDB_rating>, <distributor_name>, <major_genre> and <director_name> to what you want. This route will add new movies in our database.

However, if the movie is already in our database, it should display:

That Movie already exists. Please go back to the main app!

If not, for example, if I enter : http://127.0.0.1:5000/movie/new/Hunger games 1/8.2/Warner Bros/drama/Chris Cedar/ , it should display:

New Movie: Hunger games 1 by Chris Cedar. Distributed by Warner Bros. Check out the URL for ALL movies to see the whole list.


 
4) Change the URL to "http://127.0.0.1:5000/all_movies".

It should display (movies in your database):

Rush hours by Jackie Chen - action              IMDB Rating: 8.1      Distributed by Warner Bros
Happy Death Day 1 by James Pratt - thriller     IMDB Rating: 6.5      Distributed by Fox
Rush hours 1 by Jackie Chen - action            IMDB Rating: 7.9      Distributed by Warner Bros
Mission D by Jay Chou - drama                   IMDB Rating: 5.1      Distributed by Enlight Pictures
Hunger games 1 by Chris Cedar - drama           IMDB Rating: 8.2      Distributed by Warner Bros
 

4) Change the URL to "http://127.0.0.1:5000/director/new/<name>/<nationality>/". Change <name> and <nationality> to whoever director you want.

However, if the director is already in our database, it should display:

This Director already exists.

If not, it should display(something like this):

New Director: Wilson White -- England.



## Use requirements.txt to set your virtual environment

1)Create a virtual environment

python3 -m venv project3-env

2)Activate your virtual environment

source project3-env/bin/activate    # For Mac/Linux...

source project3-env/Scripts/activate    # For Windows

3)Install all requirements

pip install -r requirements.txt


4)Try our Flash app

See "How to run our Flash app"

5)Deactivate

deactivate

## SI507_movies_database_plan

I designed four tables in the diagram, which are Movie, Rating, Distributor and Director.
See details below:

![Test Image 6](https://github.com/lukecui95/SI507_Project3_cpengwei/blob/master/SI507_movies_database.png)

