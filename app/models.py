from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.twitteri import get_tweet_id

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Entry', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    english_word = db.Column(db.String, index=True, unique=True)
    latin_top_choice = db.Column(db.String, index=True)
    tweet_id = db.Column(db.String, index=True)
    username = db.Column(db.String)
    body = db.Column(db.String(140))
    tweet_date = db.Column(db.DateTime)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def set_tweet_id(self, url):
        self.tweet_id = get_tweet_id(url)

    def __repr__(self):
        return '<Entry {}>'.format(self.english_word)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
