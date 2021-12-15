import time
from socket import *

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1.0)
message = 'ping'
# server adress from given server code
address = ("localhost", 12000)
for i in range(1, 11):
    start = time.time()
    client_socket.sendto(message.encode(), address)
    try:
        response, server = client_socket.recvfrom(1024)
        end = time.time()
        RTT = end - start

        print('#' + str(i))
        print('Response_message: ' + response.decode())
        print('RTT: ' + str(RTT) + " seconds")
    except timeout:
        print('#' + str(i))
        print('Request timed out')
print("Good Bye...")
client_socket.close()
