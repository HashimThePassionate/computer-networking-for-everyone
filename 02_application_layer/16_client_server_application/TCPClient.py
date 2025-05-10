from socket import *
ServerPort = 12000
Server_name = 'Localhost'
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((Server_name, ServerPort))
sentence = input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
clientSocket.close()