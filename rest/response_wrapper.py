import json

from addict import Dict
from requests import Response


def parse_body(text):
    dict = json.loads(text)
    return Dict(dict)


class ResponseWrapper(Response):
    def __init__(self, response=Response):
        self.wrapped_response = response
        self.status_code = response.status_code
        self.body = parse_body(response.text)
        self.json = json.loads(response.text)
