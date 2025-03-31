from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
from src.features.payment.async_use_cases.webhook_payment import WebhookPaymentUseCase
from src.dependencies import get_db


router = APIRouter()


def get_webhook_payment_usecase(db: AsyncSession = Depends(get_db)):
    return WebhookPaymentUseCase(db)


@router.post("/webhook-payment")
async def webhook_payment(
    amount: float, usecase: WebhookPaymentUseCase = Depends(get_webhook_payment_usecase)
):
    order_id = str(uuid.uuid4())
    await usecase.execute(order_id, amount, "payment.process")
    return {"order_id": order_id, "status": "processing"}
