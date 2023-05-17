import requests

class DallEOpenAi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.openai.com/v1/images/generations"

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
            result = response.json()
            if "data" in result and len(result["data"]) > 0 and "url" in result["data"][0]:
                return result["data"][0]["url"]
            else:
                raise Exception("Failed to retrieve image URL from the response")
        else:
            raise Exception("Image generation failed")
