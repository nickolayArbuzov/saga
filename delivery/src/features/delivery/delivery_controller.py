from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.delivery.usecases.webhook_delivery import WebhookDeliveryUseCase
from src.features.delivery.delivery_schema import WebhookDeliveryPayload
from src.dependencies import get_db


router = APIRouter()


def get_webhook_delivery_usecase(db: AsyncSession = Depends(get_db)):
    return WebhookDeliveryUseCase(db)


@router.post("/webhook-delivery")
async def webhook_delivery(
    payload: WebhookDeliveryPayload,
    usecase: WebhookDeliveryUseCase = Depends(get_webhook_delivery_usecase),
):
    await usecase.execute(payload)
    return {"status": "ok"}
