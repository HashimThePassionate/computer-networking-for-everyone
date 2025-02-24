# **Transport Services Available to Applications 🚀**

## 📌 Overview

A **socket** serves as the interface between an application process and the **transport-layer protocol**. When an application sends a message, it passes through the socket. The transport-layer protocol is responsible for delivering this message to the receiving process's socket. Many networks, including the **Internet**, provide multiple transport-layer protocols.

When developing an application, you must select an appropriate **transport-layer protocol** based on the services it provides. This decision is analogous to choosing between a **train** or an **airplane** for travel between two cities—each mode of transport offers different services. For instance:

- 🚆 **Train:** Offers **downtown pickup and drop-off**
- ✈️ **Airplane:** Provides **shorter travel times**

Similarly, transport-layer protocols provide different services tailored to specific needs.

## 🔍 Key Transport-Layer Services

Transport-layer services can be classified into four broad dimensions:

1. **✅ Reliable Data Transfer** – Ensures that data is delivered correctly and in order.
2. **📈 Throughput** – Determines the amount of data successfully delivered per unit time.
3. **⏳ Timing** – Guarantees specific delays or ensures timely delivery.
4. **🔒 Security** – Provides encryption and data integrity mechanisms.

# **Reliable Data Transfer** 🚀

## 📌 Overview

In computer networks, **packets can be lost** due to various reasons:

- 🔄 **Buffer overflow** in routers.
- ⚠️ **Corruption of bits** in transmission.
- ❌ **Discarding of packets** by routers or hosts.

For **critical applications** such as:

- 📧 **Email**
- 📂 **File Transfer**
- 🌐 **Web document transfers**
- 🏦 **Financial transactions**

loss of data can lead to **devastating consequences**. Therefore, a mechanism is required to **ensure that data is delivered correctly and completely**. This mechanism is known as **reliable data transfer (RDT)**.

## 🔹 What is Reliable Data Transfer?

A transport-layer protocol that guarantees that data sent by one end is **correctly and completely received** by the other end is said to provide **reliable data transfer**.

When a transport protocol provides **process-to-process reliable data transfer**:

✅ The sending process can pass its data into the **socket**, ensuring delivery **without errors**.


✅ The receiving process gets the **same data** in order, without corruption or loss.

### **When is Reliable Data Transfer Not Needed?**

- Some applications, such as **multimedia streaming (audio/video calls, live broadcasts)**, can tolerate **some data loss**.
- Losing small amounts of data might only cause **minor glitches** but does not render the communication useless.

## 🔄 Implementing Reliable Data Transfer with TCP

The **Transmission Control Protocol (TCP)** is a widely used transport-layer protocol that ensures **reliable** data transfer. Below is an example demonstrating **TCP-based communication** between a client and a server.

### **🔹 TCP Server Example (Reliable Data Reception)**

```python
import socket  # Importing the socket library

# Create a TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))  # Bind to localhost on port 8080
server_socket.listen(1)  # Allow 1 connection

print("Server is waiting for a connection...")
conn, addr = server_socket.accept()  # Accept an incoming connection
print(f"Connected to {addr}")

# Receiving data reliably
data = conn.recv(1024).decode()  # Receive data from the client
print(f"Received: {data}")

# Sending acknowledgment
conn.send("Data received successfully!".encode())

conn.close()  # Close the connection
```

### **🔍 Code Breakdown**

- `socket.AF_INET`: Uses **IPv4 addressing**.
- `socket.SOCK_STREAM`: Specifies a **TCP** connection.
- `bind(('localhost', 8080))`: Binds the socket to **port 8080**.
- `listen(1)`: Allows **one** client to connect.
- `accept()`: Accepts a **client connection**.
- `recv(1024)`: Receives **data reliably**.
- `send()`: Sends an acknowledgment to the client.

### **🔹 TCP Client Example (Reliable Data Sending)**

```python
import socket  # Importing the socket library

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))  # Connect to the server

message = "Hello, Server! This is reliable data transfer."
client_socket.send(message.encode())  # Send data

# Receiving acknowledgment
ack = client_socket.recv(1024).decode()
print(f"Acknowledgment from server: {ack}")

client_socket.close()  # Close the connection
```

### **🔍 Code Breakdown**

- `socket.SOCK_STREAM`: Establishes a **TCP connection**.
- `connect(('localhost', 8080))`: Connects to the **server**.
- `send()`: Sends **reliable** data to the server.
- `recv(1024)`: Receives an acknowledgment ensuring **successful delivery**.
