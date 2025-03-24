from sqlalchemy import Column, String, Float, Enum
from ...database import Base


class OutboxModel(Base):
    __tablename__ = "outbox"
    id = Column(String, primary_key=True)
    event_type = Column(String, nullable=False)
    payload = Column(String, nullable=False)
    sent = Column(
        Enum("true", "false", name="payment_outbox_status_enum"), default="false"
    )
