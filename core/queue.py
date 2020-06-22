import pika
import snapse
import json
import base64
import hashlib

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

channel.queue_declare(queue='images')


def callback(ch, method, properties, body):
    data = json.loads(body)
    image = base64.decodebytes(bytes(data['image'], encoding='utf-8'))
    width = int(data['width'])
    height = int(data['height'])
    name = hashlib.md5(data).hexdigest()
    snapse.resize(image, width, height, name)
    channel.confirm_delivery()


channel.basic_consume(
    queue='images', on_message_callback=callback, auto_ack=True)

print('Queue is started. To exit press CTRL+C')
channel.start_consuming()
