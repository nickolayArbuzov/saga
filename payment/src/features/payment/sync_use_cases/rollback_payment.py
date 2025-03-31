from sqlalchemy.orm import Session
from sqlalchemy import insert, select

from src.features.outbox.outbox_model import OutboxModel
from src.features.payment.payment_model import PaymentModel


class RollbackPaymentUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, payload) -> None:
        # send req to payment-system
        pass
