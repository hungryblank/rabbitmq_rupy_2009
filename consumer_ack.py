import pika
import asyncore

conn = pika.AsyncoreConnection(pika.ConnectionParameters(
    '127.0.0.1',
    credentials = pika.PlainCredentials('guest', 'guest')))

ch = conn.channel()
ch.queue_declare(queue="sport", durable=False, exclusive=False, auto_delete=False)

def handle_delivery(method, header, body):
    print "sport:  '%r'" % (body)
    ch.basic_ack(delivery_tag = method.delivery_tag)

ch.basic_consume(handle_delivery, queue = 'sport', no_ack = False)
asyncore.loop()
