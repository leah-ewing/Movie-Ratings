"""Models for movie ratings app."""
#Your routes are wonky!!!! They were working before you copy/pasted the other two codes
#but now they're not working anymore. All of your code is "correct" as per instructions(?)
#code is pressed about "user" specifically
#sqlalchemy.exc.ProgrammingError: (psycopg2.errors.UndefinedTable) relation "user" does not exist
#LINE 1: INSERT INTO "user" (email, password) VALUES ('test@test.test...
#you'll probably want to just go ahead and ask for help :D

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# Replace this with your code!


def connect_to_db(flask_app, db_uri='postgresql:///ratings', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

class User(db.Model):
    """A user."""

    __tablename__ = 'user'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    #added nullable variables, if issues arise, come here first! :)
    #took them away! you did indeed run into issue, as expected!

    

    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'

class Movie(db.Model):
    """A movie."""

    __tablename__ = 'movie'

    movie_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    

    def __repr__(self):
        return f'<Movie movie_id={self.movie_id} title={self.title}>'

class Ratings(db.Model):
    """A movie rating."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    movie = db.relationship('Movie', backref='ratings')
    user = db.relationship('User', backref='ratings')
    

    def __repr__(self):
        return f'<Ratings rating_id={self.rating_id} score={self.score}>'


if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
