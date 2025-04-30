from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update

from src.features.payment.payment_model import PaymentModel


class CancelPaymentUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def execute(self, payload: dict) -> None:
        await self.session.execute(
            update(PaymentModel)
            .where(PaymentModel.order_id == payload["order_id"])
            .values(status="CANCELING")
        )

    # integrate with external payment-service and wait for webhook trigger
