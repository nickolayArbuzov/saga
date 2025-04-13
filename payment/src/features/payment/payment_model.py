from sqlalchemy import Column, String, Float, Enum, Integer
from src.database import Base


class PaymentModel(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(
        Enum("PENDING", "COMPLETED", "FAILED", "REFUNDED", name="payment_status_enum"),
        default="PENDING",
    )
