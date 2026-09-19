from abc import ABC, abstractmethod
from es_a1.order import Order


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: int):
        ...


class PixPayment(Payment):
    def pay(self, amount: int):
        ...


class CreditCardPayment(Payment):
    def pay(self, amount: int):
        ...


class BoletoPayment(Payment):
    def pay(self, amount: int):
        ...


# factories -------------------

class PaymentProcessor(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        ...

    @abstractmethod
    def process_order(self, order: Order):
        ...


class PixProcessor(PaymentProcessor):
    def create_payment(self):
        return PixPayment()

    def process_order(self, order: Order):
        return self.create_payment().pay(order.total())


class CreditCardProcessor(PaymentProcessor):
    def create_payment(self):
        return CreditCardPayment()

    def process_order(self, order: Order):
        return self.create_payment().pay(order.total())


class BoletoProcessor(PaymentProcessor):
    def create_payment(self):
        return BoletoPayment()

    def process_order(self, order: Order):
        return self.create_payment().pay(order.total())
