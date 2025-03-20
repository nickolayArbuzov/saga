from celery import Celery

celery_app = Celery(
    "payment_service", broker="amqp://guest:guest@localhost:5672//", backend="rpc://"
)

celery_app.autodiscover_tasks(["src.tasks"])
