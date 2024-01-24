import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)

# Instantiate the GetRequester class
get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')

# Send HTTP GET request and load JSON
result = get_requester.load_json()

# Print the result
print(result)
