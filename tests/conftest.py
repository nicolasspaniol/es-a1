import pytest
from es_a1.app_config import AppConfig


@pytest.fixture(autouse=True)
def reset_singleton():
    AppConfig._instance = None
    AppConfig._initialized = False

