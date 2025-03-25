from celery import Celery

celery_app = Celery(
    "payment_service", broker="amqp://guest:guest@rabbitmq:5672//", backend="rpc://"
)
celery_app.conf.task_default_queue = "payment_queue"
celery_app.conf.task_routes = {
    "payment.*": {"queue": "payment_queue"},
}
celery_app.autodiscover_tasks(["src.tasks"])
