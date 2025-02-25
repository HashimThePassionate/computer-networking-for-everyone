# &#x20;**Transport Services Provided by the Internet 📌**

## 🌍nn Overview

The Intern&#x20;

et provides two primary transport protocols for applications:

- **TCP (Transmission Control Protocol)**
- **UDP (User Datagram Protocol)**

When developing a network application, one of the first decisions is choosing between **TCP and UDP** based on the application's requirements.

---

## 📊 Transport Service Requirements for Selected Applications

### 📌 Understanding Application Requirements

Different applications have different transport service requirements. These requirements help in deciding whether to use **TCP** or **UDP** based on factors like **data loss tolerance, throughput demands, and time sensitivity**.

### 📊 Comparison Table

| **Application**                       | **Data Loss** | **Throughput**                              | **Time-Sensitive** |
| ------------------------------------- | ------------- | ------------------------------------------- | ------------------ |
| File transfer/download                | No loss       | Elastic                                     | No                 |
| E-mail                                | No loss       | Elastic                                     | No                 |
| Web documents                         | No loss       | Elastic (few kbps)                          | No                 |
| Internet telephony/Video conferencing | Loss-tolerant | Audio: few kbps–1 MbpsVideo: 10 kbps–5 Mbps | Yes: 100s of msec  |
| Streaming stored audio/video          | Loss-tolerant | Same as above                               | Yes: few seconds   |
| Interactive games                     | Loss-tolerant | Few kbps–10 kbps                            | Yes: 100s of msec  |
| Smartphone messaging                  | No loss       | Elastic                                     | Yes and no         |

### 📌 Explanation of Key Factors

- **Data Loss Tolerance:**

  - Some applications like **file transfer and email** require **zero data loss**, so they must use **TCP**.
  - Other applications like **internet telephony, video conferencing, and games** can tolerate some data loss since real-time interaction is more critical than perfect accuracy.

- **Throughput Requirements:**

  - Applications like **file transfer and web documents** require **elastic throughput**, meaning they can adapt to the available bandwidth.
  - **Audio/video streaming and gaming** have specific bandwidth needs to function properly without disruption.

- **Time Sensitivity:**

  - **Real-time applications** like **video conferencing, gaming, and telephony** require low latency, meaning they need fast, uninterrupted communication.
  - **File transfer and email** are **not time-sensitive**, as delays do not impact their usability.

This table helps developers determine whether **TCP or UDP** is the better choice based on the application's needs.

---

## 🔹 **TCP Services**

TCP provides two key services:

### 🔗 **1. Connection-Oriented Service**

- TCP establishes a **handshaking procedure** before data transmission.
- A full-duplex connection is created, allowing both processes to send messages simultaneously.
- When communication is completed, the connection is **properly closed**.

### ✅ **2. Reliable Data Transfer Service**

- Ensures **error-free** and **ordered** delivery of data.
- Prevents **packet loss** and **duplicates**.
- Includes a **congestion-control mechanism** to prevent overwhelming the network.

---

## ⚡ **UDP Services**

UDP is a **lightweight, connectionless** transport protocol with minimal features.

- **No handshaking** – data is sent immediately.
- **Unreliable transmission** – messages may be lost or arrive out of order.
- **No congestion control** – data can be sent at any rate, risking network overload.

---

## 🔐 **Securing TCP with TLS (Transport Layer Security)**

**Key Points:**

- **Neither TCP nor UDP provides encryption by default.**
- Sending **unencrypted passwords** or sensitive data over TCP/UDP **can be intercepted**.
- **TLS (Transport Layer Security)** is an enhancement to TCP providing:
  - **Encryption** 🔐
  - **Data Integrity** ✅
  - **End-Point Authentication** 🔑
- **TLS Process:**
  1. The sending process passes cleartext data to a **TLS socket**.
  2. **TLS encrypts the data** and passes it to a **TCP socket**.
  3. Data is transmitted securely over the Internet.
  4. The receiving **TCP socket** forwards encrypted data to **TLS**.
  5. **TLS decrypts the data** and passes it to the application.

🚀 TLS is widely used in **HTTPS, email encryption, and secure communications**.

---

## 🎯 **Conclusion**

The choice between TCP and UDP depends on the application’s needs:

- Use **TCP** for reliable, ordered, and congestion-controlled communication.
- Use **UDP** for low-latency, loss-tolerant, and high-speed communication.
- Use **TLS with TCP** when encryption and security are required.

Understanding these transport services is essential for **network developers** to make informed decisions when designing applications. 🌍🚀

