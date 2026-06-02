# Subnetting Guide - Practical Examples for Packet Tracer

## Why Subnetting?

1. **Efficiency** - Use IP address space efficiently
2. **Security** - Isolate traffic between departments
3. **Performance** - Reduce broadcast domains
4. **Scalability** - Organize large networks logically

## Subnetting Method 1: CIDR Notation (Easiest)

### Understanding /Notation

The number after the slash indicates how many bits are for the network:

```
/8  = 255.0.0.0         (Class A)
/16 = 255.255.0.0       (Class B)
/24 = 255.255.255.0     (Class C - Most common for small networks)
/25 = 255.255.255.128   (Split a Class C in half)
/26 = 255.255.255.192   (Split into 4)
/27 = 255.255.255.224   (Split into 8)
/28 = 255.255.255.240   (Split into 16)
/29 = 255.255.255.248   (Split into 32)
/30 = 255.255.255.252   (Split into 64 - Used for router links)
/31 = 255.255.255.254   (Split into 128 - Point-to-point)
/32 = 255.255.255.255   (Single host)
```

### Quick Reference: How Many Subnets and Hosts?

**Formula:**
- Number of Subnets = 2^(host bits available in original class)
- Number of Hosts per Subnet = 2^(host bits) - 2

**Example: Divide 192.168.1.0/24 into /26**
- Original class C: 192.168.1.0/24 (last 8 bits for hosts)
- New prefix: /26 (last 6 bits for hosts)
- Borrowed bits: 8 - 6 = 2 bits
- Number of subnets: 2^2 = 4 subnets
- Hosts per subnet: 2^6 - 2 = 62 hosts

---

## Practical Subnetting Examples for Packet Tracer

### Example 1: Small Company with 3 Departments

**Requirement:** Divide 192.168.0.0/24 for:
- Sales: 50 hosts
- IT: 30 hosts
- Accounting: 25 hosts

**Solution: Use /25 (128 hosts per subnet)**

```
Subnet 1 (Sales): 192.168.0.0/25
  Network: 192.168.0.0
  First Host: 192.168.0.1
  Last Host: 192.168.0.126
  Broadcast: 192.168.0.127
  Available: 126 hosts ✓

Subnet 2 (IT): 192.168.0.128/25
  Network: 192.168.0.128
  First Host: 192.168.0.129
  Last Host: 192.168.0.254
  Broadcast: 192.168.0.255
  Available: 126 hosts ✓

Subnet 3 (Accounting): 192.168.1.0/25
  Network: 192.168.1.0
  First Host: 192.168.1.1
  Last Host: 192.168.1.126
  Broadcast: 192.168.1.127
  Available: 126 hosts ✓
```

**Packet Tracer Topology:**
```
        [Router1]
        /    |    \
    Fa0/0  Fa0/1  Fa0/2
      |      |      |
   [SW1]  [SW2]  [SW3]
      |      |      |
    Sales   IT   Accounting
   (Vlan10) (Vlan20) (Vlan30)
```

**Router Configuration:**
```
interface FastEthernet 0/0
  ip address 192.168.0.1 255.255.255.128
  description Sales

interface FastEthernet 0/1
  ip address 192.168.0.129 255.255.255.128
  description IT

interface FastEthernet 0/2
  ip address 192.168.1.1 255.255.255.128
  description Accounting
```

---

### Example 2: Point-to-Point Router Link

**Requirement:** Connect two routers with minimal IP waste

**Solution: Use /30 (4 addresses, 2 usable)**

```
Router Link: 203.0.113.0/30
  Network: 203.0.113.0
  Router1: 203.0.113.1
  Router2: 203.0.113.2
  Broadcast: 203.0.113.3
  Wasted: 0 addresses ✓
```

**Packet Tracer Configuration:**

**Router1 Serial Link:**
```
interface Serial 0/0/0
  ip address 203.0.113.1 255.255.255.252
  no shutdown
```

**Router2 Serial Link:**
```
interface Serial 0/0/0
  ip address 203.0.113.2 255.255.255.252
  no shutdown
```

---

