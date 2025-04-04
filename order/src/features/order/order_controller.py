from fastapi import APIRouter, Depends, Body, Path
from sqlalchemy.ext.asyncio import AsyncSession
import uuid
from src.features.order.async_use_cases.create_order import CreateOrderUseCase
from src.dependencies import get_db


router = APIRouter()


def get_create_order_usecase(db: AsyncSession = Depends(get_db)):
    return CreateOrderUseCase(db)


@router.post("/create-order")
async def create_order(
    amount: float, usecase: CreateOrderUseCase = Depends(get_create_order_usecase)
):
    order_id = await usecase.execute(amount)
    return {"order_id": order_id, "status": "processing"}
