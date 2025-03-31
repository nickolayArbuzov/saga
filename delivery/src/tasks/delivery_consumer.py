from src.database import SessionLocal
from src.tasks.celery_app import celery_app
from src.features.delivery.sync_use_cases.process_delivery import ProcessDeliveryUseCase


@celery_app.task(name="delivery.process", acks_late=True)
def delivery_process_consumer(payload):
    db = SessionLocal()
    try:
        usecase = ProcessDeliveryUseCase(db)
        usecase.execute(payload)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
