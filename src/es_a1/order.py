from itertools import product
from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass

# this avoids circular imports while preserving typing; payment.py already imports order.py
if TYPE_CHECKING:
    from es_a1.payment import PaymentProcessor


@dataclass(eq=False)
class Product:
    name: str
    price: float


@dataclass(eq=False)
class Order:
    client: str
    products: list[Product]
    address: Optional[str]
    coupon: Optional[str]
    payment_type: Optional[PaymentProcessor]
    observation: Optional[str]

    def total(self) -> float:
        return sum(product.price for product in self.products )


class OrderBuilder:
    def __init__(self):
        self._client = None
        self._products = []
        self._address = None
        self._coupon = None
        self._payment_type = None
        self._observation = None

    def with_client(self, client: str):
        self._client = client
        return self

    def add_product(self, product: Product):
        self._products.append(product)
        return self

    def with_address(self, address: str):
        self._address = address
        return self

    def with_coupon(self, coupon: str):
        self._coupon = coupon
        return self

    def with_payment_type(self, payment_type: PaymentProcessor):
        self._payment_type = payment_type
        return self

    def with_observation(self, observation: str):
        self._observation = observation
        return self

    def build(self) -> Order:
        if not self._client:
            raise ValueError("O pedido precisa ter um cliente.")
        
        return Order(
            self._client, 
            self._products, 
            self._address, 
            self._coupon, 
            self._payment_type, 
            self._observation
        )
