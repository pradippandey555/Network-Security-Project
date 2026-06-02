# The OSI Model - Layer by Layer

## Overview

The Open Systems Interconnection (OSI) model is a conceptual framework that describes how network communication works. It divides the process into 7 layers, each with specific functions and protocols.

## The 7 Layers of OSI

### Layer 7: Application Layer
**Function:** User services and application interface

**Key Protocols:**
- HTTP/HTTPS (Web browsing)
- FTP (File transfer)
- SMTP (Email sending)
- POP3/IMAP (Email receiving)
- SSH (Secure shell)
- Telnet (Remote login)
- DNS (Domain name resolution)

**Examples:**
- Web browsers
- Email clients
- File transfer applications
- Remote desktop tools

---

### Layer 6: Presentation Layer
**Function:** Data formatting, encryption, and compression

**Key Functions:**
- Character encoding (ASCII, Unicode)
- Encryption/Decryption (SSL/TLS)
- Data compression
- Data formatting

**Examples:**
- SSL/TLS certificates
- JPEG/PNG image formatting
- Video codecs
- Data encryption standards

---

### Layer 5: Session Layer
**Function:** Establishes, maintains, and terminates communication sessions

**Key Functions:**
- Session establishment
- Session maintenance
- Session termination
- Synchronization

**Protocols:**
- NetBIOS
- RPC (Remote Procedure Call)
- PPTP (Point-to-Point Tunneling Protocol)

---

### Layer 4: Transport Layer
**Function:** End-to-end delivery and flow control

**Key Protocols:**
- **TCP (Transmission Control Protocol)** - Reliable, connection-oriented
- **UDP (User Datagram Protocol)** - Fast, connectionless
- SCTP (Stream Control Transmission Protocol)

**Functions:**
- Segmentation and reassembly
- Flow control
- Error checking
- Port-based communication

**Port Examples:**
- Port 80: HTTP
- Port 443: HTTPS
- Port 21: FTP
- Port 22: SSH
- Port 25: SMTP
- Port 53: DNS

---

### Layer 3: Network Layer
**Function:** Routing and IP addressing

**Key Protocols:**
- IP (IPv4, IPv6)
- ICMP (Internet Control Message Protocol)
- IGMP (Internet Group Management Protocol)
- ARP (Address Resolution Protocol)
- BGP, OSPF, EIGRP (Routing protocols)

**Functions:**
- IP addressing
- Routing
- Packet forwarding
- Logical network design

**Examples:**
- Routers
- IP addresses (192.168.1.1)
- Routing tables

---

### Layer 2: Data Link Layer
**Function:** MAC addressing and physical transmission

**Key Protocols:**
- Ethernet
- PPP (Point-to-Point Protocol)
- Frame Relay
- 802.1X (Port Security)
- VLAN (802.1Q)

**Functions:**
- MAC addressing
- Frame formatting
- Error detection
- Physical addressing

**Examples:**
- Switches
- MAC addresses (00:1A:2B:3C:4D:5E)
- Network cards

---

### Layer 1: Physical Layer
**Function:** Physical transmission of data

**Components:**
- Cables (Copper, Fiber Optic)
- Connectors (RJ45, LC)
- Hubs
- Repeaters
- Physical signals (Voltage, Light)

**Functions:**
- Bit transmission
- Physical connection
- Signal encoding

**Examples:**
- Ethernet cables
- Fiber optic cables
- Network interface cards (NICs)
- Hubs (Layer 1 devices)

---

## Layer Interaction Example

When you browse a website (example.com), here's what happens:

1. **Layer 7 (Application):** Web browser sends HTTP request
2. **Layer 6 (Presentation):** Request is formatted and encrypted (HTTPS)
3. **Layer 5 (Session):** Session established with web server
4. **Layer 4 (Transport):** TCP breaks data into segments, manages ports (80/443)
5. **Layer 3 (Network):** IP addresses source and destination (192.168.1.100 → example.com's IP)
6. **Layer 2 (Data Link):** MAC addresses added (Your MAC → Router MAC)
7. **Layer 1 (Physical):** Data transmitted as electrical signals through cables

---

## Memory Aid: "Please Do Not Throw Sausage Pizza Away"

- **P**hysical (Layer 1)
- **D**ata Link (Layer 2)
- **N**etwork (Layer 3)
- **T**ransport (Layer 4)
- **S**ession (Layer 5)
- **P**resentation (Layer 6)
- **A**pplication (Layer 7)

---

## OSI vs TCP/IP Model

| OSI Layers | TCP/IP Model |
|-----------|----------|
| Layer 7, 6, 5 | Application |
| Layer 4 | Transport |
| Layer 3 | Internet |
| Layer 2, 1 | Link |

---

## Practice Questions

1. At which layer does routing occur?
   **Answer:** Layer 3 (Network Layer)

2. What layer is responsible for MAC addressing?
   **Answer:** Layer 2 (Data Link Layer)

3. Which protocol operates at Layer 4?
   **Answer:** TCP and UDP

4. What is the function of Layer 6?
   **Answer:** Data formatting, encryption, and compression

5. Which device operates at Layer 1?
   **Answer:** Hub, repeater, or physical cables

---

## Key Concepts

- **Protocol Data Unit (PDU):** Different names at each layer
  - Layer 7-5: Data
  - Layer 4: Segment (TCP) or Datagram (UDP)
  - Layer 3: Packet
  - Layer 2: Frame
  - Layer 1: Bit

- **Encapsulation:** Each layer adds its own header (and sometimes trailer)
- **De-encapsulation:** Each layer removes its header when receiving data

---

## Summary

The OSI model provides a structured way to understand network communication. Each layer has specific responsibilities and works with the layers above and below it. Understanding the OSI model is essential for network troubleshooting and configuration.

## Next: TCP/IP Stack
Move to `02-TCP-IP-Stack/` to understand the practical implementation of these layers.