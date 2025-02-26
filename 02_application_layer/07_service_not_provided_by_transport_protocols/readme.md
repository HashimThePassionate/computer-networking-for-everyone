# **Services Not Provided by Internet Transport Protocols** 🚀 

## 📌 Overview

Internet transport protocols, such as **TCP** and **UDP**, provide essential communication services. However, they do **not** offer guarantees in certain key areas, particularly **throughput and timing**. Despite this, many time-sensitive applications still function effectively over the Internet by adapting their design to compensate for these limitations.

---

## 🔍 Dimensions of Transport Protocol Services

Transport protocols can be categorized based on the following four dimensions:

1. **Reliable Data Transfer** ✅
2. **Throughput** ❌ (Not Guaranteed)
3. **Timing** ❌ (Not Guaranteed)
4. **Security** 🔐 (Available with TLS over TCP)

---

## 📌 Key Observations

- **TCP provides** **reliable end-to-end data transfer** but does not guarantee **timing or throughput**.
- **TLS (Transport Layer Security)** can be applied at the application layer to provide encryption and security services over TCP.
- **UDP provides** an **unreliable, lightweight** service with no built-in guarantees for data delivery, ordering, timing, or security.
- **Time-sensitive applications** (such as **Internet telephony**) still operate effectively on the Internet but must adapt to its limitations.
- **Excessive delay or low throughput** can hinder the performance of time-sensitive applications despite adaptive design strategies.

---

## 📊 Transport Protocols Used by Popular Internet Applications

| **Application**            | **Application-Layer Protocol**                                                                                                             | **Underlying Transport Protocol** |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------- |
| **Electronic Mail**        | SMTP ([RFC 5321](https://tools.ietf.org/html/rfc5321))                                                                                     | TCP                               |
| **Remote Terminal Access** | Telnet ([RFC 854](https://tools.ietf.org/html/rfc854))                                                                                     | TCP                               |
| **Web**                    | HTTP 1.1 ([RFC 7230](https://tools.ietf.org/html/rfc7230))                                                                                 | TCP                               |
| **File Transfer**          | FTP ([RFC 959](https://tools.ietf.org/html/rfc959))                                                                                        | TCP                               |
| **Streaming Multimedia**   | HTTP (e.g., YouTube), DASH                                                                                                                 | TCP                               |
| **Internet Telephony**     | SIP ([RFC 3261](https://tools.ietf.org/html/rfc3261)), RTP ([RFC 3550](https://tools.ietf.org/html/rfc3550)), or proprietary (e.g., Skype) | UDP or TCP                        |

---

## 🎯 Choosing Between TCP and UDP

- **Reliable Applications**: E-mail, remote terminal access, web browsing, and file transfers require **TCP** for reliable, ordered data transfer.
- **Time-Sensitive Applications**: Internet telephony and streaming multimedia prefer **UDP** for low latency but may use **TCP** if UDP is blocked by firewalls.
- **Adaptive Design**: Many applications use **UDP for speed** but fall back to **TCP** for reliability when necessary.

---

## 🔐 Security Considerations

- Neither TCP nor UDP provides built-in **encryption** or **data protection**.
- **TLS (Transport Layer Security)** is an enhancement applied at the application layer to **TCP-based** communications, ensuring:
  - **Encryption** 🔐
  - **Data Integrity** ✅
  - **End-Point Authentication** 🔑

---

## ✅ Conclusion

- **The Internet does not guarantee throughput or timing**, but applications are designed to handle these limitations.
- **TCP is ideal for applications requiring reliability**, while **UDP is used for low-latency, time-sensitive communication**.
- **Security is a separate concern**, addressed at the application layer using **TLS over TCP**.
- **Developers must choose** between **TCP and UDP** based on their application's needs, considering factors like **latency, reliability, and firewall constraints**.



