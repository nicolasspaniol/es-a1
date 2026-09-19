from es_a1.app_config import AppConfig


def test_app_config_uniqueness():
    a = AppConfig()
    b = AppConfig()
    assert a is b
