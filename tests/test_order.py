from es_a1.order import Product, OrderBuilder


# TODO: mudar nome da funcao
def test_order_():
    pedido = (OrderBuilder()
              .with_client("Maria Silva")
              .add_product(Product("Teclado", 100.0))
              .with_address("Rua Central 456")
              .build())
    
    assert pedido.client == "Maria Silva", "Error cliente"
    assert pedido.address == "Rua Central 456", "Error endereco"