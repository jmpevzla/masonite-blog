from masonite.controllers import Controller
from masonite.request import Request
from masonite.response import Response
from masonite.views import View
from app.models.Post import Post
from time import sleep

class BlogController(Controller):
    def show(self, view: View):
        return view.render("blog")

    def store(self, request: Request, response: Response):
        Post.create(
            title=request.input('title'),
            body=request.input('body'),
            author_id=request.user().id,
        )

        print("post created!")
        sleep(1)

        return response.redirect(name='blog')
