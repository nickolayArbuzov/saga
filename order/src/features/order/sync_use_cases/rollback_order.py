from sqlalchemy.orm import Session
from sqlalchemy import insert, select

from src.features.order.order_model import OrderModel
from src.features.outbox.outbox_model import OutboxModel
from src.features.inbox.inbox_model import InboxModel


class RollbackOrderUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, payload) -> None:
        existing = (
            self.session.execute(
                select(InboxModel).where(InboxModel.event_id == payload["event_id"])
            )
        ).one_or_none()
        if existing is not None:
            return

        inbox_event = InboxModel(
            event_id=payload["event_id"],
            payload=payload,
            processed=False,
        )
        self.session.execute(insert(InboxModel).values(**inbox_event))
        self.session.commit()
