from es_a1.order import Product, OrderBuilder


# TODO: mudar nome da funcao
def test_order_():
    pedido = (OrderBuilder()
              .com_cliente("Maria Silva")
              .adicionar_produto(Product("Teclado", 100.0))
              .com_endereco("Rua Central 456")
              .build())
    
    assert pedido.cliente == "Maria Silva", "Error cliente"
    assert pedido.endereco == "Rua Central 456", "Error endereco"