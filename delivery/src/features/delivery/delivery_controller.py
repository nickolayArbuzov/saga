from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
from src.features.delivery.async_use_cases.webhook_delivery import (
    WebhookDeliveryUseCase,
)
from src.dependencies import get_db


router = APIRouter()


def get_webhook_delivery_usecase(db: AsyncSession = Depends(get_db)):
    return WebhookDeliveryUseCase(db)


@router.post("/webhook-delivery")
async def create_order(
    amount: float,
    usecase: WebhookDeliveryUseCase = Depends(get_webhook_delivery_usecase),
):
    order_id = str(uuid.uuid4())
    await usecase.execute(order_id, amount, "payment.process")
    return {"order_id": order_id, "status": "processing"}
