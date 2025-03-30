from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.database import Base, async_engine

from src.features.order import order_controller
from src.features.order import order_model
from src.features.outbox import outbox_model


async def lifespan(app):
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(order_controller.router, prefix="/api", tags=["order"])
