from flask_restful import Resource
from flask import request
from models.post import Post

class PostList(Resource):
    # get all posts
    def get(self):
        msg = 'Resource good'
        return msg 
    # new post
    def post(self):
        pass
class Post(Resource):
    # get post by id
    def get(self,id):
        pass 
    
    # delete post by id
    def delete(slef,id):
        pass