import pika
import snapse
import json
import base64

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()

channel.queue_declare(queue='images')


def rescaler(ch, method, properties, body):
    data = json.loads(body)
    image = base64.decodebytes(bytes(data['image'], encoding='utf-8'))
    width = int(data['width'])
    height = int(data['height'])
    snapse.resize(image, width, height)
    channel.confirm_delivery()


def formater(ch, method, properties, body):
    data = json.loads(body)
    image = base64.decodebytes(bytes(data['image'], encoding='utf-8'))
    kind = data['kind']
    snapse.formater(image, kind)
    channel.confirm_delivery()


channel.basic_consume(
    queue='resize', on_message_callback=rescaler, auto_ack=True)

channel.basic_consume(
    queue='filter', on_message_callback=formater, auto_ack=True)

print('Queues are started. To exit press CTRL+C')
channel.start_consuming()
