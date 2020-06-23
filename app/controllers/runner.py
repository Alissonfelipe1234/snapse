import pika
import hashlib
import json
import base64


class Runner(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='127.0.0.1'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='resize')
        self.channel.queue_declare(queue='filter')

    def resize(self, image_binary, width, height):
        image = base64.encodebytes(image_binary).decode('utf-8')
        data = {'image': image, 'width': width, 'height': height}
        data = json.dumps(data)
        self.channel.basic_publish(
            exchange='', routing_key='resize', body=data)
        name = image_binary + bytes(width) + bytes(height)
        return hashlib.md5(name).hexdigest() + ".png"

    def formater(self, image_binary, kind):
        image = base64.encodebytes(image_binary).decode('utf-8')
        data = {'image': image, 'kind': kind}
        data = json.dumps(data)
        self.channel.basic_publish(
            exchange='', routing_key='filter', body=data)
        name = image_binary + bytes(kind, encoding='utf-8')
        return hashlib.md5(name).hexdigest() + ".png"

    def close(self):
        self.connection.close()
