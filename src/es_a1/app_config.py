from __future__ import annotations
from typing import ClassVar


class AppConfig:
    environment: str
    currency: str
    debug: bool

    _instance: ClassVar[AppConfig | None] = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        self.environment = 'production'
        self.currency = 'BRL'
        self.debug = False

