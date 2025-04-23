import aio_pika
from src.broker.handler import on_message


async def start_consumer():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()

    queue = await channel.declare_queue("order.events", durable=True)
    await queue.consume(on_message)
