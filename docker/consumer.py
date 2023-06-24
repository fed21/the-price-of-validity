# example_publisher.py
import pika, os, logging, sys

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

logging.basicConfig()

#amqps://ihhuwrwo:kDQ69TDnElY2FIg5IyzmxTZcLCBslbtb@rat.rmq2.cloudamqp.com/ihhuwrwo
def main():

    neighbours = os.environ['NEIGHBOURS_LIST'].split(',')
    container_queue = os.environ['QUEUE']
    
    url = os.environ.get('CLOUDAMQP_URL', 'amqps://ihhuwrwo:kDQ69TDnElY2FIg5IyzmxTZcLCBslbtb@rat.rmq2.cloudamqp.com/ihhuwrwo')
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    channel = connection.channel() # start a channel
    channel.queue_declare(queue=container_queue) # Declare a queue
    print(' [*] Declared Queue ' + container_queue)
   
    # receive a message
    channel.basic_consume(queue=container_queue, on_message_callback=callback, auto_ack=True)
    print(' [*] Waiting for messages')
    channel.start_consuming()

if __name__ == '__main__':
    main()

