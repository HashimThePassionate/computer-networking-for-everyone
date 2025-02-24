import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8080))  # Bind to all network interfaces on port 8080
server_socket.listen(1)  # Listen for a client connection
print("Server is waiting for a connection...")

conn, addr = server_socket.accept()
print(f"Connected to {addr}")

message = conn.recv(1024).decode()  # Receive message from client
print(f"Client says: {message}")

conn.send("Hello from server!".encode())  # Respond to client
conn.close()
server_socket.close()