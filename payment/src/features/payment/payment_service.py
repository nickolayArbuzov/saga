def process_payment(payload):
    order_id = payload["order_id"]
    amount = payload["amount"]
    # Обрабатываем оплату
    # Если успех, пишем в outbox "delivery.schedule"
    # Если ошибка, пишем в outbox "order.cancel"
