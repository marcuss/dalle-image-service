from flask import Blueprint, jsonify, render_template, request
from dall_e_openai import DallEOpenAi

class ImageAPI:
    def __init__(self):
        self.blueprint = Blueprint('image_api', __name__, url_prefix='/v1')
        self.dalle_client = DallEOpenAi("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")  # Replace with your actual API key

        @self.blueprint.route('/image', methods=['GET'])
        def get_image():
            prompt = request.args.get('prompt', default='', type=str)  # Get the prompt from the request query parameters
            image = self.dalle_client.generate_image(prompt)

            return jsonify({'image_url': image})

        @self.blueprint.route('/image/show', methods=['GET'])
        def show_image():
            prompt = request.args.get('prompt', '')  # Get the 'prompt' query parameter from the request
            image = self.dalle_client.generate_image(prompt)

            # Render the 'image.html' template and pass the 'image' variable as a parameter
            return render_template('image.html', image=image, prompt=prompt)

    def add_to_app(self, app):
        app.register_blueprint(self.blueprint)
