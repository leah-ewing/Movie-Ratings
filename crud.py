"""CRUD operations."""

from model import db, User, Movie, Ratings, connect_to_db

# Functions start here!

def create_user(email, password):
    """Create and return a new user."""

    user = User(email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

  

def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie."""

    movie = Movie(title = title,
                overview = overview,
                release_date = release_date,
                poster_path = poster_path)

    db.session.add(movie)
    db.session.commit()

    return movie

def get_movies():
    """Create and return a new movie."""

    return Movie.query.all()
    #your links aren't showing up! but you're at step "Your task" PT 3
    #"view list of all movies"

def create_rating(user, movie, score):
    """Create and return a new rating."""

    rating = Ratings(user=user, movie=movie, score=score)

    db.session.add(rating)
    db.session.commit()

    return rating





if __name__ == '__main__':
    from server import app
    connect_to_db(app)