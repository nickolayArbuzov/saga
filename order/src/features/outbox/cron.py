import asyncio
from sqlalchemy import select, update
from src.features.outbox.outbox_model import OutboxModel
from src.broker.publisher import publish_event
from src.dependencies import session_scope
from src.database import AsyncSessionLocal


async def run_outbox_publisher():
    while True:
        async with session_scope(AsyncSessionLocal) as session:
            result = await session.execute(
                select(OutboxModel).where(OutboxModel.processed == False)
            )
            events = result.scalars().all()
            for event in events:
                await publish_event(event.event_type, event.payload, event.routing_key)
                await session.execute(
                    update(OutboxModel)
                    .where(OutboxModel.id == event.id)
                    .values(processed=True)
                )
        await asyncio.sleep(60)

