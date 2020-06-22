import pika
import hashlib
import json
import base64


class Runner(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='127.0.0.1'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='images')

    def resize(self, image_binary, width, height):
        image = base64.encodebytes(image_binary).decode('utf-8')
        data = {'image': image, 'width': width, 'height': height}
        data = json.dumps(image_binary)
        self.channel.basic_publish(
            exchange='', routing_key='images', body=data)
        return hashlib.md5(data).hexdigest() + ".png"

    def close(self):
        self.connection.close()
