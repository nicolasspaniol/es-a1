from abc import ABC, abstractmethod
from es_a1.order import Order


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        ...


class PixPayment(Payment):
    def pay(self, amount: float):
        ...


class CreditCardPayment(Payment):
    def pay(self, amount: float):
        ...


class BoletoPayment(Payment):
    def pay(self, amount: float):
        ...


# factories -------------------

class PaymentProcessor(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        ...

    def process_order(self, order: Order):
        return self.create_payment().pay(order.total())


class PixProcessor(PaymentProcessor):
    def create_payment(self):
        return PixPayment()


class CreditCardProcessor(PaymentProcessor):
    def create_payment(self):
        return CreditCardPayment()


class BoletoProcessor(PaymentProcessor):
    def create_payment(self):
        return BoletoPayment()
