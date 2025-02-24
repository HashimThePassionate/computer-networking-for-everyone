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

---

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

---

#  **Throughput in Network Communication** 🚀

## 📌 Overview
**Throughput** refers to the rate at which the **sending process delivers bits** to the **receiving process** in a communication session over a network path. Since multiple sessions share bandwidth, the **available throughput fluctuates** over time.

A **transport-layer protocol** can offer a service to guarantee a **minimum available throughput**. This is particularly crucial for **bandwidth-sensitive applications**, which require a consistent rate to function effectively.

## 🔹 Importance of Guaranteed Throughput
A **guaranteed throughput service** ensures that an application always receives a specified data rate **r bits/sec**. This is essential for:
- 🎤 **Internet Telephony** (e.g., VoIP) requiring **32 kbps** for proper voice transmission.
- 🎥 **Streaming video** needing a **minimum throughput** to maintain video quality.
- 🎶 **Live audio broadcasting** that relies on **stable data flow**.

If the network **cannot** meet the application's required throughput, the application may:
- **Lower its data rate** using adaptive encoding.
- **Fail to function properly**, causing disruptions.

## 🔹 Bandwidth-Sensitive vs. Elastic Applications
### **🎯 Bandwidth-Sensitive Applications**
Require a **specific amount of throughput** to function correctly. If the required throughput isn’t met, the application performance **significantly degrades**.
Examples:
- **VoIP calls**
- **Live video streaming**
- **Online gaming**

### **📈 Elastic Applications**
Can function with **varying levels of throughput**. Higher throughput improves performance but is **not mandatory**.
Examples:
- 📧 **Email**
- 📂 **File transfer (FTP, cloud backups)**
- 🌐 **Web browsing**

## 📜 Code Example: Measuring Network Throughput
The following **Python program** demonstrates how to measure the **throughput** of a network connection using a TCP socket.

### **🔹 Server Code (Receiver Side)**
```python
import socket
import time

# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8080))
server_socket.listen(1)

print("Server waiting for connection...")
conn, addr = server_socket.accept()
print(f"Connected to {addr}")

start_time = time.time()
data_received = 0

while True:
    data = conn.recv(4096)  # Receive 4KB chunks
    if not data:
        break
    data_received += len(data)

end_time = time.time()
throughput = (data_received * 8) / (end_time - start_time)  # Convert to bits/sec

print(f"Throughput: {throughput:.2f} bps")
conn.close()
```

### **🔍 Code Breakdown**
- `socket.AF_INET`: Uses **IPv4 addressing**.
- `socket.SOCK_STREAM`: Uses **TCP** for reliable communication.
- `bind(('localhost', 8080))`: Binds the server to **port 8080**.
- `listen(1)`: Allows **one** client connection.
- `recv(4096)`: Receives **4KB** of data at a time.
- Calculates **throughput in bits/sec** using:
  ```python
  throughput = (data_received * 8) / (end_time - start_time)
  ```

### **🔹 Client Code (Sender Side)**
```python
import socket
import time

# Client setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8080))

message = b'X' * 1024 * 1024  # Send 1MB of data
start_time = time.time()

client_socket.sendall(message)
client_socket.close()

end_time = time.time()
duration = end_time - start_time
print(f"Data sent in {duration:.2f} seconds")
```

### **🔍 Code Breakdown**
- `socket.SOCK_STREAM`: Establishes a **TCP connection**.
- `connect(('localhost', 8080))`: Connects to the **server**.
- `b'X' * 1024 * 1024`: Creates **1MB** of dummy data.
- `sendall()`: Ensures the **entire message** is sent before closing.

---

# ⏳ **Timing Guarantees in Transport-Layer Protocols**

## 📌 Overview
Transport-layer protocols can provide **timing guarantees**, ensuring that **data arrives within a specific timeframe**. Similar to **throughput guarantees**, timing constraints vary depending on the application’s needs.

An example of a **timing guarantee** is ensuring that every bit sent into a socket **arrives within 100 milliseconds** at the receiving socket.

This is **critical** for **real-time applications**, such as:
- 🎤 **Internet Telephony (VoIP)** – Avoids unnatural conversation pauses.
- 🎮 **Multiplayer Gaming** – Ensures smooth and responsive gameplay.
- 🖥️ **Virtual Environments** – Maintains immersive interaction.
- 📹 **Teleconferencing** – Reduces lag for effective communication.

For **non-real-time applications** (e.g., **email, file transfer, web browsing**), lower delays are preferable, but **strict constraints aren’t necessary**.

## 🔹 Why Timing Guarantees Matter?
Without proper timing, real-time applications suffer from:
- **🛑 Increased Latency:** Causes noticeable pauses and interruptions.
- **🔄 Jitter Issues:** Uneven delay variations affect streaming and gaming.
- **⏳ Poor User Experience:** Delayed responses impact interactivity.

