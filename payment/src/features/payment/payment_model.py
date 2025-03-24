from sqlalchemy import Column, String, Float, Enum
from ...database import Base


class PaymentModel(Base):
    __tablename__ = "payment"
    id = Column(String, primary_key=True)
    order_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(
        Enum("PENDING", "COMPLETED", "FAILED", "REFUNDED", name="payment_status_enum"),
        default="PENDING",
    )
