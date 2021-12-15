import ssl
from base64 import *
from socket import *

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("mail.smtp2go.com", 5000)  # Fill in start #Fill in end
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
recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server')

# Encrypt the socket
clientSocket = ssl.wrap_socket(clientSocket)
clientSocket.send("AUTH LOGIN " + b64encode("lab3@gmail.com".encode()) + "\r\n")
recv3 = clientSocket.recv(1024)
print(recv3)
if (recv3[:3] != "334"):
    print('334 reply not received from server.')

clientSocket.send(b64encode("gtuforever".encode()) + "\r\n")
recv4 = clientSocket.recv(1024)
print(recv4)
if (recv4[:3] != "235"):
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <lab3@gmail.com>\r\n"
clientSocket.send(mailFrom.encode())
recv5 = clientSocket.recv(1024)
print(recv5)
if (recv5[:3] != '250'):
    print('250 reply not received from server.')
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start
rcptToCommand = "RCPT TO: <lab3_1@gmail.com>\r\n"
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
message = "SUBJECT: SMTP Mail Client Test\nSMTP Mail Client Test Content" + msg + endmsg
clientSocket.send(message.encode())
recv8 = clientSocket.recv(1024)
print(recv8)
if (recv8[:3] != '250'):
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
Quit = "Quit\r\n"
print(Quit)
clientSocket.send(Quit.encode())
recv9 = clientSocket.recv(1024)
print(recv9)
if (recv9[:3] != '221'):
    print('221 reply not received from server.')

print("Mail Sent")
# Fill in end

clientSocket.close()
