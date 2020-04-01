import pika
import snapse
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672))
channel = connection.channel()

channel.queue_declare(queue='images')


def callback(ch, method, properties, body):
    snapse.resize(body)
    channel.confirm_delivery()


channel.basic_consume(
    queue='images', on_message_callback=callback, auto_ack=True)

print('Queue is started. To exit press CTRL+C')
channel.start_consuming()
