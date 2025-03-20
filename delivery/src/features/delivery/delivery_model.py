from sqlalchemy import Column, String, Enum
from database import Base


class Delivery(Base):
    __tablename__ = "deliveries"
    id = Column(String, primary_key=True)
    order_id = Column(String, nullable=False)
    status = Column(Enum("SCHEDULED", "DELIVERED", "FAILED"), default="SCHEDULED")
