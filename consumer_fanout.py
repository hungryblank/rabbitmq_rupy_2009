#!/usr/bin/env python
'''
Example of simple consumer, waits one message, replies an ack and exits.
'''

import os
import pika
import asyncore

conn = pika.AsyncoreConnection(pika.ConnectionParameters(
    '127.0.0.1',
    credentials = pika.PlainCredentials('guest', 'guest')))

ch = conn.channel()
queue_name = "consumer-%i" % os.getpid()
ch.queue_declare(queue=queue_name, durable=False, exclusive=True)
ch.queue_bind(queue = queue_name, exchange = 'clock', routing_key = '')

def handle_delivery(method, header, body):
    print body

ch.basic_consume(handle_delivery, queue = queue_name, no_ack = True)
asyncore.loop()
