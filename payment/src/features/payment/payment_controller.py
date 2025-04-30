from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.payment.usecases.webhook_payment import WebhookPaymentUseCase
from src.features.payment.payment_schema import WebhookPaymentPayload
from src.dependencies import get_db


router = APIRouter()


def get_webhook_payment_usecase(db: AsyncSession = Depends(get_db)):
    return WebhookPaymentUseCase(db)


@router.post("/webhook-payment")
async def webhook_payment(
    payload: WebhookPaymentPayload,
    usecase: WebhookPaymentUseCase = Depends(get_webhook_payment_usecase),
):
    await usecase.execute(payload)
    return {"status": "ok"}
