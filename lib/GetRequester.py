import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Send the HTTP GET request and hand back the raw response payload.
        # .content gives us the un-decoded bytes, which is what the tests compare against.
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        # The response body arrives as a JSON formatted byte string, so parse it
        # into native Python objects (a list of dicts) before returning it.
        return json.loads(self.get_response_body())