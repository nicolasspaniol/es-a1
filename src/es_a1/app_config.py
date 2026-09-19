from __future__ import annotations
from typing import ClassVar


class AppConfig:
    """
    App configuration class (singleton)

    Attributes:
        environment (str): defaults to 'production'
        currency (str): defaults to 'BRL'
        debug (bool): defaults to False

    """

    environment: str
    currency: str
    debug: bool

    _instance: ClassVar[AppConfig | None] = None
    _initialized: ClassVar[bool] = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if not self._initialized:
            self.environment = 'production'
            self.currency = 'BRL'
            self.debug = False

            AppConfig._initialized = True

