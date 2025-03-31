import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.features.outbox.outbox_model import OutboxModel
from src.features.payment.payment_model import PaymentModel


class WebhookPaymentUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, order_id, result) -> None:
        if result == "process":
            outbox_data = {
                "event_type": "delivery.process",
                "payload": {
                    "order_id": order_id,
                    "event_id": str(uuid.uuid4()),
                },
                "sent": False,
            }
        elif result == "rollback":
            outbox_data = {
                "event_type": "order.rollback",
                "payload": {
                    "order_id": order_id,
                    "event_id": str(uuid.uuid4()),
                },
                "sent": False,
            }

        await self.session.execute(insert(OutboxModel).values(**outbox_data))
