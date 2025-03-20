import uuid
from core.services import create_order_and_outbox
from tasks.celery_app import celery_app


async def publish_order_created(amount):
    order_id = str(uuid.uuid4())
    await create_order_and_outbox(order_id, amount, "payment.process")
    celery_app.send_task(
        "payment.process", args=[{"order_id": order_id, "amount": amount}]
    )
    return order_id
