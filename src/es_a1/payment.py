from abc import ABC, abstractmethod
from es_a1.order import Order


class Payment(ABC):
    @abstractmethod
    def pay(self, amount: float):
        ...


class PixPayment(Payment):
    def pay(self, amount: float):
        print(f'Pago via Pix: {amount:.2f}')


class CreditCardPayment(Payment):
    def pay(self, amount: float):
        print(f'Pago via cartão de crédito: {amount:.2f}')


class BoletoPayment(Payment):
    def pay(self, amount: float):
        print(f'Pago via boleto: {amount:.2f}')


# factories -------------------

class PaymentProcessor(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        ...

    def process_order(self, order: Order):
        self.create_payment().pay(order.total())

        # did this so as to be able to verify payment type compliance
        order.tipo_pagamento = self


class PixProcessor(PaymentProcessor):
    def create_payment(self):
        return PixPayment()


class CreditCardProcessor(PaymentProcessor):
    def create_payment(self):
        return CreditCardPayment()


class BoletoProcessor(PaymentProcessor):
    def create_payment(self):
        return BoletoPayment()
