from sqlalchemy import Column, String, Float, Enum
from src.database import Base


class OrderModel(Base):
    __tablename__ = "order"
    id = Column(String, primary_key=True)
    amount = Column(Float, nullable=False)
    status = Column(
        Enum("CREATED", "PAID", "DELIVERED", "CANCELLED", name="order_status_enum"),
        default="CREATED",
    )
