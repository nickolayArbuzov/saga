import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, update

from src.features.outbox.outbox_model import OutboxModel
from src.features.payment.payment_model import PaymentModel


class WebhookPaymentUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, order_id, result) -> None:
        if result == "process":
            outbox_data = {
                "event_type": "delivery.process",
                "routing_key": "delivery.events",
                "payload": {
                    "order_id": order_id,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }
            payment_status = "COMPLETED"
        elif result == "rollback":
            outbox_data = {
                "event_type": "order.rollback",
                "routing_key": "order.events",
                "payload": {
                    "order_id": order_id,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }
            payment_status = "CANCELED"

        await self.session.execute(
            update(PaymentModel)
            .where(PaymentModel.order_id == order_id)
            .values(status=payment_status)
        )

        await self.session.execute(insert(OutboxModel).values(**outbox_data))
