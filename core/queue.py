import pika
import snapse
import gzip
import json


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

channel.queue_declare(queue='images')


def callback(ch, method, properties, body):
    data = json.loads(body)
    snapse.resize(data['image'], data['width'], data['height'])
    channel.confirm_delivery()


channel.basic_consume(
    queue='images', on_message_callback=callback, auto_ack=True)

print('Queue is started. To exit press CTRL+C')
channel.start_consuming()
