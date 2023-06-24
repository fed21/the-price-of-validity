# example_publisher.py
import pika, os, logging
logging.basicConfig()

# Parse CLODUAMQP_URL (fallback to localhost)

#amqps://ihhuwrwo:kDQ69TDnElY2FIg5IyzmxTZcLCBslbtb@rat.rmq2.cloudamqp.com/ihhuwrwo

url = os.environ.get('CLOUDAMQP_URL', 'amqps://ihhuwrwo:kDQ69TDnElY2FIg5IyzmxTZcLCBslbtb@rat.rmq2.cloudamqp.com/ihhuwrwo')
params = pika.URLParameters(url)
params.socket_timeout = 5
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel() # start a channel
# channel.queue_declare(queue='coda2') # Declare a queue
# send a message

channel.basic_publish(exchange='', routing_key='coda2', body='Ciao')
print ("[x] Message sent to consumer")
connection.close()