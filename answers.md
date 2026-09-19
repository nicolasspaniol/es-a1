# Respostas escritas

## 1. Configuração da aplicação

**1. Explique por que utilizar __new__ não impede, por si só, novas execuções de __init__.**
Porque a `__init__` é chamado toda vez que a classe é chamada (`AppConfig()`), independente do comportamento da `__new__`. Chamar a classe novamente, mesmo quando já há uma instância criada, vai executar novamente `__init__` naquela instância.

**2. Explique como um módulo Python poderia ser utilizado para compartilhar uma configuração sem implementar uma segunda versão do Singleton.**
As variáveis agora contidas no _singleton_ poderiam ser movidas para um módulo próprio, como:

```py
# app_config.py
environment = 'production'
currency = 'BRL'
debug = False
```

E usadas como:

```py
import app_config as AppConfig

assert not AppConfig.debug
AppConfig.debug = True

import app_config as AppConfig2
assert AppConfig2.debug
```

Como cada módulo só é importado uma vez, o objeto do módulo se comporta como um _singleton_.

**3. Identifique uma possível consequência de possuir um objeto de configuração global compartilhado.**
Se, em algum momento, for identificada a necessidade de se ter mais arquivos de configuração (por exemplo, para usuários diferentes), haverá o trabalho de adaptar o código pra essa possibilidade.

## 3. Pagamento e Factory Method

**1. Identifique os papéis de: Creator, Concrete Creator, Product, Concrete Product.**
- Creator: `PaymentProcessor`
- Concrete Creator: `PixProcessor`, `CreditCardProcessor`, `BoletoProcessor`
- Product: `Payment`
- Concrete Product: `PixPayment`, `CreditCardPayment`, `BoletoPayment`

**2. Explique por que uma função contendo simplesmente uma sequência de if/elif
escolhendo classes concretas não é, por si só, suficiente para caracterizar o padrão
Factory Method.**
O _Factory Method_ permite que novos "produtos" sejam adicionados no sistema sem que o código já existente precise ser alterado, o que não seria o caso com os `if`s/`elif`s.

**3. Considere que uma nova forma de pagamento seja adicionada posteriormente.
Explique quais partes da sua implementação precisariam ser alteradas.**
Só precisariam ser adicionadas as classes relacionadas a essa nova forma de pagamento, ex: `GooglePayPayment`, `GooglePayProcessor`.
