from sqlalchemy import Column, Integer, Float, Enum
from src.database import Base


class DeliveryModel(Base):
    __tablename__ = "delivery"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(
        Enum("PROCESSED", "COMPLETED",  "CANCELED", name="delivery_status_enum"),
        default="PROCESSED",
    )

