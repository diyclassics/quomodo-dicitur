from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5

from datetime import datetime

from app.twitteri import get_tweet_id, get_tweet_screenname, get_tweet_text, get_tweet_date

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Entry', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)

    def submitted_entries(self):
        submitted = Entry.query.filter_by(user_id=self.id)
        return submitted.order_by(Entry.timestamp.desc())

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    definitions = db.relationship('Definitions', backref='entry', lazy='dynamic')
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
        self.tweet_username = get_tweet_id(url)

    def set_tweet_screenname(self, id):
        self.username = get_tweet_screenname(id)

    def set_tweet_text(self, id):
        self.body = get_tweet_text(id)

    def set_tweet_id(self, id):
        self.tweet_date = get_tweet_date(id)

    def __repr__(self):
        return '<Entry {}>'.format(self.english_word)


class Definitions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    latin_word = db.Column(db.String, index=True)
    tweet_id = db.Column(db.String, index=True)
    username = db.Column(db.String)
    body = db.Column(db.String(140))
    tweet_date = db.Column(db.DateTime)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    entry_id = db.Column(db.Integer, db.ForeignKey('entry.id'))
    votes = db.Column(db.Integer, default=0)
    #
    # def set_tweet_id(self, url):
    #     self.tweet_username = get_tweet_id(url)
    #
    # def set_tweet_screenname(self, id):
    #     self.username = get_tweet_screenname(id)
    #
    # def set_tweet_text(self, id):
    #     self.body = get_tweet_text(id)
    #
    # def set_tweet_id(self, id):
    #     self.tweet_date = get_tweet_date(id)
    #
    # def __repr__(self):
    #     return '<Definitions {}>'.format(self.latin_word)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
