from typing import Optional, TYPE_CHECKING
from dataclasses import dataclass

# this avoids circular imports while preserving typing; payment.py already imports order.py
if TYPE_CHECKING:
    from es_a1.payment import PaymentProcessor


@dataclass(eq=False)
class Product:
    nome: str
    preco: float


@dataclass(eq=False)
class Order:
    cliente: str
    produtos: list[Product]
    endereco: Optional[str]
    cupom: Optional[str]
    tipo_pagamento: Optional[PaymentProcessor]
    observacao: Optional[str]

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

    def com_cliente(self, cliente: str):
        self._cliente = cliente
        return self

    def adicionar_produto(self, produto: Product):
        self._produtos.append(produto)
        return self

    def com_endereco(self, endereco: str):
        self._endereco = endereco
        return self

    def com_cupom(self, cupom: str):
        self._cupom = cupom
        return self

    def com_forma_pagamento(self, forma: PaymentProcessor):
        self._forma_pagamento = forma
        return self

    def com_observacao(self, obs: str):
        self._observacao = obs
        return self

    def build(self) -> Order:
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
