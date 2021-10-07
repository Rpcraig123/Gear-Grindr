from datetime import datetime
from models.db import db


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    post = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=str(
        datetime.utcnow()), nullable=False)

    def __init__(self, username, post):
        self.username = username
        self.post = post

    def json(self):
        return {"id": self.id, "username": self.username, "post": self.post, "created_at": str(self.created_at)}

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        return Post.query.all()

    @classmethod
    def find_by_all(cls, post_id):
        post = Post.query.filter_by(id=post_id).first()
        return post
