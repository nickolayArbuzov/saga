from aio_pika import IncomingMessage
from uuid import UUID
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
            message_id = UUID(body["message_id"])
            event_type = body["event_type"]
            payload = body["payload"]

            async with session_scope(AsyncSessionLocal) as session:
                exists = await session.get(InboxModel, message_id)
                if exists:
                    return

                session.add(
                    InboxModel(id=message_id, event_type=event_type, payload=payload)
                )

                usecase_class = USECASE_MAP.get(event_type)
                if usecase_class:
                    await usecase_class(session).execute(payload)
                else:
                    print(f"⚠️ Unknown event type: {event_type}")

        except Exception as e:
            raise e
