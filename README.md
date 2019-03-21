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

The last route is designed for adding new directors in our database. You also need to enter specific URLS to add new directors.

## Templates

There are two html files in the templates folder. These two html files are used to display contents for the first and third routes.

## How to run my Flash application

## Use requirements.txt to set your virtual environment

## SI507_movies_database_plan
