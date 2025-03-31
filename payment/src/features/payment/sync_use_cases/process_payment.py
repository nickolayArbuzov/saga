from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, select

from src.features.outbox.outbox_model import OutboxModel
from src.features.payment.payment_model import PaymentModel


class ProcessPaymentUseCase:
    def __init__(self, session: AsyncSession):
        self.session = session

    def execute(self, payload) -> None:
        print("payload", payload)
