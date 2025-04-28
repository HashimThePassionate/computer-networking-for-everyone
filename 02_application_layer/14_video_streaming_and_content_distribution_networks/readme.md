# **Video Streaming and CDN** 📺🌐

## Overview 🎬

Streaming video services like **Netflix**, **YouTube**, and **Amazon Prime** dominate Internet traffic, accounting for approximately **80% of global Internet traffic in 2020** \[Cisco 2020\]. This section explores how these services are implemented using **application-level protocols** and **servers** that operate similarly to a cache, ensuring efficient delivery of video content to users worldwide. 🚀

## Internet Video: The Basics 📹

Internet video refers to **prerecorded videos** (e.g., movies, TV shows, YouTube content) stored on servers and streamed on-demand to users. Major providers include **Netflix**, **YouTube**, **Amazon**, and **TikTok**. Below are the key characteristics of Internet video:

### What is a Video? 🖼️

- A video is a **sequence of images** displayed at a constant rate, typically **24 or 30 frames per second**.
- Each image is an **array of pixels**, encoded into bits to represent **luminance** and **color**.
- **Compression** is critical:
  - Videos can be compressed to trade off **quality** for **bit rate**.
  - Higher bit rates yield better quality but consume more data. 📈
  - Example: A **2 Mbps** video of **67 minutes** consumes **1 GB** of storage or traffic.

### Bit Rate and Bandwidth 📊

- Compressed Internet video bit rates range from:
  - **100 kbps** for low-quality streams.
  - **4 Mbps** for high-definition (HD) streams.
  - **10 Mbps+** for **4K streaming**.
- **Key Performance Metric**: **Average end-to-end throughput** must match or exceed the video’s bit rate to ensure **continuous playback** without buffering. ⚡
- **Multiple Versions**: Compression allows creating multiple versions of the same video (e.g., **300 kbps**, **1 Mbps**, **3 Mbps**). Users select versions based on their **available bandwidth**:
  - High-speed users (e.g., fiber) may choose **3 Mbps**.
  - Mobile users (e.g., 3G) may opt for **300 kbps**.

## HTTP Streaming 📡

In **HTTP streaming**, videos are stored as **ordinary files** on an **HTTP server**, each with a unique **URL**. The process works as follows:

1. **Client Request**:
   - The client establishes a **TCP connection** with the server.
   - Sends an **HTTP GET request** for the video’s URL.
2. **Server Response**:
   - The server sends the video file in an **HTTP response**, as fast as network conditions allow.
3. **Client Playback**:
   - Bytes are collected in a **client application buffer**.
   - Once the buffer reaches a **threshold**, playback begins.
   - The streaming app periodically retrieves frames from the buffer, decompresses them, and displays them on the screen. 🖥️
4. **Ongoing Process**:
   - The client continues buffering later parts of the video while playing earlier parts.

### Limitation of HTTP Streaming ⚠️

- **Uniform Quality**: All clients receive the **same video encoding**, regardless of their bandwidth.
- This is problematic because:
  - Bandwidth varies across users (e.g., 3G vs. fiber).
  - Bandwidth fluctuates over time, especially for mobile users. 📉

## Dynamic Adaptive Streaming over HTTP (DASH) 🌟

**DASH** addresses the limitations of traditional HTTP streaming by enabling **adaptive streaming**. It allows clients to dynamically adjust video quality based on **available bandwidth**.

### How DASH Works 🔄

1. **Multiple Encodings**:
   - The video is encoded into **several versions**, each with a different **bit rate** and **quality level**.
   - Example: Versions at **300 kbps**, **1 Mbps**, and **3 Mbps**.
2. **Chunk-Based Delivery**:
   - Videos are divided into **small segments (chunks)**, typically a few seconds long.
   - Clients request chunks one at a time using **HTTP GET requests**.
3. **Manifest File**:
   - The HTTP server stores a **manifest file** that lists:
     - URLs for each video version.
     - Corresponding bit rates.
   - The client first downloads the manifest file to learn about available versions.
4. **Dynamic Selection**:
   - The client measures **received bandwidth** and runs a **rate determination algorithm**.
   - Based on **buffer status** and **bandwidth**:
     - **High bandwidth** or large buffer → Selects a **high bit rate chunk** (better quality).
     - **Low bandwidth** or small buffer → Selects a **low bit rate chunk** (lower quality).
5. **Seamless Switching**:
   - Clients can **switch between quality levels** as bandwidth changes, ensuring smooth playback. 🔄

### Benefits of DASH 🎉

- **Personalized Quality**:
  - Users with **low-speed connections** (e.g., 3G) receive **low bit rate** streams.
  - Users with **high-speed connections** (e.g., fiber) enjoy **high-quality** streams.
- **Adaptability**:
  - DASH adapts to **fluctuating bandwidth**, which is critical for mobile users moving between network zones (e.g., near or far from base stations). 📱
- **Efficient Resource Use**:
  - By selecting appropriate chunks, DASH optimizes **data usage** and ensures **continuous playback**.

### Example Workflow 🛠️

- A user on a **fiber connection** starts streaming a video:
  - Downloads the **manifest file**.
  - Sees high bandwidth (e.g., 10 Mbps) and selects **3 Mbps chunks**.
- The same user switches to **mobile data**:
  - Bandwidth drops to 500 kbps.
  - DASH automatically switches to **300 kbps chunks** to avoid buffering.