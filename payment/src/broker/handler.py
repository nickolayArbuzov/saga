from sqlalchemy import select
from aio_pika import IncomingMessage
import json
from src.dependencies import session_scope
from src.database import AsyncSessionLocal
from src.features.inbox.inbox_model import InboxModel
from src.features.payment.usecases.create_payment import CreatePaymentUseCase
from src.features.payment.usecases.cancel_payment import CancelPaymentUseCase

USECASE_MAP = {
    "payment.process": CreatePaymentUseCase,
    "payment.rollback": CancelPaymentUseCase,
}


async def on_message(msg: IncomingMessage):
    async with msg.process(requeue=True):
        try:
            body = json.loads(msg.body)
            event_type = body["event_type"]
            payload = body["payload"]
            event_id = payload["event_id"]
            async with session_scope(AsyncSessionLocal) as session:
                exists = (
                    await session.execute(
                        select(InboxModel).where(InboxModel.event_id == event_id)
                    )
                ).scalar_one_or_none()

                if exists:
                    return

                session.add(
                    InboxModel(event_id=event_id, payload=payload, processed=False)
                )

                usecase_class = USECASE_MAP.get(event_type)
                if usecase_class:
                    await usecase_class(session).execute(payload)
                else:
                    print(f"⚠️ Unknown event type: {event_type}")

        except Exception as e:
            raise e
