#import socket
import socket

#Define socket address information
serverAddress = '127.0.0.1'
serverPort = 8000

#create a socket obj
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#attempt connect to server
connectionSocket.connect((serverAddress, serverPort))

serverData = connectionSocket.recv(1024)
print(serverData)

connectionSocket.send(b' world')

connectionSocket.close()