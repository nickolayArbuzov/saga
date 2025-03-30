from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
from src.dependencies import get_db
from src.features.order.order_service import OrderService


router = APIRouter()


def get_order_service(db: AsyncSession = Depends(get_db)):
    return OrderService(db)


@router.post("/create-order")
async def create_order(
    amount: float, service: OrderService = Depends(get_order_service)
):
    order_id = str(uuid.uuid4())
    await service.create_order_and_outbox(order_id, amount, "payment.process")
    return {"order_id": order_id, "status": "processing"}
