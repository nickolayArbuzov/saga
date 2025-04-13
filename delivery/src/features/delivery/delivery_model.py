from sqlalchemy import Column, String, Enum, Integer
from src.database import Base


class DeliveryModel(Base):
    __tablename__ = "delivery"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, nullable=False)
    status = Column(
        Enum("SCHEDULED", "DELIVERED", "FAILED", name="delivery_status_enum"),
        default="SCHEDULED",
    )
