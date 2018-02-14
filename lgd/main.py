# coding=utf-8

import pika
from pika import BasicProperties
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic

from lgba.messages.base import BaseMessage

# TODO: settings definition
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='commands')


def callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
    # pprint(ch)
    # pprint(method)
    # pprint(properties)
    # TODO: message processors
    print(BaseMessage.deserialize(body))


channel.basic_consume(
    callback,
    queue='commands',
    no_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
