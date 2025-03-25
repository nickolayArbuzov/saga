from celery import Celery

celery_app = Celery(
    "delivery_service", broker="amqp://guest:guest@rabbitmq:5672//", backend="rpc://"
)
celery_app.conf.task_default_queue = "delivery_queue"
celery_app.conf.task_routes = {
    "delivery.*": {"queue": "delivery_queue"},
}
celery_app.autodiscover_tasks(["src.tasks"])
