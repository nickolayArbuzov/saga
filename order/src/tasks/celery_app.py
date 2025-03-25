from celery import Celery

celery_app = Celery(
    "order_service", broker="amqp://guest:guest@rabbitmq:5672//", backend="rpc://"
)
celery_app.conf.task_default_queue = "order_queue"
celery_app.conf.task_routes = {
    "order.*": {"queue": "order_queue"},
}
celery_app.autodiscover_tasks(["src.tasks"])
