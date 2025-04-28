from sqlalchemy import Column, Float, Enum, Integer
from src.database import Base


class PaymentModel(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    amount = Column(Float, nullable=False)
    status = Column(
        Enum(
            "PROCESSED",
            "COMPLETED",
            "CANCELING",
            "CANCELED",
            name="payment_status_enum",
        ),
        default="PROCESSED",
    )
