from rest.abstract_rest_client import RestClient
from rest.url_handler import endpoint
from services.v2.pet_model import PetRequest

restClient = RestClient()
endpoint = endpoint()


def get_pet(petId, status_code=200):
    url = endpoint.v2.get_pet.format(petId=petId)
    return restClient.get(url, status_code)


def add_pet(pet_request=PetRequest, status_code=200):
    url = endpoint.v2.add_pet
    return restClient.post(url, object=pet_request, status_code=status_code)


def add_pet_simple(json, status_code=200):
    url = endpoint.v2.add_pet
    return restClient.post(url, json=json, status_code=status_code)
