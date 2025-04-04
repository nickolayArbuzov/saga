from celery import Celery


celery_app = Celery(
    "order_service",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="rpc://",
    include=["src.tasks.order_publisher", "src.tasks.order_consumer"],
)
celery_app.conf.task_default_queue = "order_queue"
celery_app.conf.task_routes = {
    "order.*": {"queue": "order_queue"},
}

celery_app.conf.beat_schedule = {
    "send-outbox-every-minute": {
        "task": "src.tasks.order_publisher.send_outbox_events",
        "schedule": 60.0,
    },
}
