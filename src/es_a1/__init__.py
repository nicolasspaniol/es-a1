from es_a1.app_config import AppConfig
from es_a1.channel import get_channel_factory
from es_a1.order import OrderBuilder, Product
from es_a1.order_service import OrderService
from es_a1.payment import  PixProcessor, CreditCardProcessor, BankTransferProcessor                                

def main() -> None:
    config = AppConfig()

    print(f"Ambiente: {config.environment}")
    print(f"Moeda: {config.currency}")
    print(f"Debug: {config.debug}")

    scenarios = [
        ("WEB", PixProcessor()),
        ("KIOSK", CreditCardProcessor()),
        ("MOBILE", BankTransferProcessor()),
    ]

    for channel, processor in scenarios:
        print(f"\n=== PEDIDO NO CANAL {channel} ===")

        order = (
            OrderBuilder()
            .with_client("Ximena")
            .add_product(Product("Mouse", 100.00))
            .add_product(Product("Teclado", 250.00))
            .with_address("Rio de Janeiro")
            .with_observation("Pedido de demonstração")
            .with_payment_type(processor)
            .build()
        )

        factory = get_channel_factory(channel)
        service = OrderService(factory)
        service.process_order(order)