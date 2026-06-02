# Static Routing - Foundation for Understanding Routing

## What is Static Routing?

Static routing is:
- **Manual configuration** - Administrator specifies routes
- **No discovery** - Router doesn't learn about network changes automatically
- **Simple** - Easy to understand and troubleshoot
- **Efficient** - Uses minimal bandwidth
- **Limited** - Not suitable for large, dynamic networks

## When to Use Static Routes

✅ **Use Static Routes for:**
- Small networks with few routers
- Default routes (route to ISP)
- Backup/redundant paths
- Security-sensitive networks
- Point-to-point links
- Administrative control over routing decisions

❌ **Don't Use Static Routes for:**
- Large complex networks
- Frequently changing topologies
- Networks requiring automatic failover
- ISP-scale routing

---

## Packet Tracer Static Routing Lab

### Network Topology

```
Network 1: 192.168.1.0/24        Network 2: 192.168.2.0/24
   [PC1]                            [PC2]
     │                                │
   [SW1]                            [SW2]
     │ Fa0/0                          │ Fa0/0
   192.168.1.1                      192.168.2.1
     │                                │
   [Router1] ─── S0/0/0 ─── S0/0/0 ─── [Router2]
  203.0.113.1            203.0.113.2
```

### Step 1: Configure Router1 Interfaces

```
Router1> enable
Router1# configure terminal
Router1(config)# hostname Router1

!--- Configure Fa0/0 (connects to PC1 network)
Router1(config)# interface FastEthernet 0/0
Router1(config-if)# ip address 192.168.1.1 255.255.255.0
Router1(config-if)# description Link to Network 1
Router1(config-if)# no shutdown
Router1(config-if)# exit

!--- Configure S0/0/0 (connects to Router2)
Router1(config)# interface Serial 0/0/0
Router1(config-if)# ip address 203.0.113.1 255.255.255.252
Router1(config-if)# description Link to Router2
Router1(config-if)# no shutdown
Router1(config-if)# exit
```

### Step 2: Configure Router1 Static Routes

```
!--- Route to Network 2 via Router2
Router1(config)# ip route 192.168.2.0 255.255.255.0 203.0.113.2

!--- Default route (for any unknown destination)
Router1(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.2
```

### Step 3: Configure Router2 Interfaces

```
Router2> enable
Router2# configure terminal
Router2(config)# hostname Router2

!--- Configure S0/0/0 (connects to Router1)
Router2(config)# interface Serial 0/0/0
Router2(config-if)# ip address 203.0.113.2 255.255.255.252
Router2(config-if)# description Link to Router1
Router2(config-if)# no shutdown
Router2(config-if)# exit

!--- Configure Fa0/0 (connects to PC2 network)
Router2(config)# interface FastEthernet 0/0
Router2(config-if)# ip address 192.168.2.1 255.255.255.0
Router2(config-if)# description Link to Network 2
Router2(config-if)# no shutdown
Router2(config-if)# exit
```

### Step 4: Configure Router2 Static Routes

```
!--- Route to Network 1 via Router1
Router2(config)# ip route 192.168.1.0 255.255.255.0 203.0.113.1

!--- Default route (for any unknown destination)
Router2(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.1
```

### Step 5: Configure PCs

**PC1 Configuration:**
- IP Address: 192.168.1.10
- Subnet Mask: 255.255.255.0
- Default Gateway: 192.168.1.1 (Router1 Fa0/0)

**PC2 Configuration:**
- IP Address: 192.168.2.10
- Subnet Mask: 255.255.255.0
- Default Gateway: 192.168.2.1 (Router2 Fa0/0)

---

## Verification Commands

### View Routing Table
```
Router1# show ip route

Codes: C - connected, S - static, R - RIP, M - mobile, B - BGP
       D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area

Gateway of last resort is 203.0.113.2 to network 0.0.0.0

C    192.168.1.0/24 is directly connected, FastEthernet0/0
C    203.0.113.0/30 is directly connected, Serial0/0/0
S    192.168.2.0/24 [1/0] via 203.0.113.2
S*   0.0.0.0/0 [1/0] via 203.0.113.2
```

### Test Connectivity
```
PC1# ping 192.168.2.10
Pinging 192.168.2.10 with 32 bytes of data:

Reply from 192.168.2.10: bytes=32 time=10ms TTL=126
Reply from 192.168.2.10: bytes=32 time=10ms TTL=126
Reply from 192.168.2.10: bytes=32 time=10ms TTL=126
Reply from 192.168.2.10: bytes=32 time=10ms TTL=126

Ping statistics for 192.168.2.10:
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

### Trace Route Path
```
PC1# tracert 192.168.2.10
Tracing route to 192.168.2.10 over a maximum of 30 hops:

  1     *        *        *     Request timed out.
  2    10ms    10ms    10ms    192.168.2.10

Trace complete.
```

---

## Static Route Syntax Explained

### Basic Format
```
ip route destination-network subnet-mask next-hop-address
```

### Example: Route to 10.0.0.0/24 via 192.168.1.254
```
Router(config)# ip route 10.0.0.0 255.255.255.0 192.168.1.254
│                      │             │             │
│                      │             │             └─ Next hop (gateway)
│                      │             └─ Subnet mask
│                      └─ Destination network
└─ Command
```

### Default Route (Route of Last Resort)
```
Router(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.254
│                      │        │        │
│                      │        │        └─ Gateway (usually ISP)
│                      │        └─ Match all hosts (0.0.0.0)
│                      └─ Match all networks (0.0.0.0)
└─ Send unknown traffic to gateway
```

### Floating Static Route (Backup Route)
```
Router(config)# ip route 192.168.2.0 255.255.255.0 203.0.113.2 1
│                                                                  └─ Administrative distance (higher = lower priority)

Secondary route (takes over if primary fails):
Router(config)# ip route 192.168.2.0 255.255.255.0 203.0.113.3 2
```

---

## Common Issues and Solutions

### Problem: "Network is unreachable"
**Causes:**
1. No route to destination
2. Next hop is unreachable
3. Subnet mask is wrong

**Solution:**
```
Router# show ip route              # Check routing table
Router# ping next-hop-address      # Verify gateway is reachable
Router# show ip interface brief    # Verify interfaces are up
```

### Problem: Routes are removed after reboot
**Cause:** Configuration not saved

**Solution:**
```
Router# copy running-config startup-config
Router# write memory
```

### Problem: Ping to gateway works but not beyond
**Cause:** Return path not configured on other router

**Solution:**
```
!On the receiving router, add route back to source network
Router2(config)# ip route 192.168.1.0 255.255.255.0 203.0.113.1
```

---

## Static Routing Best Practices

✅ **Do:**
- Document all static routes
- Always configure return paths
- Use default routes for unknown destinations
- Test connectivity after configuration
- Save configuration to startup-config
- Use floating static routes for redundancy

❌ **Don't:**
- Configure overlapping routes
- Forget to configure interface addressing first
- Use wrong subnet masks
- Leave configuration unsaved
- Forget return routes on other routers

---

## Summary

Static routing is:
- Simple and efficient for small networks
- Requires manual configuration
- Best for default routes and specific paths
- Foundation for understanding routing concepts

## Advanced: Multi-Router Static Routing

```
For 3+ routers, ensure bidirectional routes:

Router1 ──────→ Router2 ──────→ Router3
         S0/0/0          S0/0/0

Router1 must know how to reach Router3's network (via Router2)
Router3 must know how to reach Router1's network (via Router2)
Router2 must know about both sides
```

## Next: Dynamic Routing
Move to `02-OSPF-Configuration/` to learn automatic routing discovery.