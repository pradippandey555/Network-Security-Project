# Troubleshooting Guide - Common Issues and Solutions

## Network Connectivity Issues

### Problem: Can't ping between PCs on same network

**Symptoms:**
- Ping returns "Destination Host Unreachable"
- Reply timeout
- No response

**Diagnosis Steps:**
```
1. Check if both PCs are connected to same network
   Router# show ip route
   
2. Verify IP addresses are in same subnet
   PC1: 192.168.1.10 / 255.255.255.0 = Network 192.168.1.0
   PC2: 192.168.1.20 / 255.255.255.0 = Network 192.168.1.0 ✓
   
3. Check if switch is configured for VLAN
   Switch# show interfaces Fa0/1 switchport | include VLAN
   
4. Verify interfaces are up
   Router# show interfaces brief
   Switch# show interfaces status
```

**Solutions:**

❌ **Wrong Subnet Mask:**
```
PC1: 192.168.1.10 / 255.255.255.128 = 192.168.1.0/25
PC2: 192.168.1.135 / 255.255.255.128 = 192.168.1.128/25
→ Different subnets! Change mask to 255.255.255.0
```

❌ **Interfaces Down:**
```
Router# show interfaces
FastEthernet0/0 is down, line protocol is down
→ Fix: Router(config-if)# no shutdown
```

❌ **Wrong VLAN Assignment:**
```
Switch# show vlan brief
Fa0/1 is in VLAN 10 but PC is plugged into Fa0/2 (VLAN 20)
→ Fix: Reassign port to correct VLAN
```

✅ **Correct Configuration:**
```
Both PCs same subnet
Both interfaces up
Correct VLAN assignment
ARP resolves MAC addresses
```

---

### Problem: Can't ping between different networks/VLANs

**Symptoms:**
- Ping to router interface works
- Ping to other VLAN fails
- "Network is unreachable"

**Diagnosis:**
```
1. Verify router has subinterfaces configured
   Router# show interfaces | include VLAN
   
2. Check if trunk is configured on switch
   Switch# show interfaces trunk
   
3. Check routing table
   Router# show ip route
   
4. Test with router ping first
   PC1# ping 192.168.20.1 (router VLAN 20 interface)
```

**Solutions:**

❌ **No Subinterface for VLAN:**
```
→ Fix: Create subinterface
Router(config)# interface Fa0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0
```

❌ **Trunk Not Configured:**
```
→ Fix: Configure trunk
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30
```

❌ **ACL Blocking Traffic:**
```
→ Check: Router# show access-lists
→ If ACL denies traffic, modify or remove
```

---

## Routing Issues

### Problem: Static route not working

**Symptoms:**
- Added route but traffic doesn't flow
- Packets don't reach destination
- "No route to host"

**Diagnosis:**
```
1. Verify route exists
   Router1# show ip route
   S 10.0.0.0/24 [1/0] via 203.0.113.2
   
2. Check if interface to gateway is up
   Router1# show interfaces Serial0/0/0 | include up
   
3. Ping the gateway address
   Router1# ping 203.0.113.2
   
4. Check return route on other router
   Router2# show ip route | include 192.168.1.0
```

**Solutions:**

❌ **Missing Return Route:**
```
Router1: 192.168.1.0/24 ← Router2
Router2: Missing route to 192.168.1.0

→ Fix on Router2:
Router2(config)# ip route 192.168.1.0 255.255.255.0 203.0.113.1
```

❌ **Wrong Next Hop:**
```
Router1(config)# ip route 10.0.0.0 255.255.255.0 203.0.113.2
But Serial0/0/0 on other side has IP 203.0.113.1

→ Check: Router2# show interfaces Serial0/0/0
→ Use correct IP as next hop
```

❌ **Interface Down:**
```
Serial0/0/0 is down
→ Activate: Router(config-if)# no shutdown
→ Check clock rate (if DCE): Router(config-if)# clock rate 128000
```

---

### Problem: OSPF neighbors not forming

**Symptoms:**
- Routes not learned
- "No OSPF neighbors" in show output
- Network unreachable

**Diagnosis:**
```
1. Check OSPF is enabled
   Router# show ip ospf
   Router# show ip ospf process
   
2. Check interface status
   Router# show ip ospf interface brief
   
3. Check process ID matches
   Router1: router ospf 1
   Router2: router ospf 1 ✓ (must match)
   
4. Check networks advertised
   Router# show ip ospf database
   
5. Verify networks are in OSPF
   Router# show run | include network
```

**Solutions:**

❌ **Wrong Process ID:**
```
Router1: router ospf 1
Router2: router ospf 2

→ Must use same process ID:
Router2(config)# router ospf 1
```

❌ **Network Not Advertised:**
```
Router(config-router)# network 192.168.1.0 0.0.0.255 area 0
Must be enabled for OSPF to work
```

