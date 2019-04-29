from socket import *
import socket
#servername = socket.gethostbyname('www.facebook.com')
name = socket.gethostname()
servername = socket.gethostbyname(name)
# print(servername)
serverport = 8090
clientSocket = socket.socket(AF_INET, SOCK_STREAM)
address = (servername, serverport)
clientSocket.connect(address)

requestMessage = "GET /s.pdf HTTP/1.1\r\nHost: "+ servername +"\r\n\r\n"
splittedData = requestMessage.split()
requestType = splittedData[0]
clientSocket.send(requestMessage.encode())
responseMessage = clientSocket.recv(2048).decode()
print('From Server:', responseMessage)

if "GET" in str(requestType):
    requestedFile = splittedData[1]
    requestedFile = requestedFile[1:]
    if "HTTP/1.1 200 OK" in responseMessage:
        try:
            file = open(requestedFile,'wb')
            while True:
                buffer = clientSocket.recv(2048)
                if not buffer: break
               # print("aloooo "+buffer)
                file.write(buffer)
            file.close()

        except FileNotFoundError:
            print("File save error")
    clientSocket.close()


elif "POST" in str(requestType):
    requestedFile = splittedData[1]
    requestedFile = requestedFile[1:]

    # OKmessage = clientSocket.recv(1024).decode()
    # print('From ServerOK:', OKmessage)
    if "OK" in responseMessage:
        try:
            file = open(requestedFile, 'rb')
            # header = 'HTTP/1.1 200 OK\r\n\r\n'
            # clientSocket.send(header.encode())
            buffer = file.read(2048)
            while buffer:
                # print(buffer)
                clientSocket.send(buffer)
                buffer = file.read(2048)
            file.close()
        except:
            print("Nothing")

clientSocket.close()

# ip=socket.gethostbyname("www.google.com")
# # print(ip)
##############################################
# if requestType.upper() == "GET":
#     headerMessage = clientSocket.recv(1024).decode()
#     print("From Server: " + headerMessage)
#     responseMessage = clientSocket.recv(2048).decode()
#     print("From Server:" + responseMessage)
#     clientSocket.close()