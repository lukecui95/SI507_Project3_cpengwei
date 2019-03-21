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

