import pika
import hashlib
import gzip
import json


class Runner(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='127.0.0.1'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='images')

    def resize(self, image_binary, width, height):
        data = {'image':str(gzip.compress(image_binary)),'width':width, 'height':height}
        self.channel.basic_publish(
            exchange='', routing_key='images', body=json.dumps(data))
        return hashlib.md5(image_binary).hexdigest() + ".png"

    def close(self):
        self.connection.close()
