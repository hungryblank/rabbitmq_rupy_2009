import pika
import time
import asyncore

conn = pika.AsyncoreConnection(pika.ConnectionParameters(
        '127.0.0.1',
        credentials=pika.PlainCredentials('guest', 'guest')))

ch = conn.channel()
ch.exchange_declare(exchange="clock", type="fanout")

while True:
    time.sleep(1)
    ch.basic_publish(exchange='clock',
      routing_key="",
      body="it's %i" % time.mktime(time.localtime()),
      properties=pika.BasicProperties(
        content_type = "text/plain",
        delivery_mode = 1
      ))
    asyncore.loop(count = 1)
