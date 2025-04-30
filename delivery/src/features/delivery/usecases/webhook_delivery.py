import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, update

from src.features.outbox.outbox_model import OutboxModel
from src.features.delivery.delivery_model import DeliveryModel
from src.features.delivery.delivery_schema import WebhookDeliveryPayload

class WebhookDeliveryUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, payload: WebhookDeliveryPayload) -> None:
        if payload.result == "process":
            outbox_data = {
                "event_type": "order.process",
                "routing_key": "order.events",
                "payload": {
                    "order_id": payload.order_id,
                    "amount": payload.amount,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }
            delivery_status = "COMPLETED"
        elif payload.result == "rollback":
            outbox_data = {
                "event_type": "payment.rollback",
                "routing_key": "payment.events",
                "payload": {
                    "order_id": payload.order_id,
                    "amount": payload.amount,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }
            delivery_status = "CANCELED"

        await self.session.execute(
            update(DeliveryModel)
            .where(DeliveryModel.order_id == payload.order_id)
            .values(status=delivery_status)
        )

        await self.session.execute(insert(OutboxModel).values(**outbox_data))

