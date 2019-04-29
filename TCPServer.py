
from socket import *
import socket
# import sys
# import _thread
import threading

serverSocket = socket.socket(AF_INET, SOCK_STREAM)
print("Socket Created")

name = socket.gethostname()
ip = socket.gethostbyname(name)
port = 8090
address = (ip, port)
serverSocket.bind(address)
print("Socket has been bounded")
serverSocket.listen(5)


def clientThreadHandler(connectionSocket):
    # try:
     #welcomeMessage = "Welcome to the server!\n"
     #connectionSocket.send(welcomeMessage.encode())

        # while True:
    print("Server started listening on ip: " + str(ip) + " | port:" + str(port))
    data = connectionSocket.recv(2048).decode()
    if not data:
        connectionSocket.close()
        # break

    print("what we got from client " + str(data))
    splittedData = data.split()
    requestType = splittedData[0]
    # print(requestType)
    requestedFile = splittedData[1]
    requestedFile = requestedFile[1:]
    if requestedFile == "":
        requestedFile = "data.html"
    # print(requestedFile)

    if "GET" in str(requestType):
        try:
            file = open(requestedFile, 'rb')
            header = 'HTTP/1.1 200 OK\r\n\r\n'
            connectionSocket.send(header.encode())
            buffer = file.read(2048)
            while buffer:
                # print(buffer)
                connectionSocket.send(buffer)
                buffer = file.read(2048)
            file.close()
        except FileNotFoundError:
            header = 'HTTP/1.0 404 Not Found\r\n\r\n'
            connectionSocket.send(header.encode())
       # connectionSocket.close()
    elif "POST" in str(requestType):
        header = "OK"
        connectionSocket.send(header.encode())
        try:
            file = open(requestedFile, 'wb')
            while True:
                buffer = connectionSocket.recv(2048)
                if not buffer: break
                # print("aloooo "+buffer)
                file.write(buffer)
            file.close()

        except FileNotFoundError:
            print("File save error")
       # connectionSocket.close()
    connectionSocket.close()
    # except Exception:
    #     import traceback
    #     print("E= " +str(Exception))
while True:
        connectionSocket, address = serverSocket.accept()
        print("Got a connection from " + str(address[0]) + " | " + str(address[1]))
        # try:
        #     _thread.start_new_thread(clientThreadHandler, (connectionSocket,))
        # except:
        #   print("Error: unable to start thread")

        # threads for clients
        client_thread_handler = threading.Thread(
            target=clientThreadHandler,
            args=(connectionSocket,)
        )
        client_thread_handler.start()

#serverSocket.close()





# from socket import *
# serverPort = 12000
# serverSocket = socket(AF_INET, SOCK_STREAM)
# serverSocket.bind(('', serverPort))
# serverSocket.listen(1)
# print("The server is ready to receive")
# while True:
#     connectionSocket, addr = serverSocket.accept()
#     print(addr)
#     sentence = connectionSocket.recv(1024).decode()
#     capitalizedSentence = sentence.upper()
#     connectionSocket.send(capitalizedSentence.encode())
#     connectionSocket.close()

