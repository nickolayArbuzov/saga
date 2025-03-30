from src.tasks.celery_app import celery_app
from src.database import SessionLocal
from src.features.outbox.outbox_model import OutboxModel

from sqlalchemy import select


@celery_app.task
def send_outbox_events():
    with SessionLocal() as session:
        events = (
            (session.execute(select(OutboxModel).where(OutboxModel.sent == False)))
            .scalars()
            .all()
        )
        for event in events:
            celery_app.send_task(
                event.type,
                args=[{"payload": event.payload}],
                queue="payment_queue",
            )
            event.sent = True
        session.commit()
