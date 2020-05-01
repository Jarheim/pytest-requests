import pytest

from test_base import TestBase
from various_methods import VariousMethods

variousMethods = VariousMethods()

@pytest.mark.smoke
class TestClass(TestBase):

    def test_convert_to_atlas_string(self):
        actual = variousMethods.ConvertToAtlasCopcoString(15)
        assert actual == "AtlasCopco"

    def test_convert_to_atlas_string_again(self):
        actual = variousMethods.ConvertToAtlasCopcoString(15)
        assert actual == "AtlasCopco"