❌ **Interface Down:**
```
→ Check: Router# show interfaces Fa0/0
→ Fix: Router(config-if)# no shutdown
```

❌ **ACL Blocking OSPF:**
```
OSPF uses IP protocol 89
→ Check ACL allows: permit ospf any any
→ Or: permit ip any any
```

---

## ACL Issues

### Problem: ACL not filtering traffic

**Symptoms:**
- Traffic passes even with ACL applied
- Denied traffic still flows
- ACL ineffective

**Diagnosis:**
```
1. Verify ACL exists
   Router# show access-lists
   
2. Check applied to interface
   Router# show ip interface Fa0/0 | include access list
   
3. Check direction (in/out)
   Router# show run | include access-group
   
4. Test with debug
   Router# debug ip packet detail
```

**Solutions:**

❌ **ACL Applied to Wrong Interface:**
```
Intended: Fa0/0 (LAN side)
Actual: Fa0/1 (WAN side)

→ Apply to correct interface
Router(config)# interface Fa0/0
Router(config-if)# ip access-group 100 in
```

❌ **Wrong Direction:**
```
Want to filter inbound traffic
Applied outbound (out instead of in)

→ Fix: Remove and reapply
Router(config-if)# no ip access-group 100 out
Router(config-if)# ip access-group 100 in
```

❌ **Implicit Deny Allows Traffic:**
```
access-list 100 permit tcp 192.168.1.0 0.0.0.255 any eq 80
(implicit deny any any at end)

Traffic not matching allowed rule is denied ✓
But if need other traffic: add permit any at end
```

---

## NAT Issues

### Problem: NAT translation not working

**Symptoms:**
- No addresses translated
- Internal traffic not reaching external
- "No translations" in show output

**Diagnosis:**
```
1. Check NAT configuration
   Router# show ip nat translations
   Router# show ip nat statistics
   
2. Verify inside/outside interfaces
   Router# show run | include "ip nat"
   
3. Check ACL for NAT
   Router# show access-lists
   
4. Test with debug
   Router# debug ip nat
```

**Solutions:**

❌ **Interfaces Not Marked:**
```
Missing: ip nat inside / ip nat outside

→ Fix:
Router(config)# interface Fa0/0
Router(config-if)# ip nat inside
Router(config)# interface Serial0/0/0
Router(config-if)# ip nat outside
```

❌ **ACL Doesn't Match Traffic:**
```
ACL: permit ip 192.168.1.0 0.0.0.255 any
But traffic from 192.168.2.0 not matched

→ Fix ACL to include all networks to be translated
```

❌ **Default Route Missing:**
```
No route to outside network

→ Add default route:
Router(config)# ip route 0.0.0.0 0.0.0.0 203.0.113.1
```

---

## Firewall Issues

### Problem: Firewall blocking legitimate traffic

**Symptoms:**
- Users can't access needed services
- Web pages load slowly
- Some protocols don't work

**Diagnosis:**
```
1. Check firewall rules
   ASA# show access-list
   ASA# show access-group
   
2. Review logs
   ASA# show logging
   
3. Check interface security levels
   ASA# show interface
   
4. Verify NAT rules
   ASA# show nat
```

**Solutions:**

❌ **Overly Restrictive Rules:**
```
Deny all by default (✓ good)
But forgot to permit HTTP/HTTPS

→ Add permit rules for needed services:
access-list OUTSIDE_IN permit tcp any 172.16.1.0 255.255.255.0 eq 80
access-list OUTSIDE_IN permit tcp any 172.16.1.0 255.255.255.0 eq 443
```

❌ **Wrong Security Zone:**
```
DMZ to Inside blocked
But web server needs database access

→ Adjust firewall zone rules
```

❌ **Stateful Inspection Issues:**
```
Return traffic from outside not allowed

→ Enable stateful inspection:
ASA(config)# inspect all (or specific protocols)
```

---

## VPN Issues

### Problem: VPN tunnel won't come up

**Symptoms:**
- Tunnel shows as "down"
- IKE negotiation fails
- Phase 1 or Phase 2 fails

**Diagnosis:**
```
1. Check IKE Phase 1
   Router# show crypto isakmp sa
   
2. Check IPSec Phase 2
   Router# show crypto ipsec sa brief
   
3. Check crypto map
   Router# show crypto map
   
4. Verify connectivity to peer
   Router# ping [VPN_peer_IP]
```

**Solutions:**

❌ **Pre-shared Keys Don't Match:**
```
Router1: crypto isakmp key MyKey123 address 203.0.113.2
Router2: crypto isakmp key DifferentKey address 203.0.113.1

→ Must match on both sides!
```

❌ **Transform Sets Don't Match:**
```
Router1: esp-aes esp-sha-hmac
Router2: esp-3des esp-md5

→ Must be identical:
Both: crypto ipsec transform-set VPN-TRANSFORM esp-aes 256 esp-sha-hmac
```

