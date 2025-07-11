# **Understanding UDP Connectionless** 🥳

## 📑 **Table of Contents**

- [**Understanding UDP Connectionless** 🥳](#understanding-udp-connectionless-)
  - [📑 **Table of Contents**](#-table-of-contents)
  - [1. What UDP Does 📬](#1-what-udp-does-)
  - [2. Why “Connectionless”? 🔌✂️](#2-why-connectionless-️)
  - [3. When to Use UDP vs. TCP 🤔](#3-when-to-use-udp-vs-tcp-)
  - [4. Real-World Examples 🌍](#4-real-world-examples-)
  - [5. Pros \& Cons of UDP 👍👎](#5-pros--cons-of-udp-)
    - [👍 Advantages](#-advantages)
    - [👎 Disadvantages](#-disadvantages)
    - [A bit more on **why TCP vs. UDP**:](#a-bit-more-on-why-tcp-vs-udp)
- [**UDP Segment Structure** 🚀](#udp-segment-structure-)
  - [1. UDP Segment Layout 🗂️](#1-udp-segment-layout-️)
  - [2. The **Length** Field 📏](#2-the-length-field-)
  - [3. The **Checksum** Field ✅❌](#3-the-checksum-field-)
    - [3.1 Purpose](#31-purpose)
    - [3.2 How It’s Computed](#32-how-its-computed)
    - [3.3 Step-by-Step Example](#33-step-by-step-example)
      - [a) Sum Word 1 + Word 2](#a-sum-word-1--word-2)
      - [b) Add Word 3](#b-add-word-3)
      - [c) Compute 1’s-Complement](#c-compute-1s-complement)
  - [4. What Happens on Error? 🛑](#4-what-happens-on-error-)
- [**Principles of Reliable Data Transfer** 🔒](#principles-of-reliable-data-transfer-)
  - [🖼️ Fig. 3.8(a): **Service Model** (What the upper layer **expects**)](#️-fig-38a-service-model-what-the-upper-layer-expects)
  - [🔧 Fig. 3.8(b): **Service Implementation** (How RDT is actually built)](#-fig-38b-service-implementation-how-rdt-is-actually-built)
  - [🎯 Key Building Blocks](#-key-building-blocks)
  - [💡 Analogy: **Reliable Courier Service**](#-analogy-reliable-courier-service)
- [**rdt1.0: Reliable Data Transfer over a **Perfectly Reliable** Channel** 📦](#rdt10-reliable-data-transfer-over-a-perfectly-reliable-channel-)
  - [🏗️ Sender-Side FSM (Figure 3.9a)](#️-sender-side-fsm-figure-39a)
  - [🏗️ Receiver-Side FSM (Figure 3.9b)](#️-receiver-side-fsm-figure-39b)
  - [🎯 Why rdt1.0 Is So Simple](#-why-rdt10-is-so-simple)
- [**rdt2.0: Handling **Bit Errors** with Stop-and-Wait ARQ** 🛠️](#rdt20-handling-bit-errors-with-stop-and-wait-arq-️)
  - [📊 Sender FSM (Figure 3.10a)](#-sender-fsm-figure-310a)
  - [📊 Receiver FSM (Figure 3.10b)](#-receiver-fsm-figure-310b)
  - [🔍 How it Works](#-how-it-works)
  - [⚠️ The Big Flaw](#️-the-big-flaw)
- [**rdt2.1: Stop-and-Wait with Sequence Numbers (Fixing Corrupted ACKs/NAKs)** 🔁](#rdt21-stop-and-wait-with-sequence-numbers-fixing-corrupted-acksnaks-)
  - [📶 Sender FSM (Figure 3.11)](#-sender-fsm-figure-311)
    - [🔑 Key Points](#-key-points)
  - [📩 Receiver FSM (Figure 3.12)](#-receiver-fsm-figure-312)
  - [🎉 Why rdt2.1 Works](#-why-rdt21-works)
- [**rdt3.0: Handling **Lossy** Channels with Bit Errors** ⏲️](#rdt30-handling-lossy-channels-with-bit-errors-️)
  - [📦 Figure 3.14: Sender FSM for rdt3.0](#-figure-314-sender-fsm-for-rdt30)
    - [🛠️ Key Sender Actions](#️-key-sender-actions)
  - [⏳ Figure 3.15: Timeline Illustrations](#-figure-315-timeline-illustrations)
    - [a) No Loss, No Errors](#a-no-loss-no-errors)
    - [b) Data Packet Lost](#b-data-packet-lost)
    - [c) ACK Packet Lost](#c-ack-packet-lost)
  - [🎉 Why rdt3.0 Works](#-why-rdt30-works)
- [**Pipelined Reliable Data Transfer Protocols** 📡](#pipelined-reliable-data-transfer-protocols-)
  - [🚀 Pipelined Reliable Data Transfer Protocols (Concise)](#-pipelined-reliable-data-transfer-protocols-concise)
    - [🔑 Key Ideas](#-key-ideas)
    - [🔄 Two Main ARQ Schemes](#-two-main-arq-schemes)
    - [📈 Why Pipelining Helps](#-why-pipelining-helps)
  - [📊 Figure 3.16: Operation of rdt3.0 (Alternating-Bit Protocol)](#-figure-316-operation-of-rdt30-alternating-bit-protocol)
  - [🌉 Figure 3.17: Stop-and-Wait vs Pipelined Protocol](#-figure-317-stop-and-wait-vs-pipelined-protocol)
  - [⏱️ Figure 3.18: Timing Diagrams](#️-figure-318-timing-diagrams)
  - [🔑 Why Pipelining Helps](#-why-pipelining-helps-1)

---

**UDP (User Datagram Protocol)** is the simplest way for applications to send messages over the Internet. Think of it like sending postcards—each one goes off on its own, with no guarantee it arrives, but there's almost no delay in sending.


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
| **Electronic mail**        | SMTP                   | TCP                    | Mail must arrive intact and in order, so we use TCP's reliability.        |
| **Remote terminal access** | Telnet                 | TCP                    | Interactive sessions (typing commands) need reliable delivery.            |
| **Secure remote access**   | SSH                    | TCP                    | Same as Telnet but encrypted—still needs all data reliably.               |
| **Web (HTTP/1-2)**         | HTTP                   | TCP                    | Web pages (text, images) must download fully and in order.                |
| **Web (HTTP/3)**           | HTTP/3                 | UDP                    | Newer HTTP runs over UDP (via QUIC) for faster connection setup.          |
| **File transfer**          | FTP                    | TCP                    | Whole files must arrive without missing bytes—use TCP.                    |
| **Remote file server**     | NFS                    | Typically UDP          | NFS can afford occasional retries and wants low overhead.                 |
| **Streaming multimedia**   | DASH                   | TCP                    | DASH is adaptive-bitrate streaming over HTTP/TCP (to simplify firewalls). |
| **Internet telephony**     | (proprietary)          | UDP or TCP             | Voice apps often choose UDP for low delay, but may fall back to TCP.      |
| **Network management**     | SNMP                   | Typically UDP          | Management queries need to work even under heavy network stress.          |
| **Name translation (DNS)** | DNS                    | Typically UDP          | Quick lookups—avoids TCP's connection delay and overhead.                 |

---

### A bit more on **why TCP vs. UDP**:

* **TCP** = **Reliable & Ordered**

  * Guarantees every byte arrives and in the right order.
  * Good for email, file transfer, web pages—where you can’t tolerate missing data.

* **UDP** = **Fast & Lean**

  * No handshakes, minimal headers, no built-in retries.
  * Great for quick queries (DNS), real-time media (voice/video), and cases where your app will handle any lost packets.

---

# **UDP Segment Structure** 🚀

UDP’s simplicity comes from having a **tiny header** (just 8 bytes) and treating the rest as “payload” (your application data). Let’s break down every field, see how the **length** works, and walk through the **checksum** calculation with a clear example.

## 1. UDP Segment Layout 🗂️

```
  0        16       32 bits
  ┌────────────┬────────────┬────────────┬────────────┐
  │ Source Port│Dest. Port  │ Length     │ Checksum   │  ← 8 bytes = 4 fields × 2 bytes
  ├────────────┼────────────┼────────────┼────────────┤
  │                Application Data (payload)         │
  │                           …                        │
  └────────────────────────────────────────────────────┘
```

| Field           | Size (bytes) | Description                                                                                 |
| --------------- | ------------ | ------------------------------------------------------------------------------------------- |
| **Source Port** | 2            | Port number of the sender’s application process                                             |
| **Dest. Port**  | 2            | Port number of the receiver’s application process (used for demultiplexing)                 |
| **Length**      | 2            | Total size of UDP segment (header **+** data), in bytes                                     |
| **Checksum**    | 2            | 1’s-complement checksum over header, data, and parts of IP header → for **error detection** |

## 2. The **Length** Field 📏

* **Why**: Because UDP doesn’t pad to a fixed size, the receiver needs to know where the user data ends.

* **Value**:

  > `Length = 8 (bytes of header) + N (bytes of application data)`

* **Example**:
  If your application sends 100 bytes,
  `Length = 8 + 100 = 108` → this 108 is put in the Length field.

## 3. The **Checksum** Field ✅❌

### 3.1 Purpose

* Catches **bit errors** that may happen:

  * Over an unreliable link
  * In router memory
  * On any path where link-layer checks aren’t guaranteed

* Follows the **end-to-end principle**: even if lower layers check errors, UDP must still verify the data once it arrives.

### 3.2 How It’s Computed

1. **Form 16-bit words**:

   * Treat the entire UDP segment (header + data) as a sequence of 16-bit (2-byte) words.
   * If the data has an odd number of bytes, pad with one zero byte at the end.

2. **Sum the words** using a **1’s-complement addition**:

   * Add all 16-bit words.
   * **If there’s overflow** beyond 16 bits, “wrap around” (i.e., add the overflow back into the low-order bits).

3. **Take the 1’s-complement** of that sum:

   * Invert every bit (0→1, 1→0).
   * Store this 16-bit result in the Checksum field.

4. **At the receiver**:

   * Sum *all* 16-bit words **including** the checksum.
   * A correct segment yields a sum of all-ones: `0xFFFF` (i.e., no detected errors).

### 3.3 Step-by-Step Example

Suppose our UDP segment (header+data) yields **three 16-bit words**:

```
 Word 1: 0110 0110 0110 0000   (0x6660)
 Word 2: 0101 0101 0101 0101   (0x5555)
 Word 3: 1000 1111 0000 1100   (0x8F0C)
```

#### a) Sum Word 1 + Word 2

```
  0110 0110 0110 0000  (Word 1)
+ 0101 0101 0101 0101  (Word 2)
──────────────────────
  1011 1011 1011 0101  (Intermediate Sum)
```

#### b) Add Word 3

```
  1011 1011 1011 0101  (Intermediate)
+ 1000 1111 0000 1100  (Word 3)
──────────────────────
1 0100 1010 1100 0010  (Raw 17-bit result)
```

* **Overflow bit** (the leftmost `1`) “wraps around”—add it back into the low 16 bits:

```
  Low 16 bits:     0100 1010 1100 0010 
+ Overflow (0x0001) 0000 0000 0000 0001
─────────────────────────────────────────
  Final Sum:       0100 1010 1100 0011
```

#### c) Compute 1’s-Complement

Invert every bit of `0100 1010 1100 0011`:

```
  0100 1010 1100 0011  (Sum)
→ 1011 0101 0011 1100  (Checksum)
```

So the **Checksum field** = `0xB53C`.

## 4. What Happens on Error? 🛑

* **Receiver sums** all words (including checksum).
* If the result ≠ `0xFFFF`, **an error is detected**.

  * Some UDP stacks **discard** the bad segment silently.
  * Others **deliver** it to the application but set an error flag.

---

#  **Principles of Reliable Data Transfer** 🔒

When two programs (sender and receiver) communicate over an **unreliable channel** (where packets can be lost or corrupted), we need a **reliable data transfer (RDT) protocol** to make sure:

1. ✅ **No bits are corrupted**
2. 📦 **No packets are lost**
3. 🔢 **Packets arrive in order**

This is exactly what **TCP** does for your web browser, but the same ideas apply at the link layer, application layer, and elsewhere!

<div align="center">
  <img src="./images/02.jpg" alt="" width="600px"/>
</div>

## 🖼️ Fig. 3.8(a): **Service Model** (What the upper layer **expects**)

```text
Application
   │   rdt_send(data)
   ▼
Transport layer (RDT)
   │   deliver_data(data)
   ▼
Network (reliable!)
```

* **Provided service**: a **reliable channel**

  * You call `rdt_send()` to send data.
  * You receive data via `deliver_data()`—with **no errors**, **no losses**, and **in correct order**.
* **Magic**: the layer below looks like a perfect pipe!

## 🔧 Fig. 3.8(b): **Service Implementation** (How RDT is actually built)

```text
   Application                     Application
      │                                ▲
      │ rdt_send(data)                 │ deliver_data(data)
      ▼                                │
 ┌───────────────────┐       ┌───────────────────┐
 │ Reliable Data     │       │ Reliable Data     │
 │ Transfer Protocol │       │ Transfer Protocol │
 │   (sender side)   │       │ (receiver side)   │
 └───────────────────┘       └───────────────────┘
      │                                ▲
      │ udt_send(pkt)                  │ rdt_rcv(pkt)
      ▼                                │
 ┌───────────────────┐        ┌───────────────────┐
 │ Unreliable        │◀───────┤ Unreliable        │
 │ Channel           │        │ Channel           │
 └───────────────────┘        └───────────────────┘
```

1. **`rdt_send(data)`**

   * Called by your application to send a chunk of data.

2. **`udt_send(pkt)`**

   * The RDT sender wraps `data` into a **packet** (adds headers, checksums, sequence numbers) and calls `udt_send()`.
   * **`udt_send()`** hands the packet to the **unreliable channel** (packets may get lost or corrupted).

3. **Unreliable Channel**

   * Can **lose** packets entirely or **corrupt** their bits.
   * **Assumption**: does **not** reorder packets.

4. **`rdt_rcv(pkt)`**

   * When a packet arrives, the RDT receiver is invoked.
   * It checks for **corruption** (via checksum) and **sequence correctness**.

5. **`deliver_data(data)`**

   * If packet is good **and** in order, the RDT receiver extracts `data` and delivers it to the application.
   * Otherwise, it discards or asks for **retransmission** (via ACK/NACK).


## 🎯 Key Building Blocks

1. **Checksums** 🧾

   * Detect bit errors.
   * Sender computes checksum; receiver recomputes and compares.

2. **Sequence Numbers** 🔢

   * Tag each packet (e.g., 0, 1, 2, …) so the receiver can detect losses or duplicates.

3. **Acknowledgments (ACKs) & Retransmissions** ↩️

   * Receiver sends an **ACK** when it gets a good packet.
   * If sender doesn’t get ACK in time, it **retransmits**.

4. **Timeouts** ⏲️

   * Sender starts a timer after sending.
   * If timer expires before ACK arrives, **re-send** the packet.

## 💡 Analogy: **Reliable Courier Service**

| Concept              | Courier Analogy                            |
| -------------------- | ------------------------------------------ |
| Packet               | A sealed envelope with a tracking number   |
| Checksum             | Tamper-evident seal                        |
| Sequence Number      | “Letter #5 of 10” label                    |
| ACK                  | Signed delivery receipt                    |
| Timeout & Retransmit | If no receipt arrives, resend the envelope |

A **reliable protocol** ensures **every letter** arrives **intact**, **in order**, or else gets **re-sent** until the receipt (ACK) is received.

---

#  **rdt1.0: Reliable Data Transfer over a **Perfectly Reliable** Channel** 📦

In **rdt1.0**, we assume the network below is **perfect**—no packets are ever lost or corrupted, and the receiver can always keep up with the sender. Because nothing can go wrong, the protocol is extremely simple!

<div align="center">
  <img src="./images/03.jpg" alt="" width="600px"/>
</div>

## 🏗️ Sender-Side FSM (Figure 3.9a)

```text
      ┌──────────────────────────────┐
      │ Wait for call from above    │  ←── initial state
      └──────────────────────────────┘
                  │
    rdt_send(data)│
                  ▼
      ┌──────────────────────────────┐
      │  Actions:                    │
      │ 1. packet = make_pkt(data)   │
      │ 2. udt_send(packet)          │
      │ 3. (no state change)         │
      └──────────────────────────────┘
                  │
                  └───loops back───▶
```

* **State**: “Waiting for data from the application.”
* **Event**: `rdt_send(data)`

  * Triggered when the application calls `rdt_send()` with new data.
* **Actions**:

  1. **Create a packet**: `packet = make_pkt(data)`
  2. **Send it**: `udt_send(packet)`
* **No feedback** or additional states—straight back to waiting for more data.

## 🏗️ Receiver-Side FSM (Figure 3.9b)

```text
      ┌──────────────────────────────┐
      │ Wait for packet from below  │  ←── initial state
      └──────────────────────────────┘
                  │
     rdt_rcv(packet)│
                  ▼
      ┌──────────────────────────────┐
      │  Actions:                    │
      │ 1. extract(packet, data)     │
      │ 2. deliver_data(data)        │
      │ 3. (no state change)         │
      └──────────────────────────────┘
                  │
                  └───loops back───▶
```

* **State**: “Waiting for a packet from the (perfect) channel.”
* **Event**: `rdt_rcv(packet)`

  * Triggered when `udt_send()`’s packet arrives intact.
* **Actions**:

  1. **Unpack data**: `extract(packet, data)`
  2. **Deliver up**: `deliver_data(data)` to the application.
* **No ACKs**, **no checksums**, **no sequence numbers**—just straight delivery.

## 🎯 Why rdt1.0 Is So Simple

1. **Perfect channel** ✅

   * **No losses** → no retransmissions needed.
   * **No corruptions** → no checksums or error detection.
2. **Infinite speed** ⚡

   * Receiver is assumed fast enough; no flow-control necessary.
3. **No feedback loop** 🔄

   * Since nothing can go wrong, the receiver never needs to tell the sender anything.

---

#  **rdt2.0: Handling **Bit Errors** with Stop-and-Wait ARQ** 🛠️

When the channel can corrupt bits (but still delivers packets in order), we upgrade rdt1.0 by adding:

1. **Error Detection** via **checksums**
2. **Receiver Feedback** using **ACK** (acknowledgment) and **NAK** (negative acknowledgment)
3. **Retransmission** of corrupted packets

This “stop-and-wait” protocol is called **rdt2.0**.

<div align="center">
  <img src="./images/04.jpg" alt="" width="600px"/>
</div>


## 📊 Sender FSM (Figure 3.10a)

```text
 State A: Wait for call from above
   │
   └─ rdt_send(data) ──────────────────▶
       • sndpkt = make_pkt(data, checksum)
       • udt_send(sndpkt)
       • Transition to State B

 State B: Wait for ACK or NAK
   │
   ├─ rdt_rcv(rcvpkt) && isACK(rcvpkt) ──▶
   │     • (valid ACK received)
   │     • Return to State A
   │
   └─ rdt_rcv(rcvpkt) && isNAK(rcvpkt) ──▶
         • (NAK or corrupted data detected)
         • udt_send(sndpkt)  ← retransmit same packet
         • Stay in State B
```

| State | Description                                |
| ----- | ------------------------------------------ |
| **A** | Waiting for application data.              |
| **B** | Waiting for receiver’s feedback (ACK/NAK). |

* **Event** `rdt_send(data)` in **State A**:

  * **Action**: create packet with data & checksum, send it, move to **State B**.
* **Event** `rdt_rcv(rcvpkt) && isACK(rcvpkt)` in **State B**:

  * **Action**: Got positive feedback ➡️ back to **State A** to send new data.
* **Event** `rdt_rcv(rcvpkt) && isNAK(rcvpkt)` in **State B**:

  * **Action**: Got negative feedback ➡️ **retransmit** previous packet, remain in **State B**.

## 📊 Receiver FSM (Figure 3.10b)

```text
 State R: Wait for call from below (packet arrival)
   │
   ├─ rdt_rcv(rcvpkt) && corrupt(rcvpkt) ──▶
   │     • (packet failed checksum)
   │     • sndpkt = make_pkt(NAK)
   │     • udt_send(sndpkt)
   │     • Stay in State R
   │
   └─ rdt_rcv(rcvpkt) && notcorrupt(rcvpkt) ──▶
         • extract(rcvpkt, data)
         • deliver_data(data)
         • sndpkt = make_pkt(ACK)
         • udt_send(sndpkt)
         • Stay in State R
```

* **State R**: Always “waiting for a packet.”
* **Event** `rdt_rcv(rcvpkt) && corrupt(rcvpkt)`:

  * **Action**: send a **NAK** back, so sender will retry.
* **Event** `rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)`:

  * **Action**: extract and deliver data to application, send an **ACK**.


## 🔍 How it Works

1. **Checksum**

   * Sender computes a checksum over message bits.
   * Receiver recomputes; mismatch ⇒ **corrupt**.

2. **ACK/NAK Feedback**

   * **ACK** (e.g., a packet with “ACK” flag) tells sender “I got it correctly.”
   * **NAK** tells sender “Please resend that packet.”

3. **Stop-and-Wait**

   * Sender sends **one** packet and then **waits** for ACK/NAK before sending the next.
   * Ensures in-order, error-free delivery, but can be slow (idle time while waiting).


## ⚠️ The Big Flaw

> **What if the ACK or NAK itself gets corrupted?**

* The sender might misinterpret a **corrupted ACK** as a NAK (or vice versa), leading to:

  * **Unnecessary retransmissions**, or
  * **Deadlock** (sender stuck waiting).

**Fixes** (in later versions, rdt2.1+ and rdt3.0):

* **Add checksums** to ACK/NAK packets.
* Use **sequence numbers** (0/1) to distinguish new ACKs from old/corrupted ones.
* Introduce **timeouts**, so sender can retransmit if no valid ACK arrives in time.

---

#  **rdt2.1: Stop-and-Wait with Sequence Numbers (Fixing Corrupted ACKs/NAKs)** 🔁

To handle corrupted control packets (ACKs/NAKs) without adding new packet types, **rdt2.1** adds a **1-bit sequence number** to every data packet. This lets the receiver detect duplicates and the sender know exactly which packet is being acknowledged.

<div align="center">
  <img src="./images/05.jpg" alt="" width="600px"/>
</div>

## 📶 Sender FSM (Figure 3.11)

The sender now has **four states**, alternating between “sending seq 0” and “sending seq 1”:

```
 ┌─────────────────────────────────────────────┐
 │ State S0: “Wait for call 0 from above”     │
 └─────────────────────────────────────────────┘
    │ rdt_send(data) when expecting seq 0
    ▼
  sndpkt = make_pkt(0, data, checksum)
  udt_send(sndpkt)
    │
    ▼
 ┌─────────────────────────────────────────────┐
 │ State S0_ACK: “Wait for ACK/NAK 0”          │
 └─────────────────────────────────────────────┘
    ├─ On rdt_rcv(rcvpkt) && (corrupt(rcvpkt)  
    │      || isNAK(rcvpkt)) ──────────▶
    │     • udt_send(sndpkt)  (retransmit 0)
    │     • Remain in State S0_ACK
    │
    └─ On rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)
          && isACK(rcvpkt) (ACK 0) ───▶
         • Transition to State S1  (ready for seq 1)
```

Then, **mirror** for sequence 1:

```
 ┌─────────────────────────────────────────────┐
 │ State S1: “Wait for call 1 from above”     │
 └─────────────────────────────────────────────┘
    │ rdt_send(data) when expecting seq 1
    ▼
  sndpkt = make_pkt(1, data, checksum)
  udt_send(sndpkt)
    │
    ▼
 ┌─────────────────────────────────────────────┐
 │ State S1_ACK: “Wait for ACK/NAK 1”          │
 └─────────────────────────────────────────────┘
    ├─ On rdt_rcv(rcvpkt) && (corrupt(rcvpkt)  
    │      || isNAK(rcvpkt)) ──────────▶
    │     • udt_send(sndpkt)  (retransmit 1)
    │     • Remain in State S1_ACK
    │
    └─ On rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)
          && isACK(rcvpkt) (ACK 1) ───▶
         • Transition back to State S0  (ready for seq 0)
```

### 🔑 Key Points

* **Single outstanding packet**: Sender never sends seq 1 until seq 0 is ACKed, and vice versa.
* **Retransmit on:**

  * **Corrupted ACK/NAK**
  * **Explicit NAK**
* **Advance** state only on a **valid ACK** matching the current sequence.

## 📩 Receiver FSM (Figure 3.12)

<div align="center">
  <img src="./images/06.jpg" alt="" width="600px"/>
</div>


The receiver also has **two states**—“expecting seq 0” and “expecting seq 1”:

```
 ┌─────────────────────────────────────────────┐
 │ State R0: “Wait for 0 from below”          │
 └─────────────────────────────────────────────┘
    ├─ On rdt_rcv(rcvpkt) && corrupt(rcvpkt) ─▶
    │     • sndpkt = make_pkt(NAK, checksum)
    │     • udt_send(sndpkt)  (NAK 0)
    │     • Stay in State R0
    │
    ├─ On rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)
    │      && has_seq0(rcvpkt) ──────────▶
    │     • extract(rcvpkt, data)
    │     • deliver_data(data)
    │     • sndpkt = make_pkt(ACK, checksum)
    │     • udt_send(sndpkt)  (ACK 0)
    │     • Transition to State R1
    │
    └─ On rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)
          && has_seq1(rcvpkt) ──────────▶
         • sndpkt = make_pkt(ACK, checksum)
         • udt_send(sndpkt)  (duplicate ACK 1)
         • Stay in State R0
```

Then mirror for **State R1** (“wait for seq 1”):

```
 ┌─────────────────────────────────────────────┐
 │ State R1: “Wait for 1 from below”          │
 └─────────────────────────────────────────────┘
    ├─ On rdt_rcv(rcvpkt) && corrupt(rcvpkt) ─▶
    │     • send NAK 1, stay in R1
    │
    ├─ On rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)
    │      && has_seq1(rcvpkt) ──────────▶
    │     • extract/deliver data
    │     • send ACK 1, move to State R0
    │
    └─ On rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)
          && has_seq0(rcvpkt) ──────────▶
         • send duplicate ACK 0, stay in R1
```

## 🎉 Why rdt2.1 Works

* **Corrupted ACKs/NAKs** → Sender re-sends the same seq; receiver recognizes it as a duplicate (same seq) and re-ACKs without re-delivering.
* **Lost ACKs** → Sender waits (or in rdt2.2, will use timeout) and re-sends; receiver handles duplicates safely.
* **Bit errors in data** → Detected by checksum → NAK → retransmit.

With these FSMs, rdt2.1 **guarantees** correct, in-order delivery over a channel that:

* May **corrupt** or **lose** packets
* **Does not** reorder packets

---

#  **rdt3.0: Handling **Lossy** Channels with Bit Errors** ⏲️

**rdt3.0** builds on rdt2.2 by adding a **timer** to detect and recover from **packet loss**. Combined with checksums and sequence numbers, this gives us a fully reliable “alternating-bit” protocol over a channel that can:

* 🔄 **Corrupt** packets
* ❌ **Lose** packets
* 🚫 **Not** reorder packets

---

## 📦 Figure 3.14: Sender FSM for rdt3.0

<div align="center">
  <img src="./images/08.jpg" alt="" width="600px"/>
</div>


```text
     ┌─────────────────────────────────────────────┐
     │ State S0: “Wait for call 0 from above”     │
     └─────────────────────────────────────────────┘
          │ rdt_send(data)
          ▼
       sndpkt = make_pkt(0, data, checksum)
       udt_send(sndpkt)
       start_timer()
          │
          ▼
     ┌─────────────────────────────────────────────┐
     │ State S0_WAIT: “Wait for ACK 0”             │
     └─────────────────────────────────────────────┘
          ├─ rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)
          │      && isACK(rcvpkt,0) ──────────▶
          │    stop_timer()
          │    Transition to State S1
          │
          ├─ rdt_rcv(rcvpkt) && (corrupt(rcvpkt)
          │      || isACK(rcvpkt,1)) ──────────▶
          │    Λ  (ignore spurious/corrupted)
          │    Remain in State S0_WAIT
          │
          └─ timeout ───────────────────────────▶
               udt_send(sndpkt)   (retransmit)
               start_timer()
               Remain in State S0_WAIT
```

Then, **mirror** for sequence `1`:

```text
     ┌─────────────────────────────────────────────┐
     │ State S1: “Wait for call 1 from above”     │
     └─────────────────────────────────────────────┘
          │ rdt_send(data)
          ▼
       sndpkt = make_pkt(1, data, checksum)
       udt_send(sndpkt)
       start_timer()
          │
          ▼
     ┌─────────────────────────────────────────────┐
     │ State S1_WAIT: “Wait for ACK 1”             │
     └─────────────────────────────────────────────┘
          ├─ rdt_rcv(rcvpkt) && notcorrupt(rcvpkt)
          │      && isACK(rcvpkt,1) ──────────▶
          │    stop_timer()
          │    Transition to State S0
          │
          ├─ rdt_rcv(rcvpkt) && (corrupt(rcvpkt)
          │      || isACK(rcvpkt,0)) ──────────▶
          │    Λ  (ignore)
          │    Remain in State S1_WAIT
          │
          └─ timeout ───────────────────────────▶
               udt_send(sndpkt)   (retransmit)
               start_timer()
               Remain in State S1_WAIT
```

### 🛠️ Key Sender Actions

1. **`start_timer()`**: begins countdown after each (re)transmission.
2. **`stop_timer()`**: cancels the timer when a correct ACK arrives.
3. **`timeout`** event: retransmits the last packet and restarts the timer.
4. **Sequence numbers (0/1)** ensure the sender knows which packet is being ACKed.

## ⏳ Figure 3.15: Timeline Illustrations

<div align="center">
  <img src="./images/09.jpg" alt="" width="600px"/>
</div>

Below are three scenarios showing how **rdt3.0** behaves over time:

```
Time ▶
```

### a) No Loss, No Errors

```
Sender: Snd pkt(0) ───────────▶ Receiver
             └─ start_timer()

Receiver: Deliver data(0)
          Snd ACK(0) ───────────▶ Sender

Sender: rdt_rcv(ACK(0)) ➔ stop_timer()
        Next call → snd pkt(1)...
```

* **Smooth flow**: data and ACK arrive before timer expires.

### b) Data Packet Lost

```
Sender: Snd pkt(0) ───────────▶ [lost]
             └─ start_timer()

(time passes, no ACK)

timeout ➔ Retransmit pkt(0), restart timer

Receiver: Now gets pkt(0)
          Deliver data(0)
          Snd ACK(0) ───────────▶ Sender

Sender: rdt_rcv(ACK(0)) ➔ stop_timer()
        Proceed to pkt(1)
```

* **Lost data** triggers **timeout** → retransmission → correct delivery.

### c) ACK Packet Lost

```
Sender: Snd pkt(0) ───────────▶ Receiver
             └─ start_timer()

Receiver: Deliver data(0)
          Snd ACK(0) ───▶ [lost]

(time passes, no ACK)

timeout ➔ Retransmit pkt(0), restart timer

Receiver: Receives duplicate pkt(0)
          ❌ Duplicate → re-send ACK(0)
          Stay in same state

Sender: rdt_rcv(ACK(0)) ➔ stop_timer()
        Move to pkt(1)
```

* **Lost ACK** treated the same as lost data: **timeout** → retransmit.
* Receiver sees **duplicate data** (same seq), ignores payload but re-ACKs.


## 🎉 Why rdt3.0 Works

1. **Checksums** catch bit errors in data and ACKs.
2. **Sequence numbers** detect duplicates, so duplicate deliveries are blocked.
3. **ACKs** confirm successful receipt; **timeouts** handle lost packets or ACKs.
4. **Stop-and-wait** keeps the design simple, ensuring in-order delivery.

With these mechanisms, **rdt3.0** (the “alternating-bit” protocol) provides a **fully reliable**, in-order data channel over an unreliable physical network! 🚀

---

#  **Pipelined Reliable Data Transfer Protocols** 📡

While **rdt3.0** (alternating-bit stop-and-wait) is **correct**, its **performance** is painfully low on high-delay, high-bandwidth links. The cure is **pipelining**—sending multiple packets “in flight” before waiting for ACKs.

## 🚀 Pipelined Reliable Data Transfer Protocols (Concise)

Instead of sending **one packet at a time** (stop-and-wait), pipelining lets the sender transmit **multiple packets** before waiting for acknowledgments. This greatly improves link utilization, especially on high-delay, high-speed links!

### 🔑 Key Ideas

1. **Window of Packets**

   * Sender can have up to **N un-ACKed** packets “in flight.”
   * Fills the “pipe” so the link isn’t idle.

2. **Larger Sequence Space**

   * Need at least **N distinct** sequence numbers (e.g., modulo arithmetic).

3. **Sender Buffering**

   * Stores all sent-but-un-ACKed packets for possible retransmission.

4. **Receiver Buffering (Selective-Repeat only)**

   * May buffer out-of-order packets until missing ones arrive.


### 🔄 Two Main ARQ Schemes

| Scheme               | How It Works                                                                          | Pros & Cons                                              |
| -------------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| **Go-Back-N**        | On a loss or timeout, retransmit that packet **and all** later ones in the window.    | ✅ Simple<br>❌ Wastes bandwidth if many packets were good |
| **Selective-Repeat** | Retransmit **only** the lost/corrupted packets; receiver holds others until complete. | ✅ Efficient<br>❌ More complex buffering & bookkeeping    |


### 📈 Why Pipelining Helps

* **Higher Throughput**
  Utilization ≈ (Window × L/R) / (RTT + L/R) → close to 100% for large windows.

* **Scalable**
  Works well on long-distance, high-capacity links (e.g., fiber-optic backbones).


## 📊 Figure 3.16: Operation of rdt3.0 (Alternating-Bit Protocol)

<div align="center">
  <img src="./images/10.jpg" alt="" width="600px"/>
</div>

Each subfigure shows **sender** and **receiver** packet exchanges over time (▶ receiver direction, ◀ sender direction).

|    Scenario    | What Happens |
| :------------: | :----------- |
| **a. No loss** |              |

1. Sender → pkt0 ▶ Receiver
2. Receiver ✔ pkt0, ◀ ACK0
3. Sender ✔ ACK0 → send pkt1
|✅ **Smooth, in-order delivery** |
</br>

| **b. Lost data packet** |
1. Sender → pkt0 ▶ \[lost]
2. **Timeout** at sender → retransmit pkt0
3. Receiver ✔ pkt0, ◀ ACK0
4. Sender ✔ ACK0 → send pkt1
|🕑 **Recovery by timeout & retransmission** |
</br>

| **c. Lost ACK** |
1. Sender → pkt0 ▶ Receiver
2. Receiver ✔ pkt0, ◀ ACK0 ▶ \[lost]
3. **Timeout** → retransmit pkt0
4. Receiver sees **duplicate pkt0**, re-sends ACK0
5. Sender ✔ ACK0 → send pkt1
|🔄 **Duplicate detection via seq#** |
</br>

| **d. Premature timeout** |
1. Sender → pkt0 ▶ Receiver
2. Receiver ✔ pkt0, ◀ ACK0 (delayed)
3. Sender **times out too early**, retransmits pkt0
4. Receiver sees **duplicate pkt0**, re-sends ACK0
5. First ACK0 arrives, sender ✔ → send pkt1
    ⏲️ **Timeout tuning matters** |

## 🌉 Figure 3.17: Stop-and-Wait vs Pipelined Protocol

<div align="center">
  <img src="./images/11.jpg" alt="" width="600px"/>
</div>

**a. Stop-and-Wait**
* One data packet in flight
* Sender **idle** until ACK returns
* Low utilization on long-delay links | **b. Pipelined**
* Many data packets in flight
* Sender continuously transmits up to window size
* Far higher link utilization |

## ⏱️ Figure 3.18: Timing Diagrams

<div align="center">
  <img src="./images/12.jpg" alt="" width="600px"/>
</div>

**Legend**:

* **RTT** = round-trip propagation delay (e.g., \~30 ms coast-to-coast)
* **L/R** = transmission time per packet (e.g., 8 μs for 1 000 bytes @1 Gbps)

|       Stop-and-Wait       | Pipelined (window = 3) |
| :-----------------------: | :--------------------: |
| **a. Single-packet flow** |                        |

* Sender busy for **L/R**, then waits **RTT–L/R** for ACK
* **Utilization** ≈ (L/R)/(RTT + L/R)
* For L/R=0.008 ms & RTT=30 ms → U ≈ 0.00027 (0.027%)  | **b. Pipeline of 3 packets**
* Sender transmits 3 packets back-to-back (3×L/R) before waiting
* Utilization ≈ (3·L/R)/(RTT + L/R)
* \~3× higher throughput, approaching link capacity |

## 🔑 Why Pipelining Helps

1. **Improved Utilization**

   * More “bits in flight” fills the link.
   * Idle wait times are amortized.

2. **Window Size & Sequence Numbers**

   * Must expand sequence number space to label each in-flight packet uniquely.
   * E.g., window of N requires at least N distinct sequence values modulo space.

3. **Buffering Requirements**

   * **Sender** buffers all un-ACKed packets (in case of retransmission).
   * **Receiver** may buffer out-of-order packets (depending on protocol).

4. **Two Pipelined ARQ Schemes**

   * **Go-Back-N (GBN)**

     * On error or timeout, **retransmit** the erroneous packet **and** all subsequent ones in window.
     * Simpler, but can waste bandwidth on good packets.
   * **Selective-Repeat (SR)**

     * Retransmit **only** the specific lost/corrupted packets.
     * Receiver buffers each in-order or out-of-order packet until delivery is complete.

---

