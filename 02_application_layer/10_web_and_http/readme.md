# 🌍 **The Web and HTTP**

## 📌 Overview
Before the **1990s**, the Internet was primarily used by researchers, academics, and university students for:
- Logging into remote hosts
- Transferring files
- Sending and receiving news
- Exchanging electronic mail

Despite its usefulness, the Internet remained largely unknown outside academic and research communities. However, **the early 1990s** saw the emergence of a revolutionary application—the **World Wide Web (WWW)**.

---

## 🌐 **The Arrival of the Web**
The **World Wide Web (WWW)**, introduced by **Tim Berners-Lee in 1994**, transformed the Internet into a mainstream technology. It elevated the Internet from being just another **data network** to becoming **the primary global information network**.

### 🔹 Key Reasons for the Web’s Popularity:
- **On-Demand Access** 📡: Unlike traditional radio and television broadcasts that dictate when content is available, the Web allows users to access information **whenever they want**.
- **Easy Information Publishing** 📝: Anyone can become a content creator at a **very low cost**.
- **Hyperlinks & Search Engines** 🔗: Enable users to efficiently navigate through vast amounts of information.
- **Multimedia Integration** 🎥: The Web supports **images, videos, and interactive elements** that enhance user engagement.
- **Interactivity & Customization** 🎮: Technologies like **JavaScript, Forms, and APIs** enable interactive experiences.

---

## 🌍 **How the Web Works**
The Web operates through a client-server model, where web browsers (clients) communicate with web servers using **HTTP (HyperText Transfer Protocol)**.

### 🔹 **Key Web Technologies:**
| **Technology**  | **Purpose**  |
|-----------------|-------------|
| **HTTP** ([RFC 7230](https://tools.ietf.org/html/rfc7230)) | Defines how web browsers and servers communicate 📡 |
| **HTML** | Structure of web pages 🏗️ |
| **CSS** | Styling and design 🎨 |
| **JavaScript** | Interactive elements 🎮 |
| **Search Engines** | Helps users find relevant content 🔍 |
| **APIs (REST, GraphQL, etc.)** | Enables dynamic content exchange 🔄 |

---

## 🎥 **The Web as a Platform**
The Web is not just about static pages; it serves as the foundation for numerous modern applications:

### 🌍 **Web-Based Services**
- **YouTube** 🎬 – Video streaming
- **Gmail, Outlook** 📧 – Web-based email
- **Google Maps** 🗺️ – Location and navigation services
- **Instagram, Facebook, Twitter** 📲 – Social media platforms
- **E-commerce** 🛒 – Online shopping and transactions

### 🔹 **Mobile & Cloud Integration**
- Many mobile applications rely on Web technologies for **real-time data synchronization**.
- Cloud computing services use the Web for remote storage, document collaboration, and seamless communication.

---

# 📌 Overview of HTTP

## 🌍 Introduction
**HyperText Transfer Protocol (HTTP)** is the foundation of data communication on the World Wide Web. It is an **application-layer protocol** that defines how messages are formatted and transmitted between clients and servers. HTTP is standardized in:
- 📜 [RFC 1945] (HTTP/1.0)
- 📜 [RFC 7230] (HTTP/1.1)
- 📜 [RFC 7540] (HTTP/2)

## ⚙️ How HTTP Works
HTTP is based on a **client-server model**, meaning:
1. **Client Program** – Initiates requests (e.g., web browsers like Chrome, Firefox, and Edge).
2. **Server Program** – Handles requests and sends back responses (e.g., Apache, Nginx, IIS).

These two communicate via **HTTP messages** that define the structure and exchange process.

## 🌐 Web Terminology
A **Web page** consists of multiple **objects**. An **object** is any file such as:
- 📄 HTML documents
- 🖼️ Images (JPEG, PNG, GIF)
- 📝 CSS stylesheets
- 📜 JavaScript files
- 🎥 Video clips

A **URL (Uniform Resource Locator)** identifies web objects. Every URL has:
- **Hostname** – Identifies the web server (e.g., `www.someSchool.edu`)
- **Path Name** – Specifies object location (e.g., `/someDepartment/picture.gif`)

For example:
```
http://www.someSchool.edu/someDepartment/picture.gif
```
Here:
- `www.someSchool.edu` → **Hostname**
- `/someDepartment/picture.gif` → **Path Name**

## 🔄 HTTP Request-Response Model
HTTP governs how clients request pages and servers respond. This interaction follows:
1. **Client requests a Web Page** (e.g., clicking a hyperlink).
2. **Browser sends HTTP request messages**.
3. **Server receives requests and responds** with HTTP response messages.
4. **Response contains requested objects** (e.g., HTML, images, scripts).

### 📌 Example of HTTP Communication
When a user requests a webpage containing **one HTML file** and **five images**, the process involves **six HTTP requests**:
- **One request** for the base HTML file
- **Five requests** for the images

<div align="center">
  <img src="./images/01.jpg" alt="" width="600px"/>

  **Figure 2.6**: HTTP request-response behavior

</div>

Each request and response follows the HTTP protocol.

## ⚡ Underlying Transport Protocol
HTTP operates over **TCP (Transmission Control Protocol)**, not UDP. The steps include:
1. **TCP connection establishment** between client and server.
2. **Data exchange** via TCP sockets.
3. **Reliable message delivery** ensured by TCP.
4. **Connection termination** after message exchange.

## 🚀 Advantages of Layered Architecture
HTTP does not manage network reliability directly. Instead, it relies on **lower-layer protocols** (such as TCP) to:
- Handle **packet loss**
- Ensure **data integrity**
- Manage **packet reordering**

## 🛑 Stateless Nature of HTTP
- HTTP is a **stateless protocol**.
- The server does **not remember** past client requests.
- If a client requests the same file multiple times, the server **reprocesses it** each time.
- There is no session storage unless additional mechanisms like **cookies or sessions** are used.

## 🏛️ Client-Server Architecture
- A **web server** remains active with a **fixed IP address**.
- It handles requests from **millions of browsers** worldwide.

## 🔄 Evolution of HTTP Versions
- **HTTP/1.0 (1990s)** – The original version defined in **RFC 1945**.
- **HTTP/1.1 (Current Majority Use)** – Standardized in **RFC 7230**, supporting:
  - Persistent connections
  - Chunked transfers
- **HTTP/2 (Emerging Standard)** – Defined in **RFC 7540**, providing:
  - Multiplexing
  - Header compression
  - Improved performance


# 🔄 Non-Persistent and Persistent Connections

## 🌐 Introduction
In many **Internet applications**, clients and servers engage in communication for an extended period, exchanging multiple requests and responses. These requests can be:
- 📌 **Back-to-back** – Continuous, without delays.
- 📌 **Periodic** – Sent at regular time intervals.
- 📌 **Intermittent** – Occasional, based on demand.

When this interaction happens over **TCP (Transmission Control Protocol)**, developers must choose how to manage connections:
1. **Non-Persistent Connections** – Each request/response pair uses a **separate TCP connection**.
2. **Persistent Connections** – All requests and responses share a **single TCP connection**.

HTTP supports both models, though **persistent connections** are the default. However, **clients and servers can be configured** to use non-persistent connections if needed.

---

