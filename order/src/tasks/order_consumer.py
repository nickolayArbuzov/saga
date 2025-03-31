from src.database import SessionLocal
from src.tasks.celery_app import celery_app
from src.features.order.sync_use_cases.process_order import ProcessOrderUseCase
from src.features.order.sync_use_cases.rollback_order import RollbackOrderUseCase


@celery_app.task(name="order.process", acks_late=True)
def order_process_consumer(payload):
    db = SessionLocal()
    try:
        usecase = ProcessOrderUseCase(db)
        usecase.execute(payload)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


@celery_app.task(name="order.rollback", acks_late=True)
def order_process_consumer(payload):
    db = SessionLocal()
    try:
        usecase = RollbackOrderUseCase(db)
        usecase.execute(payload)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
