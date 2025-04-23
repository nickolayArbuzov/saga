from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from src.broker.subscriber import start_consumer
from src.database import Base, async_engine

from src.features.payment import payment_controller
from src.features.payment import payment_model
from src.features.outbox import outbox_model
from src.features.outbox.cron import run_outbox_publisher
from src.features.inbox import inbox_model


async def lifespan(app):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    asyncio.create_task(run_outbox_publisher())
    asyncio.create_task(start_consumer())
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(payment_controller.router, prefix="/api", tags=["payment"])
