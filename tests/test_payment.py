import pytest
from es_a1.payment import PixProcessor, CreditCardProcessor
from es_a1.order import OrderBuilder


@pytest.mark.parametrize("processor_cls", [PixProcessor, CreditCardProcessor])
def test_payment_order_processing(processor_cls):
    order = OrderBuilder().com_cliente('Cliente').build()

    processor = processor_cls()
    processor.process_order(order)


def test_payment_method_follows_order():
    ...
