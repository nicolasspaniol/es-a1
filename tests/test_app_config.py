import pytest
from es_a1.app_config import AppConfig


def test_app_config_uniqueness():
    a = AppConfig()
    b = AppConfig()
    assert a is b


def test_app_config_change_propagates():
    a = AppConfig()
    b = AppConfig()

    assert not a.debug
    a.debug = True
    assert b.debug


def test_app_config_change_not_overwritten():
    a = AppConfig()
    assert not a.debug
    a.debug = True

    b = AppConfig()
    assert b.debug
