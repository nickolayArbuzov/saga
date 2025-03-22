from sqlalchemy import Column, String, Float, Enum
from database import Base


class OrderModel(Base):
    __tablename__ = "orders"
    id = Column(String, primary_key=True)
    amount = Column(Float, nullable=False)
    status = Column(
        Enum("CREATED", "PAID", "DELIVERED", "CANCELLED"), default="CREATED"
    )
