from flask_restful import Resource
from flask import request
from models.post import Post
from models.db import db

class PostList(Resource):
    # get all posts
    def get(self):
        data = Post.find_all()
        results = [u.json() for u in data]
        return results 
    # new post
    def post(self):
        data = request.get_json()
        post = Post(**data)
        post.create()
        return post.json(), 201
class Posts(Resource):
    # get post by id
    def get(self,id):
        data = Post.find_by_all(id)
        return data.json()
    
    # delete post by id
    def delete(self,id):
        post = Post.find_by_all(id)
        if not post:
            return {"msg": "Not found"}, 404
        db.session.delete(post)
        db.session.commit()
        msg = 'post {id} deleted'.format(id=id)
        return msg