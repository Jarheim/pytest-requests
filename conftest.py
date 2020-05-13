import logging

import pytest

logging.basicConfig(level=logging.DEBUG)


def pytest_addoption(parser):
    parser.addoption('--settings', action='store')


@pytest.fixture(scope="session", autouse=True)
def before_all(request):
    """
    """


def after_all(session, exitstatus):
    """
    """
