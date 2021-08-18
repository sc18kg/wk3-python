from postcode_app.config_manager import BASE_URL
from postcode_app.models.single_postcode import PostCode
import requests

class PostcodeManager:
    def __init__(self, postcode: str):
        self.url = BASE_URL + "postcodes/" + postcode
        self.request = requests.get(self.url)
        self.headers = self.request.headers
        self.response_json = self.request.json()

    def get_postcode(self):
        return PostCode(self.response_json['result'])
        
if __name__ == "__main__":
    pm = PostcodeManager("B7 4BB")
    print(pm.get_postcode())