❌ **Crypto ACL Mismatch:**
```
Router1: access-list 100 permit ip 192.168.1.0 0.0.0.255 10.0.0.0 0.0.0.255
Router2: access-list 100 permit ip 10.0.0.0 0.0.0.255 192.168.1.0 0.0.0.255

→ Source and destination reversed on one side!
```

---

## Packet Tracer Specific Issues

### Problem: Devices can't communicate in Packet Tracer

**Common Causes:**
1. Interfaces not activated (no shutdown)
2. Cables not connected or wrong cable type
3. IP addresses not configured
4. Switch mode (default: dynamic) vs access mode
5. VLAN not created on switch

**Solutions:**
```
1. Verify cables connected
   - Fa0/0 to Fa0/0 (router to switch)
   - S0/0/0 to S0/0/0 (router to router - requires DCE/DTE)
   - Fa0/1 to Fa0/1 (PC to switch)

2. Check interface mode
   Switch# show interfaces Fa0/1 switchport | include mode
   Should be: Operational Mode: static access

3. Verify no shutdown
   Router# show interfaces brief
   Should show: up  up (not down down)

4. Use Simulation Mode
   - Click "Simulation" tab
   - Send ping and watch packets
   - See where packets get lost
```

---

## Performance Issues

### Problem: Network is slow

**Diagnosis:**
```
1. Check interface utilization
   Router# show interfaces | include "input rate"
   
2. Check for packet loss
   Router# ping -c 100 [target] (count packets)
   Check % loss
   
3. Check CPU usage
   Router# show processes cpu
   Look for high CPU processes
   
4. Check for congestion
   - ACL processing overhead
   - Suboptimal routing
   - Broadcast storms (spanning tree loop?)
```

**Solutions:**

❌ **Broadcast Storm:**
```
→ Check for STP loop
Switch# show spanning-tree
Verify root bridge and port states
```

❌ **High CPU Due to ACL:**
```
→ Move ACL to more efficient location
→ Use named ACLs for better management
→ Simplify ACL rules
```

❌ **Suboptimal Routing:**
```
→ Check routing table
Router# show ip route
→ Verify primary route is best metric
→ Check for floating static routes
```

---

## General Troubleshooting Methodology

### 1. **Define the Problem**
- What's not working?
- When did it start?
- Who is affected?
- What changed?

### 2. **Gather Information**
```
show running-config
show interfaces brief
show ip route
show ip address
show logs
```

### 3. **Isolate the Layer**
- Layer 1 (Physical): Cables, interfaces
- Layer 2 (Data Link): VLANs, MAC addresses
- Layer 3 (Network): IP addresses, routing
- Layer 4 (Transport): Ports, protocols

### 4. **Test Hypothesis**
```
ping (Layer 3)
tracert (Routing path)
telnet [IP] [port] (Layer 4)
show access-lists (Filtering)
```

### 5. **Implement Solution**
- Make one change at a time
- Document changes
- Test after each change

### 6. **Verify and Document**
- Confirm problem solved
- Document solution
- Update configurations
- Backup configuration

---

## Quick Reference: Essential Commands

```bash
# Connectivity Testing
ping [IP]                           # Test layer 3
tracert [IP]                        # Trace route path
telnet [IP] [PORT]                  # Test layer 4
show ip interface brief             # Quick status

# Configuration Verification
show running-config                 # Current config
show startup-config                 # Boot config
show ip route                       # Routing table
show interfaces [interface]         # Interface details
show vlan brief                     # VLAN summary

# ACL and NAT
show access-lists                   # All ACLs
show ip nat translations            # NAT translations
show ip nat statistics              # NAT stats

# Routing Protocols
show ip ospf neighbors              # OSPF neighbors
show ip eigrp neighbors             # EIGRP neighbors
show ip bgp summary                 # BGP status

# Debugging
debug ip packet detail              # IP packet debug
debug ip routing                    # Routing debug
debug ip nat                        # NAT debug
undebug all                         # Stop all debugging
```

## When to Ask for Help

✅ **You've tried troubleshooting basics and still stuck**
- Verified physical layer
- Checked configurations
- Reviewed logs
- Tested connectivity

✅ **You have supporting information ready**
- Running-config files
- Output of show commands
- Topology diagram
- Description of what's not working
- Changes made before issue occurred

---

## Summary

Most network issues fall into these categories:
1. **Physical Layer**: Cables, power, interfaces down
2. **Configuration**: Wrong IP addresses, missing routes
3. **Routing**: Routes not advertised, wrong next hop
4. **Filtering**: ACLs, firewall rules blocking traffic
5. **Mismatch**: Settings don't match between devices

Always start with basics:
- Are devices powered on?
- Are cables connected?
- Are interfaces up?
- Are IP addresses configured?
- Are routes in place?

Then work toward more complex issues with systematic testing.