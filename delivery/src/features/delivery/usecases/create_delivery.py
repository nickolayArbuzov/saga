from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from src.features.delivery.delivery_model import DeliveryModel


class CreateDeliveryUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, payload: dict) -> None:
        delivery_data = {
            "order_id": payload["order_id"],
            "amount": payload["amount"],
            "status": "PROCESSED",
        }

        await self.session.execute(insert(DeliveryModel).values(**delivery_data))

        # integrate with delivery-service
