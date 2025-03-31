from src.database import SessionLocal
from src.tasks.celery_app import celery_app
from src.features.payment.sync_use_cases.process_payment import ProcessPaymentUseCase
from src.features.payment.sync_use_cases.rollback_payment import RollbackPaymentUseCase


@celery_app.task(name="payment.process", acks_late=True)
def payment_process_consumer(payload):
    db = SessionLocal()
    try:
        usecase = ProcessPaymentUseCase(db)
        usecase.execute(payload)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


@celery_app.task(name="payment.rollback", acks_late=True)
def payment_process_consumer(payload):
    db = SessionLocal()
    try:
        usecase = RollbackPaymentUseCase(db)
        usecase.execute(payload)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
