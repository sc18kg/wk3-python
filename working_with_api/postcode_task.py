import requests
from pprint import pprint
import json


class PostCode:
    def __init__(self, postcode_json_dict):
        self.postcode = postcode_json_dict["postcode"]
        self.lat = postcode_json_dict["latitude"]
        self.long = postcode_json_dict["longitude"]
        self.eastings = postcode_json_dict["eastings"]
        self.northings = postcode_json_dict["northings"]

    def __repr__(self):
        return f"Postcode({self.postcode})"

    def get_location(self, en=False):
        if en:
            return self.eastings, self.northings
        return self.lat, self.long