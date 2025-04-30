import uuid
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, update

from src.features.outbox.outbox_model import OutboxModel
from src.features.payment.payment_model import PaymentModel
from src.features.payment.payment_schema import WebhookPaymentPayload

class WebhookPaymentUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, payload: WebhookPaymentPayload) -> None:
        if payload.result == "process":
            outbox_data = {
                "event_type": "delivery.process",
                "routing_key": "delivery.events",
                "payload": {
                    "order_id": payload.order_id,
                    "amount": payload.amount,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }
            payment_status = "COMPLETED"
        elif payload.result == "rollback":
            outbox_data = {
                "event_type": "order.rollback",
                "routing_key": "order.events",
                "payload": {
                    "order_id": payload.order_id,
                    "amount": payload.amount,
                    "event_id": str(uuid.uuid4()),
                },
                "processed": False,
            }
            payment_status = "CANCELED"

        await self.session.execute(
            update(PaymentModel)
            .where(PaymentModel.order_id == payload.order_id)
            .values(status=payment_status)
        )

        await self.session.execute(insert(OutboxModel).values(**outbox_data))

