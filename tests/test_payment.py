import pytest
from es_a1.payment import PixProcessor, CreditCardProcessor
from es_a1.order import OrderBuilder, Order


@pytest.fixture
def order():
    return OrderBuilder().com_cliente('Cliente').build()


@pytest.mark.parametrize("processor_cls", [PixProcessor, CreditCardProcessor])
def test_payment_order_processing(order: Order, processor_cls):
    processor = processor_cls()
    processor.process_order(order)


@pytest.mark.parametrize("processor_cls", [PixProcessor, CreditCardProcessor])
def test_payment_method_follows_order(order: Order, processor_cls):
    processor = processor_cls()
    processor.process_order(order)
    assert order.tipo_pagamento == processor # see payment.py
