from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from src.features.payment.payment_model import PaymentModel


class CreatePaymentUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, payload: dict) -> None:
        payment_data = {
            "order_id": payload["order_id"],
            "amount": payload["amount"],
            "status": "PROCESSED",
        }
        await self.session.execute(insert(PaymentModel).values(**payment_data))

        # integrate with external payment-service and wait for webhook trigger

