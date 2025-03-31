from sqlalchemy.orm import Session
from sqlalchemy import insert, select

from src.features.payment.payment_model import PaymentModel
from src.features.outbox.outbox_model import OutboxModel
from src.features.inbox.inbox_model import InboxModel


class RollbackPaymentUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, payload) -> None:
        existing = (
            self.session.query(InboxModel)
            .filter_by(event_id=payload["event_id"])
            .one_or_none()
        )
        if existing is not None:
            return

        inbox_event = InboxModel(
            event_id=payload["event_id"],
            payload=payload,
            processed=False,
        )
        self.session.add(inbox_event)
        self.session.commit()
