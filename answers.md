# Respostas escritas

## 1. Configuração da aplicação

**1. Explique por que utilizar __new__ não impede, por si só, novas execuções de __init__.**
Porque a `__init__` é chamado toda vez que a classe é chamada (`AppConfig()`), independente do
comportamento da `__new__`. Chamar a classe novamente, mesmo quando já há uma instância criada,
vai executar novamente `__init__` naquela instância.

**2. Explique como um módulo Python poderia ser utilizado para compartilhar uma configuração
sem implementar uma segunda versão do Singleton.**
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
Outra opção equivalente seria colocar a classe do _singleton_, privada, no módulo e expor apenas
uma instância dela.

**3. Identifique uma possível consequência de possuir um objeto de configuração global
compartilhado.**
Se, em algum momento, for identificada a necessidade de se ter mais arquivos de configuração
(por exemplo, para usuários diferentes), haverá o trabalho de adaptar o código pra essa
possibilidade.

## 2. Pedido e Builder

**1. Identifique quais componentes da sua implementação correspondem ao Builder e ao
objeto construído.**
A classe OrderBuilder corresponde ao Builder, enquanto Order representa o objeto construído. 

**2. Explique por que seria possível construir o pedido diretamente pelo construtor de Order
e qual seria a diferença em relação à solução adotada.**

Como Order é uma dataclass, seu construtor permite receber diretamente os atributos do pedido. Portanto, seria possível criar um pedido sem utilizar o builder.

O OrderBuilder permite informar esses dados gradualmente, com métodos que tornam explícita a finalidade de cada valor. Na implementação atual, a construção direta exige informar todos os argumentos, mesmo que alguns recebam None, e não executa a validação definida no builder.

## 3. Pagamento e Factory Method

**1. Identifique os papéis de: Creator, Concrete Creator, Product, Concrete Product.**
- Creator: `PaymentProcessor`
- Concrete Creator: `PixProcessor`, `CreditCardProcessor`, `BoletoProcessor`
- Product: `Payment`
- Concrete Product: `PixPayment`, `CreditCardPayment`, `BoletoPayment`

**2. Explique por que uma função contendo simplesmente uma sequência de if/elif
escolhendo classes concretas não é, por si só, suficiente para caracterizar o padrão
Factory Method.**
O _Factory Method_ permite que novos "produtos" sejam adicionados no sistema sem que o
código já existente precise ser alterado, o que não seria o caso com os `if`s/`elif`s.

**3. Considere que uma nova forma de pagamento seja adicionada posteriormente.
Explique quais partes da sua implementação precisariam ser alteradas.**
Só precisariam ser adicionadas as classes relacionadas a essa nova forma de pagamento,
ex: `GooglePayPayment`, `GooglePayProcessor`.

## 4. Famílias por canal

**1. Explique por que checkout e notificação podem ser considerados uma família de produtos.**
TODO

**2. Explique qual problema a Abstract Factory resolve nessa situação.**
TODO

**3. Explique por que o pagamento não deve fazer parte da fábrica responsável pelo canal.**
TODO

## 5. Seleção de fábrica e alteração do sistema

**1. Liste os arquivos criados ou alterados para adicionar KIOSK.**
Escolhemos adicionar o kiosk no próprio arquivo `channel.py`, onde ficam os outros canais.
Só precisamos alterar este arquivo e as alterações foram apenas adições, sem ser necessário
alterar o corpo de nenhuma função:
- adicionamos `KioskCheckout`
- adicionamos `KioskNotification`
- adicionamos `KioskFactory`
- adicionamos ao `dict` com os tipos de pagamento a entrada `'KIOSK'`

**2. Explique por que as alterações realizadas são ou não compatíveis com o princípio OCP.**
São compatíveis, pois pudemos adicionar um novo tipo de pagamento, interoperável com os
anteriores, sem alterar nada do código já implementado.

## 6. Responsabilidades e integração

**1. Qual é a responsabilidade principal de cada componente criado?**
TODO

**2. Escolha três componentes diferentes e indique uma mudança que deveria ficar
restrita a cada um deles.**
TODO

**3. Identifique uma decisão de projeto da sua solução que poderia ser diferente.
Explique qual seria a alternativa e qual seria a consequência dessa mudança.**
TODO

## 7. Testes e alterações

Ver [test_extra.py](tests/test_extra.py)

## 8. Situação de mudança

**1. Quais arquivos foram criados ou modificados?**
TODO

**2. O fluxo principal de processamento precisou ser alterado?**
TODO

**3. Quais classes existentes precisaram ser modificadas?**
TODO

**4. Explique como o Factory Method contribuiu para essa extensão.**
TODO

**5. Compare essa alteração com a inclusão do canal KIOSK.
Quais são as semelhanças e diferenças arquiteturais entre as duas extensões?**
TODO
