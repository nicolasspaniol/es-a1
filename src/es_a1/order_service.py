from es_a1.channel import ChannelFactory
from es_a1.order import Order


class OrderService:
    def __init__(self, factory: ChannelFactory):
        self._checkout = factory.create_checkout()
        self._notification = factory.create_notification()

    def process_order(self, order: Order) -> None:
        processor = order.payment_type

        if processor is None:
            raise ValueError(
                "O pedido precisa ter uma forma de pagamento."
            )

        self._checkout.show(order)
        processor.process_order(order)
        self._notification.send(order)