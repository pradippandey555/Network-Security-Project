# TCP/IP Stack - The Practical Implementation

## Overview

While the OSI model is conceptual, the **TCP/IP model** is the actual protocol suite used in real networks. It's simpler with 4 layers instead of 7.

## TCP/IP Model Layers

### Layer 4: Application Layer
**Equivalent to:** OSI Layers 5, 6, 7

**Protocols:**
- **HTTP/HTTPS** - Web browsing
- **FTP** - File transfer
- **SMTP/POP3/IMAP** - Email
- **SSH** - Secure shell
- **DNS** - Domain name resolution
- **DHCP** - Dynamic IP assignment
- **SNMP** - Network management
- **Telnet** - Remote login (unencrypted)
- **TFTP** - Trivial file transfer
- **RTP** - Real-time protocol (VoIP)

**Examples:**
```
You open Firefox → HTTP request sent → Server responds with web page
```

---

### Layer 3: Transport Layer
**Equivalent to:** OSI Layer 4

**Protocols:**

#### TCP (Transmission Control Protocol)
- **Connection-oriented** (establishes connection first)
- **Reliable** (ensures delivery)
- **Ordered** (maintains sequence)
- **Slower** (more overhead)
- **Uses:** HTTP, HTTPS, FTP, SSH, SMTP, POP3, IMAP
- **Port range:** 0-65535

**TCP 3-Way Handshake:**
```
1. Client → Server: SYN (synchronization request)
2. Server → Client: SYN-ACK (acknowledgment + request)
3. Client → Server: ACK (acknowledgment)
→ Connection established
```

#### UDP (User Datagram Protocol)
- **Connectionless** (sends immediately)
- **Unreliable** (no delivery guarantee)
- **Unordered** (no sequence)
- **Faster** (less overhead)
- **Uses:** DNS, DHCP, VoIP, Online games, Streaming
- **Port range:** 0-65535

**Comparison:**
| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Required | Not needed |
| Reliability | High | Low |
| Speed | Slower | Faster |
| Ordering | Guaranteed | Not guaranteed |
| Use Case | Email, Web | VoIP, Gaming |

---

### Layer 2: Internet Layer
**Equivalent to:** OSI Layer 3

**Protocols:**

#### IP (Internet Protocol)
- **IPv4** - 32-bit addresses (192.168.1.1)
- **IPv6** - 128-bit addresses (2001:db8::1)

#### Supporting Protocols
- **ICMP** - Diagnostics (Ping, Traceroute)
- **IGMP** - Multicast
- **ARP** - MAC address resolution

**Functions:**
- Logical addressing
- Routing
- Packet forwarding
- Fragmentation

**Example:**
```
Destination IP: 8.8.8.8 → Router looks up routing table → Forwards packet
```

---

### Layer 1: Link Layer
**Equivalent to:** OSI Layers 1 & 2

**Protocols:**
- **Ethernet** - Wired networks
- **WiFi (802.11)** - Wireless networks
- **PPP** - Point-to-point
- **HDLC** - Synchronous serial

**Functions:**
- Physical transmission
- MAC addressing
- Frame formatting
- Physical hardware control

---

## Data Flow Example: Sending an Email

```
┌─────────────────────────────────────────────────────┐
│ 1. Application Layer                                │
│    You click "Send" in Gmail                        │
│    → SMTP protocol sends message                    │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│ 2. Transport Layer                                  │
│    Email data broken into segments                  │
│    Port 25 (SMTP) assigned                          │
│    TCP creates connection to mail server            │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│ 3. Internet Layer                                   │
│    IP header added with source/dest IPs            │
│    Routing decision made                            │
│    Packet ready for transmission                    │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│ 4. Link Layer                                       │
│    Ethernet frame created with MAC addresses       │
│    Transmitted through network cable               │
│    Converted to electrical signals                 │
└─────────────────────────────────────────────────────┘
```

---

## Port Numbers (Important for Packet Tracer)

### Well-Known Ports (0-1023)

| Port | Service | Protocol |
|------|---------|----------|
| 20 | FTP Data | TCP |
| 21 | FTP Control | TCP |
| 22 | SSH | TCP |
| 23 | Telnet | TCP |
| 25 | SMTP | TCP |
| 53 | DNS | TCP/UDP |
| 67 | DHCP Server | UDP |
| 68 | DHCP Client | UDP |
| 80 | HTTP | TCP |
| 110 | POP3 | TCP |
| 143 | IMAP | TCP |
| 443 | HTTPS | TCP |
| 161 | SNMP | UDP |
| 162 | SNMP Trap | UDP |
| 389 | LDAP | TCP/UDP |
| 636 | LDAPS | TCP |

---

## Common Ports Used in Packet Tracer Labs

```
┌─────────────────────────────────────────┐
│ Management Protocols                    │
├─────────────────────────────────────────┤
│ SSH (Port 22) - Secure access          │
│ Telnet (Port 23) - Unsecured access    │
│ SNMP (Port 161) - Network monitoring   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ Email Protocols                         │
├─────────────────────────────────────────┤
│ SMTP (Port 25) - Send email            │
│ POP3 (Port 110) - Receive email        │
│ IMAP (Port 143) - Advanced email       │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ Web Protocols                           │
├─────────────────────────────────────────┤
│ HTTP (Port 80) - Web browsing          │
│ HTTPS (Port 443) - Secure web          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ File Transfer                           │
├─────────────────────────────────────────┤
│ FTP (Port 20/21) - File transfer       │
│ SFTP (Port 22) - Secure file transfer  │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│ Network Configuration                   │
├─────────────────────────────────────────┤
│ DHCP (Port 67/68) - Auto IP config     │
│ DNS (Port 53) - Name resolution        │
└─────────────────────────────────────────┘
```

---

## Summary

- **TCP/IP** is the practical protocol suite used in real networks
- **4 layers** make it simpler than OSI model
- **TCP** for reliable communication (email, web)
- **UDP** for fast communication (VoIP, gaming)
- **IP addresses** identify hosts on network
- **Port numbers** identify services on hosts

## Next: IP Addressing
Move to `03-IP-Addressing/` to learn how IP addresses work.