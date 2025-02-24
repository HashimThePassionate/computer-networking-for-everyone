# 📡 **Addressing Processes**

For successful communication between network applications, **each process must be uniquely identifiable**. Similar to how postal mail requires an address, a networked process must have a **destination address** to send and receive data correctly. 📩🏠

## 🏛 Identifying a Process in a Network

To correctly route data between processes, two key pieces of information are required:

1. **The host’s address** (where the process is running). 🌍
2. **A unique process identifier** (specifying the exact process in the destination host). 🔢

### 🔹 Host Identification: IP Address

- A **host** in the Internet is uniquely identified by an **IP address**.
- An **IP address** is a **32-bit** number (IPv4) or **128-bit** number (IPv6) assigned to a networked device.
- We will explore **IP addressing in detail** in later sections.

### 🔹 Process Identification: Port Numbers

Since a **host** may run multiple network applications simultaneously, we need a way to **distinguish between different processes** within the same host. This is done using **port numbers**. 🔢

✅ **A destination port number uniquely identifies a process within a host.**
✅ **Each Internet service has a standard port number:**

- **Web server (HTTP):** Port **80** 🌐
- **Mail server (SMTP):** Port **25** 📧

A full list of well-known **port numbers** for Internet standard protocols is available at **[www.iana.org](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)**. 📜
