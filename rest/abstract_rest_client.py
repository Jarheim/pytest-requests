import jsonpickle

from config import Configuration
from rest.response_wrapper import ResponseWrapper
from rest.rest_session import RestSession
import json as j

config = Configuration()


class RestClient:

    def post(self, url, object=None, json=None, status_code=200, **kwargs):
        if object is not None:
            json_object = jsonpickle.encode(object, unpicklable=False)
            json = j.loads(json_object)

        response = self.restSession.post(url, json=json, **kwargs)
        assert response.status_code == status_code
        return ResponseWrapper(response)

    def get(self, url, status_code=200, **kwargs):
        response = self.restSession.get(url, **kwargs)
        assert response.status_code == status_code
        return ResponseWrapper(response)

    def __init__(self):
        self.restSession = RestSession(config.SERVER)
