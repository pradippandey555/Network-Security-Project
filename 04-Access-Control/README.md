# Access Control Lists (ACLs) - Module 4

This module covers Standard ACLs, Extended ACLs, Named ACLs, and ACL best practices.

## Contents

1. **01-Standard-ACLs/** - Basic source IP filtering
2. **02-Extended-ACLs/** - Advanced protocol and port filtering
3. **03-Named-ACLs/** - Named access lists for better management
4. **04-ACL-Best-Practices/** - Security and performance considerations

## Learning Objectives

By the end of this module, you will:
- ✅ Create and apply Standard ACLs
- ✅ Design Extended ACLs with protocol/port filtering
- ✅ Implement Named ACLs
- ✅ Apply ACLs to interfaces
- ✅ Troubleshoot ACL issues
- ✅ Follow ACL best practices

## Duration
**Week 7** of the project timeline

## Prerequisites
- Complete Modules 1-3
- Understanding of IP addresses and subnetting
- Knowledge of TCP/UDP ports
- Basic router configuration

## What Are ACLs?

Access Control Lists are:
- **Ordered rules** - Packets checked against rules in sequence
- **Permit or Deny** - Each rule permits or denies traffic
- **Applied to interfaces** - Can filter inbound or outbound
- **Stateless** - No connection tracking (unlike firewalls)
- **Direction-specific** - Must be applied to both directions for bidirectional filtering

## ACL Types

### Standard ACLs (1-99, 1300-1399)
- Filter by **source IP only**
- Simple and efficient
- Process fewer fields
- Limited functionality

**Example:**
```
access-list 1 permit 192.168.1.0 0.0.0.255
access-list 1 deny 192.168.2.0 0.0.0.255
```

### Extended ACLs (100-199, 2000-2699)
- Filter by **source, destination, protocol, port**
- More complex
- More powerful and flexible
- Higher processing overhead

**Example:**
```
access-list 100 permit tcp 192.168.1.0 0.0.0.255 any eq 80
access-list 100 deny udp any any eq 53
```

### Named ACLs
- Human-readable names
- Easier to manage
- Can be edited without recreating
- Recommended for modern networks

**Example:**
```
ip access-list standard ALLOW_SALES
  permit 192.168.10.0 0.0.0.255
  deny 192.168.20.0 0.0.0.255
  permit any
```

## Packet Tracer Lab Setup

### Network Topology
```
Sales VLAN 10:           IT VLAN 20:              Accounting VLAN 30:
192.168.10.0/24          192.168.20.0/24          192.168.30.0/24
 [PC1]                   [PC2]                    [PC3]
   │                       │                        │
 [R1]──────────────────[R2]──────────────────[R3]

Requirement: Block IT from accessing Accounting via ACL
```

## Common ACL Errors to Avoid

⚠️ **Most Common Mistakes:**

1. **Implicit deny at end** - All packets not explicitly permitted are denied
   ```
   Solution: Always end with "permit any" if you want to allow other traffic
   ```

2. **Wrong wildcard mask** - Inverted from subnet mask
   ```
   Subnet mask:  255.255.255.0
   Wildcard:     0.0.0.255  (NOT the same!)
   ```

3. **Applied to wrong interface** - ACL filters one direction only
   ```
   Solution: May need ACL on both directions or other interface
   ```

4. **Wrong order of rules** - First match wins
   ```
   Wrong:
   access-list 100 deny tcp any any eq 80
   access-list 100 permit tcp 192.168.1.0 0.0.0.255 any eq 80
   
   Right:
   access-list 100 permit tcp 192.168.1.0 0.0.0.255 any eq 80
   access-list 100 deny tcp any any eq 80
   ```

## Summary

ACLs are essential for:
- Network security
- Traffic filtering
- Access control
- QoS implementation

Key concepts:
- **Standard ACLs**: Source IP filtering
- **Extended ACLs**: Protocol and port filtering
- **Named ACLs**: Better management
- **Order matters**: First match wins
- **Implicit deny**: All unmatched traffic denied

## Next Steps

Start with Standard ACLs, progress to Extended, then implement Named ACLs.

After completing this module, proceed to **05-NAT-Configuration** to learn Network Address Translation.