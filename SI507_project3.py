

# Set up application
app = Flask(__name__)

# Routes
@app.route('/')
def home_page():
    num_movies = Movie
    return '<h1> {} movies recorded</h1>'.format(num_movies.num_records)
    #(Return how many movies are in the movies_clean.csv file!)


@app.route('/movies/ratings/')
def movies_ratings():

    #Create instance movies_list
    movies = Movie(movies_clean,0)

    #Get 10 movies and their IMBD ratings
    movies_list = movies.get_movies_ratings(10)

    return render_template("movies_ratings.html",rating_list = movies_list)

#This route can get 5 movies with IMDB ratings greater than or equal to <rating>.
#Please limit <rating> from 0 to 8.5.
@app.route('/movies/ratings/<rating>')
def get_top_rated(rating):
    num =float(rating)

    #Create instance movies_list
    movies = Movie(movies_clean,0)

    # Get 5 movies with IMDB rating greater than or equal to rating
    movies_list = movies.get_top_rated(num)

    return render_template("movies_top_rated.html",rating_list = movies_list,num = num)




if __name__ == "__main__":
    app.run()
