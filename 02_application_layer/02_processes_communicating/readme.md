# 📡 **Processes Communicating**

Before building your network application, it is essential to understand how programs running in multiple end systems communicate with each other. In operating system terminology, **it is not programs but processes that communicate**. A process is essentially a running program within an end system.

## 🏛 Interprocess Communication

- When **processes run on the same end system**, they communicate via **interprocess communication**, governed by the operating system.
- When **processes run on different end systems**, they communicate by **exchanging messages** across a computer network.

In a networked environment, processes interact by sending and receiving **messages** across the network. A sending process generates and transmits messages, while the receiving process **processes and possibly responds** to those messages. 🔄📩

📌 **Processes communicating over a network operate in the application layer of the five-layer protocol stack.**

---

## 🖥️ Client and Server Processes

A **network application** consists of **pairs of processes** that exchange messages over a network. For example:

- In a **Web application**, a **client browser process** communicates with a **Web server process**. 🌍📨
- In a **P2P file-sharing system**, one peer's process transfers a file to another peer's process. 🔄💾

For each pair of communicating processes, we label them as:

- **Client Process** – Initiates communication.
- **Server Process** – Waits to be contacted.

### 🔹 Understanding Client & Server Roles

✅ **Web Example**: A **browser** (client) contacts a **Web server** (server). 🌐💻

✅ **P2P Example**: Peer **A downloads** a file from Peer **B**, making **A the client** and **B the server**. 🔄📂

📌 In P2P networks, a process can act **both as a client and a server**. However, during any given communication session, one is still labeled the client and the other the server.

### 📌 Client and Server Definition

- **Client**: The process that initiates contact in a communication session. ⚡
- **Server**: The process that waits to be contacted. 🕒

For example, when **Peer A requests a file from Peer B**, **Peer A is the client** and **Peer B is the server** for that session. 🖥️➡️🖥️

---

## 🖥️💻 Simple Code Explanation for Client and Server

To understand the communication between client and server processes, let’s look at a basic example using Python’s built-in **socket** library.

### 🚀 Server Code (Listening for Connections)

```python
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
```

### 🔹 Explanation of Server Code

✅ **Creates a socket** to listen for incoming connections.&#x20;

✅ **Binds** the socket to a specific IP and port.&#x20;

✅ **Listens** for an incoming connection from a client.&#x20;

✅ **Accepts** a connection when a client contacts it.&#x20;

✅ **Receives and processes a message** from the client.&#x20;

✅ **Sends a response** to the client before closing the connection.&#x20;

---

### 🚀 Client Code (Initiates Connection)

```python
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))  # Connect to server on localhost

client_socket.send("Hello, Server!".encode())  # Send a message to the server
response = client_socket.recv(1024).decode()  # Receive response from the server
print(f"Server says: {response}")

client_socket.close()
```

### 🔹 Explanation of Client Code

✅ **Creates a socket** to connect to the server.&#x20;

✅ **Connects** to a specific server (IP + Port).&#x20;

✅ **Sends a message** to the server.&#x20;

✅ **Receives the server’s response** and prints it.&#x20;

✅ **Closes the connection** once communication is complete.&#x20;

---

## 🎯 Conclusion

Understanding **how processes communicate over a network** is fundamental to designing network applications. The distinction between **client and server processes** helps developers structure their applications effectively. 🚀

- **Clients initiate communication**, while **servers wait for requests**. ⚡
- In **P2P networks**, roles can switch dynamically. 🔄
- Using **sockets**, we can establish and manage network communication efficiently. 💡
