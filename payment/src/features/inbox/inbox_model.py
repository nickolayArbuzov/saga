from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from src.database import Base


class InboxModel(Base):
    __tablename__ = "inbox"
    id = Column(String, primary_key=True)
    event_id = Column(String, nullable=False)
    payload = Column(JSONB, nullable=False)
    processed = Column(Boolean, default=False)
