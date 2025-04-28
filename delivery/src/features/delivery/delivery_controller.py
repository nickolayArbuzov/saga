from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.features.delivery.usecases.webhook_delivery import (
    WebhookDeliveryUseCase,
)
from src.dependencies import get_db


router = APIRouter()


def get_webhook_delivery_usecase(db: AsyncSession = Depends(get_db)):
    return WebhookDeliveryUseCase(db)


@router.post("/webhook-delivery")
async def create_order(
    order_id: str,
    result: str,
    usecase: WebhookDeliveryUseCase = Depends(get_webhook_delivery_usecase),
):
    await usecase.execute(order_id, result)
    return {"status": "ok"}
