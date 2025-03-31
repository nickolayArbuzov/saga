from sqlalchemy.orm import Session
from sqlalchemy import insert, select

from src.features.outbox.outbox_model import OutboxModel
from src.features.payment.payment_model import PaymentModel


class WebhookPaymentUseCase:
    def __init__(self, session: Session):
        self.session = session

    async def execute(self, payload) -> None:
        print("payload", payload)
