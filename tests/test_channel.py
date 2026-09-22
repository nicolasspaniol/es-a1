from es_a1.order import Product, OrderBuilder
from es_a1.channel import WebFactory, MobileFactory


produto1 = Product("Mouse", 100.00)
produto2 = Product("Teclado", 250.00)

order = (
    OrderBuilder()
    .with_client("Ximena")
    .add_product(produto1)
    .add_product(produto2)
    .with_address("Rio de Janeiro")
    .with_payment_type("PIX")
    .build()
)


def process_channel(factory, order):
    checkout = factory.create_checkout()
    notification = factory.create_notification()

    checkout.show(order)
    notification.send(order)


print("WEB")
process_channel(WebFactory(), order)

print()

print("MOBILE")
process_channel(MobileFactory(), order)