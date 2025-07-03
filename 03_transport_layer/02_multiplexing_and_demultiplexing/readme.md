#  **Multiplexing & Demultiplexing** 🚚

When your computer runs multiple network applications at the same time (for example, two Telnet sessions, one FTP session, and one web-browser download), the **transport layer** must sort and deliver data to the correct program. This involves two complementary tasks:

1. **Multiplexing** 🔀

   * **At the sender**, the transport layer **gathers** data from different application sockets, adds transport-header information (port numbers), and passes the resulting segments down to the network layer.

2. **Demultiplexing** 🔄

   * **At the receiver**, the transport layer **examines** the incoming segment’s header, finds the matching socket, and delivers the payload to the correct application process.

<div align="center">
  <img src="./images/01.jpg" alt="" width="600px"/>
</div>

## 📺 Figure 3.2: How Demultiplexing Works

> **Visual Summary:** Three hosts on a network, each running multiple processes (P₁, P₂, P₃, P₄).
> Blue arrows show segments traveling through the network to the transport layer, then up into the correct socket and process.

* Each **process** (e.g., your FTP client or web browser) communicates via a **socket** (a virtual “door”).
* Sockets are uniquely identified so incoming data is routed correctly.
* The transport layer in the middle host must both:

  1. **Demultiplex** incoming segments to P₁ or P₂, and
  2. **Multiplex** outgoing data from P₁/P₂ back into segments.


## 🔢 Figure 3.3: Transport Segment Header Fields

<div align="center">
  <img src="./images/02.jpg" alt="" width="600px"/>
</div>

</br>

```
|  Source Port #  |  Destination Port #  |  Other Header Fields  |  Application Data ...  |
        16 bits              16 bits
```

1. **Source Port Number**

   * Identifies the sender’s socket (so replies can be routed back).

2. **Destination Port Number**

   * Identifies the receiver’s socket (so data goes to the right process).

3. **Port Number Range**

   | Range         | Meaning                                    |
   | ------------- | ------------------------------------------ |
   | 0 – 1023      | **Well-known ports** (reserved by IANA)    |
   | 1024 – 49151  | **Registered ports** (user or application) |
   | 49152 – 65535 | **Dynamic/private ports** (ephemeral use)  |

> ✨ Common examples:
>
> * **HTTP** uses port **80**
> * **FTP** uses port **21**

---

## 🏠 Mail-Room Analogy

* **Household** = your computer
* **Mail carrier** = the network layer delivering packets
* **Letters addressed to each kid** = transport segments with port numbers
* **Bill sorting mail by name** = **demultiplexing** (reading “To:” and handing letters to the right child)
* **Ann collecting outgoing mail** = **multiplexing** (gathering letters from all kids and giving to the mail carrier)

---

## 📋 Why This Matters

* Without multiplexing/demultiplexing, your computer couldn't handle more than one application at a time!
* Port numbers let many applications share the same network interface seamlessly.
* Both **UDP** and **TCP** use this scheme—TCP adds extra fields for reliability, while UDP keeps things lightweight.

