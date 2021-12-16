import ssl
from base64 import *
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ('smtp.gmail.com', 587)  # Fill in start #Fill in end
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# Fill in end
recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
recv1 = recv1.decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

command = 'STARTTLS\r\n'.encode()
clientSocket.send(command)
recv2 = clientSocket.recv(1024).decode()
print(recv2)

if recv2[:3] != '220':
    print('220 reply not received from server')

# Encrypt the socket
clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.send("AUTH LOGIN ".encode() + b64encode("cse476.2022@gmail.com".encode()) + "\r\n".encode())
recv3 = clientSocket.recv(1024)
print(recv3)
if (recv3[:3] != "334"):
    print('334 reply not received from server.')

clientSocket.send(b64encode("Gtuforever123.".encode()) + "\r\n".encode())
recv4 = clientSocket.recv(1024)
print(recv4)
if (recv4[:3] != "235"):
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <cse476.2022@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv5 = clientSocket.recv(1024)
print(recv5)
if (recv5[:3] != '250'):
    print('250 reply not received from server.')
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = "RCPT TO: <akif.kartal2017@gtu.edu.tr>\r\n"
clientSocket.send(rcptToCommand.encode())
recv6 = clientSocket.recv(1024)
print(recv6)
if (recv6[:3] != '250'):
    print('250 reply not received from server.')
# Fill in end


# Send DATA command and print server response.
# Fill in start
dataCommand = "Data\r\n"
clientSocket.send(dataCommand.encode())
recv7 = clientSocket.recv(1024)
print(recv7)
if (recv7[:3] != '354'):
    print('354 reply not received from server.')
# Fill in end


# Send message data.
# Fill in start
message = "SUBJECT: cse476 Mail Test\nMail content" + msg + endmsg
clientSocket.send(message.encode())
recv8 = clientSocket.recv(1024)
print(recv8)
if (recv8[:3] != '250'):
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
Quit = "Quit\r\n"
print("Quit Message was sent")
clientSocket.send(Quit.encode())
recv9 = clientSocket.recv(1024)
print(recv9)
if (recv9[:3] != '221'):
    print('221 reply not received from server.')

print("Mail was sent. Good Bye...")
# Fill in end

clientSocket.close()
