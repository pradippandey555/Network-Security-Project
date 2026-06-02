# IP Addressing - IPv4 and IPv6

## IPv4 Addressing

### Basics
- **32-bit address** divided into 4 octets (8 bits each)
- **Dotted decimal notation:** 192.168.1.1
- **Binary notation:** 11000000.10101000.00000001.00000001
- **Range:** 0.0.0.0 to 255.255.255.255 (4,294,967,296 possible addresses)

### IPv4 Address Classes

| Class | Range | First Octet | Default Mask | Hosts per Network |
|-------|-------|------------|-------------|------------------|
| A | 1.0.0.0 - 126.255.255.255 | 1-126 | 255.0.0.0 | 16,777,214 |
| B | 128.0.0.0 - 191.255.255.255 | 128-191 | 255.255.0.0 | 65,534 |
| C | 192.0.0.0 - 223.255.255.255 | 192-223 | 255.255.255.0 | 254 |
| D | 224.0.0.0 - 239.255.255.255 | 224-239 | N/A | Multicast |
| E | 240.0.0.0 - 255.255.255.255 | 240-255 | N/A | Reserved |

### Private IP Address Ranges

These addresses are reserved for internal networks and not routed on the internet:

**Class A Private Range:**
- 10.0.0.0 to 10.255.255.255
- Subnet Mask: 255.0.0.0 (/8)
- Hosts: 16,777,214

**Class B Private Range:**
- 172.16.0.0 to 172.31.255.255
- Subnet Mask: 255.255.0.0 (/12)
- Hosts: 1,048,574

**Class C Private Range:**
- 192.168.0.0 to 192.168.255.255
- Subnet Mask: 255.255.255.0 (/16)
- Hosts: 65,534

### Special IPv4 Addresses

| Address | Purpose | Example |
|---------|---------|----------|
| Network | First address in subnet | 192.168.1.0 |
| Broadcast | Last address in subnet | 192.168.1.255 |
| Gateway | Router address | 192.168.1.1 |
| Host | Individual device | 192.168.1.10 |
| Loopback | Local testing | 127.0.0.1 |
| APIPA | Automatic private IP | 169.254.x.x |

### Subnet Mask

A 32-bit number that separates the network portion from the host portion:

**Example: 192.168.1.0/24**
- IP: 192.168.1.0
- Subnet Mask: 255.255.255.0
- Network Bits: /24 (first 24 bits are network)
- Host Bits: /8 (last 8 bits are host)
- Total Addresses: 256
- Usable Host Addresses: 254 (minus network and broadcast)

---

## IPv6 Addressing

### Basics
- **128-bit address** (vs IPv4's 32-bit)
- **Hexadecimal notation:** 2001:0db8:85a3:0000:0000:8a2e:0370:7334
- **Abbreviated:** 2001:db8:85a3::8a2e:370:7334
- **Range:** Virtually unlimited addresses

### IPv6 Address Types

**Unicast** - One-to-one communication
- Global Unicast: 2000::/3
- Link-Local: fe80::/10
- Loopback: ::1

**Multicast** - One-to-many communication
- Starts with: ff00::/8

**Anycast** - One-to-nearest communication
- Any unicast address

### Common IPv6 Addresses

| Address | Purpose |
|---------|----------|
| 2001:db8::/32 | Documentation |
| fe80::/10 | Link-local |
| ::1 | Loopback |
| ff02::1 | All nodes multicast |
| ff02::2 | All routers multicast |

### IPv6 Prefix

Similar to subnet mask in IPv4:

**Example: 2001:db8:1234:5678::1/64**
- First 64 bits: Network
- Last 64 bits: Interface ID (host)

---

## CIDR Notation (Classless Inter-Domain Routing)

CIDR notation uses /number to represent the number of network bits:

| CIDR | Subnet Mask | Hosts | Class |
|------|------------|-------|-------|
| /8 | 255.0.0.0 | 16,777,214 | A |
| /16 | 255.255.0.0 | 65,534 | B |
| /24 | 255.255.255.0 | 254 | C |
| /25 | 255.255.255.128 | 126 | - |
| /26 | 255.255.255.192 | 62 | - |
| /27 | 255.255.255.224 | 30 | - |
| /28 | 255.255.255.240 | 14 | - |
| /29 | 255.255.255.248 | 6 | - |
| /30 | 255.255.255.252 | 2 | - |
| /31 | 255.255.255.254 | 2 | Point-to-point |
| /32 | 255.255.255.255 | 1 | Host |

---

## Packet Tracer Addressing Examples

### Example 1: Simple 2-Router Network

**Network Design:**
```
PC1 (192.168.1.10) -- Switch -- Router1 -- Router2 -- Switch -- PC2 (10.0.0.10)
                    (Fa0/0)              (S0/0/0)     (Fa0/0)
```

**Router1 Configuration:**
```
Interface Fa0/0: 192.168.1.1 (connects to PC1 network)
Interface S0/0/0: 203.0.113.1 (connects to Router2)
Default Route: 0.0.0.0 0.0.0.0 203.0.113.2
```

**Router2 Configuration:**
```
Interface S0/0/0: 203.0.113.2 (connects to Router1)
Interface Fa0/0: 10.0.0.1 (connects to PC2 network)
Default Route: 0.0.0.0 0.0.0.0 203.0.113.1
```

**PC1 Configuration:**
```
IP Address: 192.168.1.10
Subnet Mask: 255.255.255.0
Default Gateway: 192.168.1.1 (Router1 Fa0/0)
DNS Server: 8.8.8.8
```

**PC2 Configuration:**
```
IP Address: 10.0.0.10
Subnet Mask: 255.255.255.0
Default Gateway: 10.0.0.1 (Router2 Fa0/0)
DNS Server: 8.8.8.8
```

### Example 2: Multiple Subnets with VLANs

**Network Design:**
```
Sales VLAN 10: 192.168.10.0/24
IT VLAN 20: 192.168.20.0/24
Accounting VLAN 30: 192.168.30.0/24
```

---

## How to Calculate Network and Broadcast Addresses

### For 192.168.1.128/25

**Step 1:** Convert mask /25 to binary
- /25 = 255.255.255.128 (25 ones, 7 zeros)

**Step 2:** Apply mask to IP
- IP: 192.168.1.128
- Mask: 255.255.255.128
- Network: 192.168.1.128 (AND operation)

**Step 3:** Calculate broadcast
- Change all host bits to 1
- Broadcast: 192.168.1.255

**Step 4:** Calculate valid hosts
- Network: 192.168.1.128
- First Host: 192.168.1.129
- Last Host: 192.168.1.254
- Broadcast: 192.168.1.255
- Total Hosts: 126

---

## Packet Tracer IP Assignment Checklist

- [ ] Calculate network and broadcast addresses
- [ ] Assign IP to Router interface
- [ ] Assign gateway to PC
- [ ] Assign subnet mask to all devices
- [ ] Test with Ping command
- [ ] Verify ARP with "show arp" on router
- [ ] Check routing table with "show ip route"

---

## Summary

- IPv4 uses 32-bit addresses, IPv6 uses 128-bit
- Private ranges are for internal use (10.x, 172.16-31.x, 192.168.x.x)
- Subnet mask determines network and host portions
- CIDR notation (/24, /25, etc.) is standard in modern networks
- Proper IP planning is critical for network design

## Next: Subnetting
Move to `04-Subnetting-Guide/` to practice subnetting calculations.