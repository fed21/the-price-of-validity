import os

def take_data(path):
    with open(path,'r') as file:
        lines = file.readlines()
        result = float(lines[0].replace('\n',''))
        messages = int(lines[1].replace('\n',''))
        time = float(lines[2].replace('\n',''))
        # time = float('%.3f'%float(lines[2].replace('\n','')))
    return [result, messages, time]
            
hosts = 19
path = os.getcwd()+'\\results'
total_data = [0.0, 0, 0.0]
max_messages = 0

for host in range(hosts):
    data = take_data(path+'\\'+str(host)+'.txt')
    if(data[0] != 0.0):
        total_data[0] += data[0]
        total_data[2] += data[2]
    total_data[1] += data[1]
    if(data[1] > max_messages):
        max_messages = data[1]
    

print(f'Result: {total_data[0]}\nTotal messages: {total_data[1]}\nTotal time: {total_data[2]}\nMax messages: {max_messages}')