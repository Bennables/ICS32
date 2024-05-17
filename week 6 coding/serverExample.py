#import he sockets lib
import socket

#using the get host function
#print("Desktop Name: " +socket.gethostname())

#using the looback addy as servier ip addy
serverAddress = '127.0.0.1'

#def a port nnumber for server
port = 8000

#create a socket obj
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind my host with my port number
serverSocket.bind((serverAddress, port))

#setup socket using listen
# 5 means max num connections socket allows
serverSocket.listen(0)

connectionCounter=  0 
contToru = True
while contToru:
#begin accepting incoming connection requrests
    clientSocket, clientAddress = serverSocket.accept()
    connectionCounter +=1

    #printing the client address
    print("Client connected from: ", clientAddress)

    clientSocket.send(b'Hello')
    clientData = clientSocket.recv(1024)
    print(clientData.decode('ascii'))

    if connectionCounter == 10:
        contToru = False
        serverSocket.close()