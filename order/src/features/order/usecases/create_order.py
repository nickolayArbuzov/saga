import uuid

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from src.features.order.order_model import OrderModel
from src.features.outbox.outbox_model import OutboxModel


class CreateOrderUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, amount: float) -> None:
        order_data = {
            "amount": amount,
            "status": "PROCESSED",
        }

        order_id = (
            await self.session.execute(
                insert(OrderModel).values(**order_data).returning(OrderModel.id)
            )
        ).scalar_one()

        outbox_data = {
            "event_type": "payment.process",
            "routing_key": "payment.events",
            "payload": {
                "order_id": order_id,
                "amount": amount,
                "event_id": str(uuid.uuid4()),
            },
            "processed": False,
        }
        await self.session.execute(insert(OutboxModel).values(**outbox_data))

        return order_id
