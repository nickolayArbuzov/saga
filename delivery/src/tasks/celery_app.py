from celery import Celery


celery_app = Celery(
    "delivery_service",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="rpc://",
    include=["src.tasks.delivery_publisher", "src.tasks.delivery_consumer"],
)
celery_app.conf.task_default_queue = "delivery_queue"
celery_app.conf.task_routes = {
    "delivery.*": {"queue": "delivery_queue"},
}

celery_app.conf.beat_schedule = {
    "send-outbox-every-minute": {
        "task": "src.tasks.delivery_publisher.send_outbox_events",
        "schedule": 60.0,
    },
}
