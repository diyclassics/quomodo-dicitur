from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Entry', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    english_word = db.Column(db.String, index=True, unique=True)
    latin_top_choice = db.Column(db.String, index=True)
    username = db.Column(db.String)
    body = db.Column(db.String(140))
    tweet_date = db.Column(db.DateTime)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Entry {}>'.format(self.english_word)
