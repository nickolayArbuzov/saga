from sqlalchemy import Column, String, Enum
from ...database import Base


class DeliveryModel(Base):
    __tablename__ = "delivery"
    id = Column(String, primary_key=True)
    order_id = Column(String, nullable=False)
    status = Column(Enum("SCHEDULED", "DELIVERED", "FAILED"), default="SCHEDULED")
