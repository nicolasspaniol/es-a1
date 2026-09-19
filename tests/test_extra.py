import pytest
from es_a1.app_config import AppConfig
from es_a1.order import OrderBuilder, Order


def test_singleton():
    '''
    Verifica se a classe AppConfig é um tipo normal ('type') e se sua instância tem o seu
    tipo.

    ESPERADO: que AppConfig seja instância de 'type' e 'AppConfig()' seja instância de
    AppConfig.

    RELEVÂNCIA: a implementação do singleton por decorador substitui a classe que o leva
    por uma função, o que não é desejado. Aqui verificamos que isso não é o caso na nossa
    impolementação.
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

    a = OrderBuilder() \
        .com_cliente('Cliente') \
        .adicionar_produto('melancia') \
        .adicionar_produto('banana') \
        .com_endereco('Rua A') \
        .com_cupom('DESC100') \
        .build()

    b = Order('Cliente', ['melancia', 'banana'], 'Rua A', 'DESC100', None, None)

    assert a.cliente == b.cliente
    assert a.produtos == b.produtos
    assert a.endereco == b.endereco
    assert a.cupom == b.cupom
    assert a.tipo_pagamento == b.tipo_pagamento
    assert a.observacao == b.observacao


def test_factory():
    ...