## 📜 Code Example: Measuring Network Delay
The following **Python script** demonstrates how to measure **network timing (latency/delay)** using **UDP sockets**.

### **🔹 Server Code (Receiver Side)**
```python
import socket
import time

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 8080))
print("Server is ready to receive data...")

while True:
    data, addr = server_socket.recvfrom(1024)  # Receive data
    receive_time = time.time()
    print(f"Received: {data.decode()} from {addr} at {receive_time:.6f} seconds")
    
    # Sending response with timestamp
    server_socket.sendto(str(receive_time).encode(), addr)
```

### **🔍 Code Breakdown**
- `socket.SOCK_DGRAM`: Uses **UDP** for faster, connectionless communication.
- `recvfrom(1024)`: Receives data packets (max **1024 bytes**).
- `time.time()`: Captures **timestamp** when the message arrives.
- `sendto()`: Sends the **timestamp back** to the sender for latency calculation.

### **🔹 Client Code (Sender Side)**
```python
import socket
import time

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 8080)

message = "Timing Test"
start_time = time.time()
client_socket.sendto(message.encode(), server_address)  # Send message

# Receive response with timestamp
data, _ = client_socket.recvfrom(1024)
end_time = time.time()
server_timestamp = float(data.decode())

# Calculate delay
delay = (end_time - start_time) * 1000  # Convert to milliseconds
print(f"Round Trip Time (RTT): {delay:.2f} ms")
```

### **🔍 Code Breakdown**
- `socket.SOCK_DGRAM`: Uses **UDP** for faster communication.
- `sendto()`: Sends a **timing test message** to the server.
- `recvfrom(1024)`: Receives the **timestamp from the server**.
- `end_time - start_time`: Computes **Round Trip Time (RTT)** in **milliseconds**.

---

# 🔒 **Security in Transport-Layer Protocols**

## 📌 Overview

A **transport-layer protocol** can enhance an application's **security** by offering services such as:

- 🔐 **Confidentiality** – Encrypting transmitted data to prevent unauthorized access.
- ✅ **Data Integrity** – Ensuring that the received data is not tampered with.
- 🆔 **End-Point Authentication** – Verifying the identity of communication parties.

These security measures protect data even if intercepted during transmission between the **sending** and **receiving** processes.

## 🔹 Security Services in Transport Protocols

### **1️⃣ Confidentiality (Encryption & Decryption)**

- Encryption at the **sending host** ensures that data remains unreadable to unauthorized entities.
- Decryption at the **receiving host** ensures that only intended recipients can access the original message.

### **2️⃣ Data Integrity**

- Ensures that data is not **modified** during transmission.
- Prevents **man-in-the-middle (MITM) attacks** from altering messages.

### **3️⃣ End-Point Authentication**

- Verifies that the sender and receiver are legitimate parties.
- Prevents **impersonation attacks** by requiring credentials.

## 📜 Code Example: Implementing Secure Transport with Python (TLS Encryption)

### **🔹 Secure Server Code (TLS-Enabled)**

```python
import socket
import ssl

# Create a standard socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8443))
server_socket.listen(1)

# Wrap the socket with SSL
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

print("🔒 Secure Server is running...")
conn, addr = server_socket.accept()
secure_conn = context.wrap_socket(conn, server_side=True)

# Receiving encrypted data
data = secure_conn.recv(1024).decode()
print(f"Received: {data}")

# Sending encrypted response
secure_conn.send("Secure connection established!".encode())
secure_conn.close()
```

### **🔍 Code Breakdown**

- `ssl.create_default_context()`: Creates a **TLS/SSL security context**.
- `context.load_cert_chain(certfile, keyfile)`: Loads the **server's certificate and key**.
- `wrap_socket(conn, server_side=True)`: Secures the connection with **TLS encryption**.
- `recv(1024)`: Receives **encrypted data** securely.
- `send()`: Sends **encrypted responses**.

### **🔹 Secure Client Code (TLS-Enabled)**

```python
import socket
import ssl

# Create a standard socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap socket with SSL for secure communication
context = ssl.create_default_context()
secure_socket = context.wrap_socket(client_socket, server_hostname='localhost')
secure_socket.connect(('localhost', 8443))

# Sending encrypted data
secure_socket.send("Hello Secure Server!".encode())

# Receiving encrypted response
response = secure_socket.recv(1024).decode()
print(f"Server Response: {response}")

secure_socket.close()
```

### **🔍 Code Breakdown**

- `wrap_socket(client_socket, server_hostname='localhost')`: Enables **TLS encryption** for the client.
- `connect(('localhost', 8443))`: Connects to the **secure server**.
- `send()`: Sends **encrypted** data to the server.
- `recv(1024)`: Receives the **server's secure response**.

