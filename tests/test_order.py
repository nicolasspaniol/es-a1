import pytest
from es_a1.order import Product, OrderBuilder


def test_order_with_products_and_optional_fields():

    '''
    Verifica se a construção de um pedido com produtos e campos opcionais funciona corretamente.

    '''
    teclado = Product("Teclado", 100.0)

    mouse = Product("Mouse", 50.0)

    pedido = (
        OrderBuilder()
        .with_client("Maria Silva")
        .add_product(teclado)
        .add_product(mouse)
        .with_address("Rua Central 456")
        .with_coupon("PROMO10")
        .build()
    )

    assert pedido.client == "Maria Silva"
    assert pedido.products == [teclado, mouse]
    assert pedido.address == "Rua Central 456"
    assert pedido.coupon == "PROMO10"
    assert pedido.total() == pytest.approx(150.0)


def test_order_without_client_raises_error():
    '''
    Verifica se a construção de um pedido sem cliente levanta um ValueError.
    
    '''
    builder = (
        OrderBuilder()
        .add_product(Product("Teclado", 100.0))
    )

    with pytest.raises(
        ValueError,
        match="O pedido precisa ter um cliente",
    ):
        builder.build()