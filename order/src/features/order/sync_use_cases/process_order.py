from sqlalchemy.orm import Session
from sqlalchemy import insert, select

from src.features.outbox.outbox_model import OutboxModel
from src.features.order.order_model import OrderModel


class ProcessOrderUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, payload) -> None:
        print("payload", payload)
