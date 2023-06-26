from masonite.controllers import Controller
from masonite.views import View
from masonite.request import Request
from masonite.response import Response
from app.models.Post import Post
from time import sleep

class PostController(Controller):
    def show(self, view: View):
        posts = Post.all()

        return view.render("posts", { "posts": posts })

    def single(self, view: View, request: Request):
        post = Post.find(request.param('id'))

        return view.render('single', {'post': post})
    
    def update(self, view: View, request: Request):
        post = Post.find(request.param('id'))

        return view.render('update', {'post': post})

    def store(self, request: Request, response: Response):
        post = Post.find(request.param('id'))

        post.title = request.input('title')
        post.body = request.input('body')

        post.save()

        print("post updated!")
        sleep(1)

        return response.redirect(name='update', params={ 'id': request.param('id') })
    
    def delete(self, request: Request, response: Response):
        post = Post.find(request.param('id'))

        post.delete()

        print("post deleted!")
        sleep(1)

        return response.redirect(name='posts')
    