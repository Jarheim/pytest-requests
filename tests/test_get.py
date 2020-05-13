from services.v2.pet_model import PetRequest, Category
from services.v2.pet_service import get_pet, add_pet
from test_base import TestBase

a_pet = PetRequest(id=150, category=Category(id=1))


class TestGetClass(TestBase):
    pet = None

    @classmethod
    def setup_class(self):
        self.pet = add_pet(a_pet).body

    def test_pet_not_found(self):
        response = get_pet(1678, status_code=404)
        assert response.body.message == "Pet not found"

    def test_pet_found(self):
        response = get_pet(self.pet.id)
        assert response.body.name == self.pet.name
        assert response.body.category.id == self.pet.category.id
