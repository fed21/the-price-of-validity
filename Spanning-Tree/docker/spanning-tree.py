import random
import threading
import pika
import os, logging, time
import ast

logging.basicConfig()

def set_bit(sequence, function_index):
    global bits
    bit_position = count_leading_zeros(sequence) # index of last tail
    bits[function_index][bit_position] = 1

def count_leading_zeros(binary_vector):
    count = 0
    for bit in binary_vector:
        if str(bit) == "0":
            count += 1
        else:
            break
    return count

def generate_vectors():
    global num_vectors, vector_size
    vectors = []
    for i in range(num_vectors):
        vector = [random.randint(0, 1) for _ in range(vector_size)]
        vectors.append(vector)
        set_bit(vector, i)
    return vectors

def FM ():
    global bits, num_vectors
    leading_zeros = []
    print(f'Bits finale: {bits}')
    for i in range(num_vectors):
        bit_vector = bits[i]
        max_zero_position = count_leading_zeros(bit_vector)
        leading_zeros.append(max_zero_position)
    max_zero_position = max(leading_zeros)
    estimated_distinct_elements = 2 ** max_zero_position / 0.78
    return estimated_distinct_elements

def activate():
    global active
    active = True

def deactivate():
    global active
    active = False

def process_message(ch, method, properties, body):
    global processed_msgs, neighbors, val, bits, return_node, vectors, active, start, end
    processed_msgs = processed_msgs + 1
    decoded_body = body.decode('ASCII')
    # Se sono il nodo da cui inizia la computazione
    time_message_received = time.time()
    print(f'[+] Receiving message: {decoded_body}')
    if decoded_body == 'start':
        start = time_message_received
        for node_dest in neighbors:
            send_message('broadcast', val, node_dest)
        activate()
        start_timer()
    else:
        end = time_message_received
        if decoded_body == 'stop':
            close_connections()
        # Logic for processing the received message
        message_parts = decoded_body.split(';')

        # Extract message components
        message_type = message_parts[0]
        value = message_parts[1]
        sender = message_parts[2]
        
        if message_type == 'broadcast':
            if not active:
                start_timer()
                return_node = sender
                random_broadcast = len(neighbors)
                if(isdead == 'true'):
                    random_broadcast = random.randint(1, len(neighbors)+1)
                for i in range(random_broadcast):
                    send_message('broadcast', val, neighbors[i])
                if(isdead == 'true'):
                    close_connections()
                activate()
                send_message('convergecast', bits, return_node)
        else:
            # val = val || value  # Operation to be performed
            ### OPERAZIONE DI OR TRA VETTORI
            value = ast.literal_eval(value)
            bits = [[bit1 | bit2 for bit1, bit2 in zip(sublist1, sublist2)] for sublist1, sublist2 in zip(bits, value)]
            if return_node != None:
                send_message('convergecast', bits, return_node)

def send_message(message_type, value, destination):
    global channel, id, val
    message = f"{message_type};{value};{id}"
    channel.basic_publish(
        exchange='',
        routing_key=destination,
        body=message
    )
    print(f"[+] Sending message to {destination}: {message}")

def start_timer():
    global timer, timer_delta
    if timer:
        timer.cancel()  # Cancel previous timer if exists
    timer = threading.Timer(timer_delta, return_value)
    timer.start()

def return_value():
    global return_node, bits, processed_msgs, end, start, val
    ### Timer expired
    result = 0
    if return_node==None:
        ### ritorno numero di valori
        result = FM()
        print(f"[+] The result of the count is: {result}")
    print(f'[+] Processed Messages: {processed_msgs}')
    computed_time = end-start
    with open(f'/app/results/{val}.txt', 'w') as file:
        file.write(f'{result}\n{processed_msgs}\n{computed_time}')

def close_connections():
    global connection
    connection.close()

def main():
    global vectors, channel, connection
    with open(f'/app/results/{val}.txt', 'w') as file:
        file.write(f'0\n0\n0')
    vectors = generate_vectors()
    print('[+] Inizializing ' + id)
    url_amqp = os.environ['URL_AMQP']
    url = os.environ.get('CLOUDAMQP_URL', url_amqp)
    params = pika.URLParameters(url)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params) # Connect to CloudAMQP
    channel = connection.channel() # start a channel
    channel.queue_declare(queue=id)
    print('[+] Queue declared ' + id)
    channel.basic_consume(queue=id, on_message_callback=process_message, auto_ack=True)
    print('[+] Starting consuming on ' + id)
    print(f'[+] Vectors : {vectors}')
    print('[+] List of neighbors:')
    for neighbor in range(len(neighbors)):
        print(f'    [-] {neighbor}')
    channel.start_consuming() 

if __name__ == '__main__':
    id = os.environ['QUEUE']
    isdead = os.environ['DEAD']
    val = id.split('-')[1]
    neighbors = os.environ['NEIGHBORS_LIST'].split(',')
    return_node = None
    num_vectors = int(os.environ['NUM_VECTORS'])
    vector_size = 16
    bits = [[0] * vector_size for _ in range(num_vectors)]
    print(f'Dimension of Vector: {len(bits)} x {len(bits[0])}')
    vectors = []
    active = False
    timers = {}  # Dictionary to store timers for each neighbor
    connections = {}  # Dictionary to store RabbitMQ connections for each neighbor
    connection = None
    timer_delta = 5
    timer = None
    processed_msgs = 0
    channel = None
    start = 0.0
    end = 0.0
    main()
