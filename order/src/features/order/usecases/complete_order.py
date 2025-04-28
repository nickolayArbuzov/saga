from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update

from src.features.order.order_model import OrderModel


class CompleteOrderUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, payload: dict) -> None:
        await self.session.execute(
            update(OrderModel)
            .where(OrderModel.id == payload["order_id"])
            .values(status="COMPLETED")
        )
