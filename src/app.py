import os
from signal import signal, SIGINT
from flask import Flask, render_template
from image_api import ImageAPI

class MyApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.image_api = ImageAPI()
        self.image_api.add_to_app(self.app)

        @self.app.route('/')
        def hello():
            """Return a simple HTML page with a friendly message."""
            message = "It's running!"
            return render_template('index.html', message=message)

    def run(self):
        signal(SIGINT, self.handler)
        server_port = os.environ.get('PORT', '8080')
        self.app.run(debug=False, port=server_port, host='0.0.0.0')

    def handler(self, signal_received, frame):
        # SIGINT or ctrl-C detected, exit without error
        exit(0)

if __name__ == '__main__':
    my_app = MyApp()
    my_app.run()
