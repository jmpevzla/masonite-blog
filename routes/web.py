from masonite.routes import Route
from masonite.authentication import Auth

ROUTES = [
    Route.get("/", "WelcomeController@show").name("welcome"),

    # Blog Routes
    Route.get("/blog", "BlogController@show").name("blog"),
    Route.post("/blog/create", "BlogController@store"),

    Route.get("/posts", "PostController@show").name("posts"),

    Route.get('/post/@id', 'PostController@single').name("single"),

    Route.get('/post/@id/update', 'PostController@update').name("update"),
    Route.post('/post/@id/update', 'PostController@store'),

    Route.get('/post/@id/delete', 'PostController@delete'),
]

ROUTES += Auth.routes()
