import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.features.outbox.outbox_model import OutboxModel
from src.features.order.order_model import OrderModel


class OrderService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_order_and_outbox(
        self, order_id: str, amount: float, event_type: str
    ) -> None:

        order_data = {
            "id": order_id,
            "amount": amount,
            "status": "CREATED",
        }

        await self.session.execute(insert(OrderModel).values(**order_data))

        outbox_data = {
            "id": str(uuid.uuid4()),
            "event_type": event_type,
            "payload": {"order_id": order_id, "amount": amount},
            "sent": False,
        }
        await self.session.execute(insert(OutboxModel).values(**outbox_data))

        await self.session.commit()
