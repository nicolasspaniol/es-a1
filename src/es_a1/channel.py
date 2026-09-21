from abc import ABC, abstractmethod
from es_a1.order import Order


class Checkout(ABC):
    @abstractmethod
    def show(self, order: Order):
        pass


class Notification(ABC):
    @abstractmethod
    def send(self, order: Order):
        pass


class WebCheckout(Checkout):
    def show(self, order: Order):
        print("=== CHECKOUT WEB ===")
        print(f"Cliente: {order.cliente}")
        print(f"Total: R$ {order.total():.2f}")
        print(f"Forma de pagamento: {order.tipo_pagamento}")


class WebNotification(Notification):
    def send(self, order: Order):
        print(
            f"Notificacao WEB enviada para "
            f"{order.cliente}. Pedido no valor de "
            f"R$ {order.total():.2f}."
        )


class MobileCheckout(Checkout):
    def show(self, order: Order):
        print("=== CHECKOUT MOBILE ===")
        print(f"Cliente: {order.cliente}")
        print(f"Total: R$ {order.total():.2f}")
        print(f"Forma de pagamento: {order.tipo_pagamento}")


class MobileNotification(Notification):
    def send(self, order: Order):
        print(
            f"Notificacao MOBILE enviada para "
            f"{order.cliente}. Pedido no valor de "
            f"R$ {order.total():.2f}."
        )

# abstract factory

class ChannelFactory(ABC):
    @abstractmethod
    def create_checkout(self) -> Checkout:
        pass

    @abstractmethod
    def create_notification(self) -> Notification:
        pass


class WebFactory(ChannelFactory):
    def create_checkout(self) -> Checkout:
        return WebCheckout()

    def create_notification(self) -> Notification:
        return WebNotification()


class MobileFactory(ChannelFactory):
    def create_checkout(self) -> Checkout:
        return MobileCheckout()

    def create_notification(self) -> Notification:
        return MobileNotification()