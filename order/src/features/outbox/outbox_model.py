from sqlalchemy import Column, String, Float, Enum
from database import Base


class Outbox(Base):
    __tablename__ = "outbox"
    id = Column(String, primary_key=True)
    event_type = Column(String, nullable=False)
    payload = Column(String, nullable=False)
    sent = Column(Enum("true", "false"), default="false")
