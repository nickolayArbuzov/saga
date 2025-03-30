from src.tasks.celery_app import celery_app
from src.features.payment.payment_service import process_payment


@celery_app.task(name="payment.process", acks_late=True)
def payment_process_consumer(payload):
    process_payment(payload)
