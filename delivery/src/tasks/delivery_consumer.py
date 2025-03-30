from src.tasks.celery_app import celery_app
from src.features.delivery.delivery_service import schedule_delivery


@celery_app.task(name="delivery.schedule", acks_late=True)
def delivery_schedule_consumer(payload):
    schedule_delivery(payload)
