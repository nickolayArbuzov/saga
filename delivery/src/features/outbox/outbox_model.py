from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from ...database import Base


class OutboxModel(Base):
    __tablename__ = "outbox"
    id = Column(String, primary_key=True)
    event_type = Column(String, nullable=False)
    payload = Column(JSONB, nullable=False)
    sent = Column(Boolean, default=False)
