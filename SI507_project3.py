import os
from flask import Flask, render_template, session, redirect, url_for # tools that will make it easier to build on things
from flask_sqlalchemy import SQLAlchemy # handles database stuff for us - need to pip install flask_sqlalchemy in your virtual env, environment, etc to use this and run this

# Application configurations
app = Flask(__name__)
app.debug = True
app.use_reloader = True
app.config['SECRET_KEY'] = 'qwertasdfghzxcvbnm'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./SI507_project3.db' # TODO: decide what your new database name will be -- that has to go here
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Set up Flask debug stuff
db = SQLAlchemy(app) # For database use
session = db.session # to make queries easy




######### Everything above this line is important/useful setup, not problem-solving.



##### Set up Models #####


class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    ratings_id = db.Column(db.Integer,db.ForeignKey("ratings.id"))
    ratings = db.relationship("Rating", backref=db.backref("movies", uselist=False))

    title = db.Column(db.String(64))
    #US_gross = db.Column(db.Float)
    #Worldwide_gross = db.Column(db.Float)
    #USDVD_sales = db.Column(db.Float)
    #production_budget = db.Column(db.Float)
    #release_date = db.Column(db.String(64))
    #running_time = db.Column(db.Integer)
    distributor_id  = db.Column(db.Integer, db.ForeignKey("distributors.id"))
    #source = db.Column(db.String(64))
    major_genre = db.Column(db.String(64))
    #creative_type = db.Column(db.String(64))
    director_id = db.Column(db.Integer, db.ForeignKey("directors.id"))




class Rating(db.Model):
    __tablename__ = "ratings"
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(64))
    MPAA_rating = db.Column(db.String(64))
    IMDB_rating = db.Column(db.Float)




class Distributor(db.Model):
    __tablename__ = "distributors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    headquarter_location = db.Column(db.String(64))

    movies = db.relationship('Movie',backref=db.backref("Distributor"))



class Director(db.Model):
    __tablename__ = "directors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    Nationality = db.Column(db.String(64))

    movies = db.relationship('Movie',backref=db.backref("Director"))



##### Helper functions #####

### For database additions
### Relying on global session variable above existing

def get_or_create_distributor(distributor_name):
    distributor = Distributor.query.filter_by(name=distributor_name).first()
    if distributor:
        return distributor
    else:
        distributor = Distributor(name=distributor_name)
        session.add(distributor)
        session.commit()
        return distributor

def get_or_create_rating(title,IMDB_rating):
    rating = Rating.query.filter_by(title=title).first()
    if rating:
        return rating
    else:
        rating = Rating(title=title, IMDB_rating=IMDB_rating)
        session.add(rating)
        session.commit()
        return rating


def get_or_create_director(director_name):
    director = Director.query.filter_by(name=director_name).first()
    if director:
        return director
    else:
        director = Director(name=director_name)
        session.add(director)
        session.commit()
        return director

##### Set up Controllers (route functions) #####

## Main route
@app.route('/')
def index():
    movies = Movie.query.all()
    num_movies = len(movies)
    return render_template('index.html', num_movies=num_movies)

#Add new movies
@app.route('/movie/new/<title>/<IMDB_rating>/<distributor_name>/<major_genre>/<director_name>/')
def new_movie(title, IMDB_rating, distributor_name, major_genre, director_name):
    if Movie.query.filter_by(title=title).first(): # if there is a song by that title
        return "That Movie already exists. Please go back to the main app!"
    else:
        distributor = get_or_create_distributor(distributor_name)
        rating = get_or_create_rating(title,IMDB_rating)
        director = get_or_create_director(director_name)

        movie = Movie(title=title, ratings_id=rating.id, distributor_id= distributor.id, director_id = director.id, major_genre=major_genre)
        session.add(movie)
        session.commit()
        return "New Movie: {} by {}. Distributed by {}. Check out the URL for ALL movies to see the whole list.".format(movie.title, director.name, distributor.name)

#Show all movies
@app.route('/all_movies')
def see_all():
    all_movies = []
    movies = Movie.query.all()
    for s in movies:
        director = Director.query.filter_by(id=s.director_id).first()
        distributor = Distributor.query.filter_by(id=s.distributor_id).first()
        rating = Rating.query.filter_by(id=s.ratings_id).first()
        all_movies.append((s.title,rating.IMDB_rating, s.major_genre, director.name,distributor.name)) # get list of songs with info to easily access [not the only way to do this]
    return render_template('all_movies.html',all_movies=all_movies) # check out template to see what it's doing with what we're sending!

#Add new directors
@app.route('/director/new/<name>/<nationality>/')
def new_director(name, nationality):
    if Director.query.filter_by(name=name).first(): # if there is a director by that name
        return "This Director already exists."
    else:
        director = Director(name=name, Nationality=nationality)
        session.add(director)
        session.commit()
        return "New Director: {} -- {}.".format(director.name, director.Nationality)



if __name__ == '__main__':
    db.create_all() # This will create database in current directory, as set up, if it doesn't exist, but won't overwrite if you restart - so no worries about that
    app.run() # run with this: python main_app.py runserver

