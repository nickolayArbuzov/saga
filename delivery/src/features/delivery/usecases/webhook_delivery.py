import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.features.delivery.delivery_model import DeliveryModel
from src.features.outbox.outbox_model import OutboxModel


class WebhookDeliveryUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, order_id, result) -> None:
        if result == "process":
            outbox_data = {
                "event_type": "order.process",
                "payload": {
                    "order_id": order_id,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }
        elif result == "rollback":
            outbox_data = {
                "event_type": "payment.rollback",
                "payload": {
                    "order_id": order_id,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }

        await self.session.execute(insert(OutboxModel).values(**outbox_data))
