from datetime import datetime
from content_aggregator.content_frontend import db
# from flask_login import UserMixin


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable=False)
    # content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Source(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    source_name = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', backref='source', lazy=True)


# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))


# class User(db.Model, UserMixin):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
#     password = db.Column(db.String(60), nullable=False)
#     posts = db.relationship('Post', backref='author', lazy=True)
#
#     def __repr__(self):
#         return f"User('{self.username}', '{self.email}', '{self.image_file}')"



