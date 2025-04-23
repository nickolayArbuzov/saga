import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.features.order.order_model import OrderModel
from src.features.outbox.outbox_model import OutboxModel


class CancelOrderUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, amount: float) -> None:
        order_id = str(uuid.uuid4())
        order_data = {
            "id": order_id,
            "amount": amount,
            "status": "CREATED",
        }

        await self.session.execute(insert(OrderModel).values(**order_data))

        outbox_data = {
            "event_type": "payment.process",
            "payload": {
                "order_id": order_id,
                "amount": amount,
                "event_id": str(uuid.uuid4()),
            },
            "sent": False,
        }
        await self.session.execute(insert(OutboxModel).values(**outbox_data))

        return order_id
