import json

from cerberus import Validator
from jsonschema import validate

from services.v2.pet_service import get_pet
from test_base import TestBase
from util.file_reading import open_json


class TestSchemaValidation(TestBase):

    def test_demo(self):
        schema = open_json('pet_not_found.json')
        instance = get_pet(16788694, status_code=404).json

        validate(instance, schema)
