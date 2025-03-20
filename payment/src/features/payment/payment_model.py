from sqlalchemy import Column, String, Float, Enum
from database import Base


class Payment(Base):
    __tablename__ = "payments"
    id = Column(String, primary_key=True)
    order_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(
        Enum("PENDING", "COMPLETED", "FAILED", "REFUNDED"), default="PENDING"
    )
