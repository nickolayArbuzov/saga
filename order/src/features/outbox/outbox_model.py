from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.dialects.postgresql import JSONB
from src.database import Base


class OutboxModel(Base):
    __tablename__ = "outbox"
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, nullable=False)
    payload = Column(JSONB, nullable=False)
    sent = Column(Boolean, default=False)
