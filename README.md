RequestWatch

RequestWatch is a simple Django middleware that logs all incoming requests to your Django application, along with their HTTP method, URL, and timestamp. This middleware can be useful for debugging or monitoring purposes.
Installation

RequestWatch can be installed via pip:

pip install request-watch

Usage

To use RequestWatch, add it to the MIDDLEWARE list in your Django project's settings.py file:

python

MIDDLEWARE = [
    # ...
    'request_watch.middleware.RequestWatchMiddleware',
    # ...
]

RequestWatch will automatically log all incoming requests to your Django application.
Contributing

If you find a bug or have an idea for a new feature, please open an issue on the GitHub repository. Pull requests are also welcome.
License

RequestWatch is released under the MIT License. See LICENSE for details.