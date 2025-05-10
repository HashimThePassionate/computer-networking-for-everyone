# 🌐 **Delay, Loss, and Throughput in Packet-Switched Networks**

## 📑 **Table of Contents**
- [🌐 **Delay, Loss, and Throughput in Packet-Switched Networks**](#-delay-loss-and-throughput-in-packet-switched-networks)
  - [📑 **Table of Contents**](#-table-of-contents)
  - [🖥️ **Introduction**](#️-introduction)
  - [🔄 **Key Concepts**](#-key-concepts)
  - [📌 **Overview of Delay in Packet-Switched Networks**](#-overview-of-delay-in-packet-switched-networks)
  - [📊 **Impact of Delays on Applications**](#-impact-of-delays-on-applications)



## 🖥️ **Introduction**
In an ideal world, the Internet would:
- Instantly transfer unlimited data between any two end systems.
- Deliver data without any loss.
- Provide infinite throughput.

However, the reality of physical constraints introduces **delay**, **packet loss**, and **limited throughput** in computer networks. These challenges are integral to network performance and are central to understanding the behavior of packet-switched networks.

This section explores these issues and provides a foundation for understanding their impact on network performance.

---

## 🔄 **Key Concepts**

1. **Delay**:
   - The time it takes for a packet to travel from the source to the destination.
   - Comprised of multiple components: **processing delay**, **queuing delay**, **transmission delay**, and **propagation delay**.

2. **Loss**:
   - Occurs when packets are dropped due to congestion or buffer overflow.

3. **Throughput**:
   - The rate at which data is successfully transmitted from source to destination, measured in bits per second (bps).

---

## 📌 **Overview of Delay in Packet-Switched Networks**

When a packet travels from a **source** to a **destination**, it passes through multiple **nodes** (routers and hosts). At each node, the packet experiences several types of delays, which together contribute to the **total nodal delay**.



## 📊 **Impact of Delays on Applications**

1. **Web Browsing**:
   - Users experience lag if delays exceed expectations, affecting user experience.

2. **Voice-over-IP (VoIP)**:
   - Sensitive to delays, particularly queuing and propagation delays, which can cause echo or lag.

3. **Streaming Services**:
   - Require consistent throughput with minimal delays to avoid buffering.

---