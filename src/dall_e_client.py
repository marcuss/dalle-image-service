import requests

class DallEClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.openai.com/v1/images"

    def generate_image(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "prompt": prompt,
            "num_images": 1
        }
        response = requests.post(self.endpoint, json=data, headers=headers)

        if response.status_code == 200:
            return response.json()["images"][0]["image"]
        else:
            raise Exception("Image generation failed")

api_key = "YOUR API KEY"
client = DallEClient(api_key)
prompt = "a cat sitting on a table"
image = client.generate_image(prompt)
print(image)
