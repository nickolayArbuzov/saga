from datetime import datetime
from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession

from order.src.tasks.producers import publish_order_created


router = APIRouter()


@router.post("/create-order")
async def create_order(amount: float):
    order_id = await publish_order_created(amount)
    return {"order_id": order_id, "status": "processing"}
