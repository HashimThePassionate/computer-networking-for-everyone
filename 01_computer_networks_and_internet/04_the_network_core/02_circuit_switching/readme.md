# 🌐 **Circuit Switching**

## 🖥️ **Introduction**
**Circuit switching** is one of the two fundamental methods used to transmit data through a network of links and switches, the other being **packet switching**. In circuit-switched networks, resources such as **link bandwidth** and **buffers** are **reserved** for the entire duration of a communication session. This approach provides a dedicated connection between the sender and receiver, guaranteeing a constant transmission rate.

---

## 📌 **What Is Circuit Switching?**

### 🌟 **Definition**:
**Circuit switching** establishes a dedicated communication path between two endpoints for the entire session. The resources along this path are reserved and cannot be used by other connections until the session ends.

---

## 🧩 **Key Features of Circuit Switching**

1. **Resource Reservation**:  
   - Buffers and link bandwidth are reserved for the duration of the communication session.

2. **Guaranteed Performance**:  
   - Since resources are pre-allocated, the sender can transmit data at a **constant, guaranteed rate**.

3. **Connection Setup**:  
   - A **connection (circuit)** must be established before data transmission begins.

4. **Dedicated Path**:  
   - The path between the sender and receiver remains exclusively dedicated for the session.

---

## 🖼️ **Illustration: Circuit-Switched Network**

Refer to **Figure 1.13**:
- Four circuit switches are interconnected with four links.
- Each link has **four circuits**, meaning it can support up to four simultaneous connections.
- When **Host A** communicates with **Host B**, a **dedicated circuit** is reserved across two links:
  - The second circuit on the first link.
  - The fourth circuit on the second link.
- Each circuit receives a **dedicated fraction of the link’s capacity**.

<div align="center">
  <img src="../images/02_circuit_switching.jpg" alt="Circuit Switching" width="500px"/>
</div>

## 📊 **How Circuit Switching Works**

1. **Connection Establishment**:
   - Before communication begins, a **dedicated path (circuit)** is set up between the sender and receiver.
   - Each link along the path reserves a portion of its transmission capacity.

2. **Data Transmission**:
   - Data is transmitted at a constant rate along the reserved circuit.
   - The transmission is unaffected by other traffic in the network.

3. **Connection Teardown**:
   - Once the session ends, the reserved resources are released for other connections.

---

## 🧮 **Example: Circuit Allocation**

### Scenario:
- A link has a total transmission rate of **1 Mbps**.
- The link is divided into **4 circuits**.

**Result**:
- Each circuit is allocated \( \frac{1 \, \text{Mbps}}{4} = 250 \, \text{kbps} \).
- If Host A and Host B communicate, they receive **250 kbps** of dedicated bandwidth.

---

## 🔄 **Circuit Switching vs. Packet Switching**

| **Feature**                | **Circuit Switching**                          | **Packet Switching**                          |
|----------------------------|-----------------------------------------------|----------------------------------------------|
| **Resource Allocation**     | Resources are **reserved** for the session.   | Resources are **not reserved**.              |
| **Data Transmission Rate**  | Constant and guaranteed.                     | Variable and not guaranteed.                 |
| **Setup Time**              | Requires a **setup phase** before transmission.| No setup phase required.                     |
| **Congestion Handling**     | No queuing or congestion during the session.  | Packets may queue and face delays during congestion. |
| **Use Case**                | Ideal for voice calls (e.g., traditional telephony).| Ideal for data transfer (e.g., Internet traffic). |

---

## 🧩 **Advantages of Circuit Switching**

1. **Guaranteed Bandwidth**:
   - Ensures consistent performance for real-time applications like voice and video calls.

2. **No Congestion During Communication**:
   - Once the circuit is established, no additional delays or packet loss occur.

3. **Predictable Latency**:
   - Since resources are reserved, communication occurs with minimal latency.

---

## ⚠️ **Disadvantages of Circuit Switching**

1. **Inefficient Resource Usage**:
   - Resources are reserved even if no data is being transmitted, leading to potential waste.

2. **Setup Time**:
   - Establishing a connection requires additional time before data transmission can begin.

3. **Scalability Issues**:
   - Cannot efficiently handle large-scale data traffic, making it less suitable for the modern Internet.

---

## 🌟 **Real-Life Example: Traditional Telephony**

In a traditional telephone network:
- A **circuit** is established before a call begins.
- The circuit reserves a dedicated bandwidth for the entire call duration.
- Once the call ends, the circuit is released.

---

> New Section Begins

