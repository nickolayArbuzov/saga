from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.features.outbox.outbox_model import OutboxModel
from src.features.delivery.delivery_model import DeliveryModel


class WebhookDeliveryUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, payload) -> None:
        print("payload", payload)
