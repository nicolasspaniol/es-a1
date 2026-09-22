import pytest
from es_a1.app_config import AppConfig
from es_a1.order import Order, Product, OrderBuilder
from es_a1.channel import Checkout, Notification, WebFactory, MobileFactory


def test_singleton():
    '''
    Verifica se a classe AppConfig é um tipo normal ('type') e se sua instância tem o seu
    tipo.

    ESPERADO: que AppConfig seja instância de 'type' e 'AppConfig()' seja instância de
    AppConfig.

    RELEVÂNCIA: a implementação do singleton por decorador substitui a classe que o leva
    por uma função, o que não é desejado. Aqui verificamos que isso não é o caso na nossa
    implementação.
    '''

    assert isinstance(AppConfig, type)
    assert isinstance(AppConfig(), AppConfig)


def test_builder():
    '''
    Verifica se a construção de um pedido por meio do builder tem o mesmo resultado
    da construção direta do objeto, passando as informações como argumentos do __init__.

    ESPERADO: que as variáveis `a` e `b` representem objetos idênticos.

    RELEVÂNCIA: a classe do builder deve consistir apenas em uma forma mais ergonômica
    de se construir um objeto da classe original, sem modificar inesperadamente nenhum
    dos campos a ela passados.
    '''

    melancia = Product('melancia', 10.0)
    banana = Product('banana', 20.0)
    a = OrderBuilder() \
        .with_client('Cliente') \
        .add_product(melancia) \
        .add_product(banana) \
        .with_address('Rua A') \
        .with_coupon('DESC100') \
        .build()

    b = Order('Cliente', [melancia, banana], 'Rua A', 'DESC100', None, None)

    assert a.client == b.client
    assert a.products == b.products
    assert a.address == b.address
    assert a.coupon == b.coupon
    assert a.payment_type == b.payment_type
    assert a.observation == b.observation


@pytest.mark.parametrize("factory_cls", [MobileFactory, WebFactory])
def test_factory(factory_cls):
    '''
    Verifica se os objetos criados por cada uma das fábricas herdam, de fato,
    da classe abstrata daquele tipo de objeto.

    ESPERADO: que `create_notification()` e `create_checkout()` retornem objetos
    que herdam `Notification` e `Checkout`, respectivamente, para todas as
    fábricas implementadas.

    RELEVÂNCIA: a propriedade testada é necessária para que o padrão caracterizado
    pelas classes seja realmente uma Abstract Factory. Em Python, que não é uma
    linguagem com tipagem estática, as classes podem descumprir tal propriedade
    sem levantar nenhum erro.
    '''
    ...

    factory = factory_cls()
    assert isinstance(factory.create_notification(), Notification)
    assert isinstance(factory.create_checkout(), Checkout)