### Example 3: Variable-Length Subnet Mask (VLSM)

**Requirement:** Subnet 10.0.0.0/8 for different size departments
- Finance: 500 hosts
- Sales: 250 hosts
- IT: 100 hosts
- Router Links: 2 hosts each

**Solution:**

```
Finance (500 hosts) → /23 (510 hosts)
  10.0.0.0/23
  Subnet Mask: 255.255.254.0

Sales (250 hosts) → /24 (254 hosts)
  10.0.2.0/24
  Subnet Mask: 255.255.255.0

IT (100 hosts) → /25 (126 hosts)
  10.0.3.0/25
  Subnet Mask: 255.255.255.128

Router Link 1 → /30 (2 hosts)
  10.0.3.128/30
  Subnet Mask: 255.255.255.252

Router Link 2 → /30 (2 hosts)
  10.0.3.132/30
  Subnet Mask: 255.255.255.252
```

---

## Binary Subnetting (The Hard Way)

If CIDR notation isn't intuitive, use binary:

**Example: 192.168.1.0/25**

**Step 1: Convert to binary**
```
192.168.1.0 = 11000000.10101000.00000001.00000000
```

**Step 2: Show the network/host split**
```
Network bits (25):  11000000.10101000.00000001.0
Host bits (7):                                    0000000
```

**Step 3: Calculate network and broadcast**
```
Network (all host bits = 0):     11000000.10101000.00000001.00000000 = 192.168.1.0
First host (host bits = ...001): 11000000.10101000.00000001.00000001 = 192.168.1.1
Last host (host bits = ...110):  11000000.10101000.00000001.01111110 = 192.168.1.126
Broadcast (all host bits = 1):   11000000.10101000.00000001.01111111 = 192.168.1.127
```

---

## Subnetting Drill Problems

### Problem 1
Subnet 10.0.0.0/8 into networks for 100 hosts each:
- How many /24 networks? **Answer:** 256 networks
- First three networks? **Answer:** 10.0.0.0/24, 10.0.1.0/24, 10.0.2.0/24

### Problem 2
You need 5 subnets from 192.168.0.0/24:
- What prefix length? **Answer:** /27 (creates 8 subnets)
- Hosts per subnet? **Answer:** 30 hosts
- First three subnets?
  - 192.168.0.0/27 (0-31)
  - 192.168.0.32/27 (32-63)
  - 192.168.0.64/27 (64-95)

### Problem 3
Design addressing for network with:
- Marketing: 60 hosts
- Operations: 40 hosts
- Management: 15 hosts

Use 172.16.0.0/16:
- Marketing: 172.16.0.0/25 (126 hosts available)
- Operations: 172.16.0.128/26 (62 hosts available)
- Management: 172.16.0.192/27 (30 hosts available)

---

## Packet Tracer Subnetting Checklist

- [ ] Identify required number of hosts
- [ ] Determine smallest subnet size needed
- [ ] Calculate CIDR notation
- [ ] List all subnet ranges
- [ ] Assign gateway IPs to routers
- [ ] Assign host IPs to PCs
- [ ] Verify with ping command
- [ ] Check connectivity across all subnets

---

## Common Subnet Masks (Memorize These)

```
/24 = 255.255.255.0       (256 addresses, 254 hosts) - MOST COMMON
/25 = 255.255.255.128     (128 addresses, 126 hosts)
/26 = 255.255.255.192     (64 addresses, 62 hosts)
/27 = 255.255.255.224     (32 addresses, 30 hosts)
/28 = 255.255.255.240     (16 addresses, 14 hosts)
/29 = 255.255.255.248     (8 addresses, 6 hosts)
/30 = 255.255.255.252     (4 addresses, 2 hosts) - Router links
```

---

## Summary

- Subnetting divides networks into smaller, more efficient segments
- CIDR notation (/24, /25, etc.) is the modern standard
- Private ranges should be used in corporate networks
- Always plan for future growth when subnetting
- /30 is ideal for point-to-point router links

## Next Steps

Now that you understand IP addressing and subnetting, move to **02-Switching-Configuration** to learn how to implement these concepts in switches and VLANs.