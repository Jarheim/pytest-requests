from services.v2.pet_model import PetRequest, Category
from services.v2.pet_service import add_pet
from test_base import TestBase


class TestPostClass(TestBase):

    def test_simple_json(self):
        assert 1 == 1

    def test_complex_json(self):
        category = Category(id=1)
        request = PetRequest(id=100, category=category)

        response = add_pet(request)
        assert response.body.id == request.id
