from pydantic import BaseModel
from enum import Enum


class ResultEnum(str, Enum):
    process = "process"
    rollback = "rollback"


class WebhookPaymentPayload(BaseModel):
    order_id: int
    amount: float
    result: ResultEnum

