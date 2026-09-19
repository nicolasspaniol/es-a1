from typing import Optional, TYPE_CHECKING

# this avoids circular imports while preserving typing; payment.py already imports order.py
if TYPE_CHECKING:
    from es_a1.payment import PaymentProcessor


class Product:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco


class Order:
    def __init__(
        self,
            cliente: str,
            produtos: list[Product],
            endereco: Optional[str],
            cupom: Optional[str],
            tipo_pagamento: Optional[PaymentProcessor],
            observacao: Optional[str]
        ):
        self.cliente = cliente
        self.produtos = produtos
        self.endereco = endereco
        self.cupom = cupom
        self.tipo_pagamento = tipo_pagamento
        self.observacao = observacao

    def total(self) -> float:
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




