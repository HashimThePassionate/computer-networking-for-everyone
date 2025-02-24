import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))  # Connect to server on localhost

client_socket.send("Hello, Server!".encode())  # Send a message to the server
response = client_socket.recv(1024).decode()  # Receive response from the server
print(f"Server says: {response}")

client_socket.close()