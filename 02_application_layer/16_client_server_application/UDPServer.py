from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    
    print("Raw message (bytes):", message)
    print("Decoded message (string):", message.decode())
    
    print("Client address tuple:", clientAddress)
    print("Client IP:", clientAddress[0])
    print("Client port:", clientAddress[1])
    
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
