from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.payment.usecases.webhook_payment import WebhookPaymentUseCase
from src.dependencies import get_db


router = APIRouter()


def get_webhook_payment_usecase(db: AsyncSession = Depends(get_db)):
    return WebhookPaymentUseCase(db)


@router.post("/webhook-payment")
async def webhook_payment(
    order_id: str,
    result: str,
    usecase: WebhookPaymentUseCase = Depends(get_webhook_payment_usecase),
):
    await usecase.execute(order_id, result)
    return {"order_id": order_id, "status": "processing"}
