import pika
import hashlib


class Runner(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='127.0.0.1'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='images')

    def send(self, image_binary):
        self.channel.basic_publish(
            exchange='', routing_key='images', body=image_binary)
        return hashlib.md5(image_binary).hexdigest() + ".png"

    def close(self):
        self.connection.close()
