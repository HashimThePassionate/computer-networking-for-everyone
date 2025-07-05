# **Understanding UDP Connectionless** 🥳

**UDP (User Datagram Protocol)** is the simplest way for applications to send messages over the Internet. Think of it like sending postcards—each one goes off on its own, with no guarantee it arrives, but there’s almost no delay in sending.


## 1. What UDP Does 📬

1. **Adds Port Numbers**

   * Every message gets a **source port** (who sent it) and a **destination port** (who should receive it).
   * This lets your computer talk to many programs at once.

2. **Minimal Error Check**

   * UDP header has a tiny checksum to catch corrupted data, but it won’t try to fix errors.

3. **No Handshakes**

   * Unlike TCP, UDP **does not** say “Hello, ready to talk?” before sending.
   * It just **blasts** your message off immediately.


## 2. Why “Connectionless”? 🔌✂️

* **No setup or teardown**: There’s no “three-way handshake” like TCP.
* **Stateless**: Your computer doesn’t keep track of who it’s talking to.

*Result:* Very fast startup, but no built-in guarantee that messages arrive or arrive in order.

## 3. When to Use UDP vs. TCP 🤔

| Feature                    | UDP                                  | TCP                                       |
| -------------------------- | ------------------------------------ | ----------------------------------------- |
| **Speed / Delay**          | ✅ Very low delay                     | ❌ Slower (establishes connection)         |
| **Reliability**            | ❌ No automatic retransmission        | ✅ Retries lost packets, in-order delivery |
| **Overhead (Header Size)** | 🔹 8 bytes                           | 🔹 20 bytes + options                     |
| **Control**                | ✅ You decide any extra error control | ❌ TCP controls timing and rate            |

**Use UDP when:**

* You need the **fastest** possible delivery (e.g., live video, voice calls). 🎥📞
* You can tolerate **some lost packets** (a few missing frames won’t ruin a stream).
* You want to build your own custom retry or error-handling at the application level.

**Use TCP when:**

* Every byte matters (e.g., web pages, file downloads). 🌐📂
* You need guaranteed, in-order delivery and congestion control.


## 4. Real-World Examples 🌍

* **DNS Queries** 🧐

  * Quick “What is google.com?” lookups. If no reply, try again or ask another server.
* **Video Streaming & VoIP** 🎞️📱

  * Live video calls or online radio. Small glitches are OK; smooth flow is more important.
* **QUIC Protocol** 🚀

  * Google’s new transport for HTTP/3: runs over UDP but adds reliable delivery on top.


## 5. Pros & Cons of UDP 👍👎

### 👍 Advantages

* **Ultra-low startup delay**
* **Small header** = less overhead
* **Easier to handle many clients** (no per-connection state)

### 👎 Disadvantages

* **No built-in reliability**
* **No congestion control** (can overload networks if not careful)
* **Application must handle errors/retries** if needed

---

**A list of common Internet applications** and **which transport protocol** they typically use:

| **Application**            | **App-Layer Protocol** | **Transport Protocol** | **Why? (in simple terms)**                                                |
| -------------------------- | ---------------------- | ---------------------- | ------------------------------------------------------------------------- |
| **Electronic mail**        | SMTP                   | TCP                    | Mail must arrive intact and in order, so we use TCP’s reliability.        |
| **Remote terminal access** | Telnet                 | TCP                    | Interactive sessions (typing commands) need reliable delivery.            |
| **Secure remote access**   | SSH                    | TCP                    | Same as Telnet but encrypted—still needs all data reliably.               |
| **Web (HTTP/1-2)**         | HTTP                   | TCP                    | Web pages (text, images) must download fully and in order.                |
| **Web (HTTP/3)**           | HTTP/3                 | UDP                    | Newer HTTP runs over UDP (via QUIC) for faster connection setup.          |
| **File transfer**          | FTP                    | TCP                    | Whole files must arrive without missing bytes—use TCP.                    |
| **Remote file server**     | NFS                    | Typically UDP          | NFS can afford occasional retries and wants low overhead.                 |
| **Streaming multimedia**   | DASH                   | TCP                    | DASH is adaptive-bitrate streaming over HTTP/TCP (to simplify firewalls). |
| **Internet telephony**     | (proprietary)          | UDP or TCP             | Voice apps often choose UDP for low delay, but may fall back to TCP.      |
| **Network management**     | SNMP                   | Typically UDP          | Management queries need to work even under heavy network stress.          |
| **Name translation (DNS)** | DNS                    | Typically UDP          | Quick lookups—avoids TCP’s connection delay and overhead.                 |

---

### A bit more on **why TCP vs. UDP**:

* **TCP** = **Reliable & Ordered**

  * Guarantees every byte arrives and in the right order.
  * Good for email, file transfer, web pages—where you can’t tolerate missing data.

* **UDP** = **Fast & Lean**

  * No handshakes, minimal headers, no built-in retries.
  * Great for quick queries (DNS), real-time media (voice/video), and cases where your app will handle any lost packets.

---