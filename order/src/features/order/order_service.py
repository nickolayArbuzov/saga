import uuid
from datetime import datetime
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from ..outbox.outbox_model import OutboxModel
from .order_model import OrderModel


class OrderService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_order_and_outbox(
        order_id: str, amount: float, event_type: str, db: AsyncSession
    ) -> None:

        order_data = {
            "id": order_id,
            "amount": amount,
            "status": "pending",
            "created_at": datetime.utcnow(),
        }

        await db.execute(insert(OrderModel).values(**order_data))

        outbox_event_data = {
            "id": str(uuid.uuid4()),
            "event_type": event_type,
            "payload": {"order_id": order_id, "amount": amount},
            "created_at": datetime.utcnow(),
            "processed": False,
        }
        await db.execute(insert(OutboxModel).values(**outbox_event_data))

        await db.commit()
