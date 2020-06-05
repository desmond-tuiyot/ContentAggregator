from content_aggregator.content_frontend import db


class Post(db.Model):
    __name__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    link = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    source_id = db.Column(db.Integer, db.ForeignKey('source.id'), nullable=False)
    # content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Source(db.Model):
    __name__ = 'source'
    id = db.Column(db.Integer, primary_key=True)
    source_name = db.Column(db.String, nullable=False, unique=True)
    link = db.Column(db.String, nullable=False)
    posts = db.relationship('Post', backref='source', lazy=True)


