from src.es_a1.order import OrderBuilder, Product


def TestOrder():

    pedido = (OrderBuilder()
              .com_cliente("Maria Silva")
              .adicionar_produto(Product("Teclado", 100.0))
              .com_endereco("Rua Central 456")
              .build())
    
    assert pedido.cliente == "Maria Silva", "Error cliente"
    assert pedido.endereco == "Rua Central 456", "Error endereco"


# Ejecutamos la función de pruebas
TestOrder()