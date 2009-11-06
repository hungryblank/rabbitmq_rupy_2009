import pika
import time
import asyncore

conn = pika.AsyncoreConnection(pika.ConnectionParameters(
        '127.0.0.1',
        credentials=pika.PlainCredentials('guest', 'guest')))

ch = conn.channel()
ch.queue_declare(queue="sport", durable=False, exclusive=False, auto_delete=False)

while True:
    time.sleep(1)
    ch.basic_publish(exchange='',
      routing_key="sport",
      body="some footballer kicked a ball",
      properties=pika.BasicProperties(
        content_type = "text/plain",
        delivery_mode = 1
      ))
    asyncore.loop(count = 1)
