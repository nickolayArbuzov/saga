from sqlalchemy import Column, Integer, Float, Enum
from src.database import Base


class OrderModel(Base):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    status = Column(
        Enum("PROCESSED", "COMPLETED", "CANCELED", name="order_status_enum"),
        default="PROCESSED",
    )
