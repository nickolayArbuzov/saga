from celery import Celery


celery_app = Celery(
    "payment_service",
    broker="amqp://guest:guest@rabbitmq:5672//",
    backend="rpc://",
    include=["src.tasks.outbox_publisher"],
)
celery_app.conf.task_default_queue = "payment_queue"
celery_app.conf.task_routes = {
    "payment.*": {"queue": "payment_queue"},
}

celery_app.conf.beat_schedule = {
    "send-outbox-every-minute": {
        "task": "src.tasks.outbox_publisher.send_outbox_events",
        "schedule": 60.0,
    },
}
