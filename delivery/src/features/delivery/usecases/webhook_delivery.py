import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, update

from src.features.delivery.delivery_model import DeliveryModel
from src.features.outbox.outbox_model import OutboxModel


class WebhookDeliveryUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, order_id, result) -> None:
        if result == "process":
            outbox_data = {
                "event_type": "order.complete",
                "payload": {
                    "order_id": order_id,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }
            delivery_status = "COMPLETED"
        elif result == "rollback":
            outbox_data = {
                "event_type": "payment.rollback",
                "payload": {
                    "order_id": order_id,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }
            delivery_status = "CANCELED"

        await self.session.execute(
            update(DeliveryModel)
            .where(DeliveryModel.order_id == order_id)
            .values(status=delivery_status)
        )

        await self.session.execute(insert(OutboxModel).values(**outbox_data))
