import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
        response = requests.get(url)
        return response.content
        pass

    def load_json(self):

        programs_list = []
        programs = json.loads(self.get_response_body())
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list  

        pass
programs = GetRequester()
programs_schools = programs.load_json()

for school in set(programs_schools):
    print(school)