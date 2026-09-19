from __future__ import annotations
from typing import ClassVar


class Product:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Order:

    def __init__(self, cliente, produtos, endereco, cupom, tipo_pagamento, observacao):
        self.cliente = cliente
        self.produtos = produtos
        self.endereco = endereco
        self.cupom = cupom
        self.tipo_pagamento = tipo_pagamento
        self.observacao = observacao

    def total(self):
        return sum(produto.preco for produto in self.produtos)


class OrderBuilder:
    def __init__(self):
        self._cliente = None
        self._produtos = []
        self._endereco = None
        self._cupom = None
        self._forma_pagamento = None
        self._observacao = None

    def com_cliente(self, cliente):
        self._cliente = cliente
        return self

    def adicionar_produto(self, produto):
        self._produtos.append(produto)
        return self

    def com_endereco(self, endereco):
        self._endereco = endereco
        return self

    def com_cupom(self, cupom):
        self._cupom = cupom
        return self

    def com_forma_pagamento(self, forma):
        self._forma_pagamento = forma
        return self

    def com_observacao(self, obs):
        self._observacao = obs
        return self

    def build(self):
        
        if not self._cliente:
            raise ValueError("O pedido precisa ter um cliente.")
        
        return Order(
            self._cliente, 
            self._produtos, 
            self._endereco, 
            self._cupom, 
            self._forma_pagamento, 
            self._observacao
        )




