# Routing Protocols - Module 3

This module covers static routing, OSPF, EIGRP, and BGP routing protocols.

## Contents

1. **01-Static-Routing/** - Manual route configuration
2. **02-OSPF-Configuration/** - Open Shortest Path First dynamic routing
3. **03-EIGRP-Setup/** - Enhanced Interior Gateway Routing Protocol
4. **04-BGP-Implementation/** - Border Gateway Protocol for ISP routing

## Learning Objectives

By the end of this module, you will:
- ✅ Configure static routes
- ✅ Implement OSPF in single and multi-area networks
- ✅ Configure EIGRP with proper AS numbers
- ✅ Understand BGP basics
- ✅ Verify and troubleshoot routing

## Duration
**Weeks 5-6** of the project timeline

## Prerequisites
- Complete Modules 1-2
- Understanding of IP addressing
- Basic router configuration knowledge

## Routing Fundamentals

### Static Routes
- Manually configured
- No automatic updates
- Best for small networks or default routes
- Command: `ip route destination mask gateway`

### Dynamic Routing Protocols
- Automatically discover routes
- Adapt to network changes
- Suitable for larger networks
- Three main types: IGP (RIP, OSPF, EIGRP) and EGP (BGP)

## Comparison Table

| Feature | Static | OSPF | EIGRP | BGP |
|---------|--------|------|-------|-----|
| Configuration | Simple | Medium | Medium | Complex |
| Scalability | Small | Large | Large | Very Large |
| Convergence | Manual | Fast | Very Fast | Slow |
| Bandwidth | Minimal | Medium | Medium | Heavy |
| Administrator | Manual | Easy | Easy | Complex |
| Best For | Default routes | ISP backbones | Enterprise | Internet |

## Packet Tracer Topologies

### OSPF Multi-Area Network
```
Area 0 (Backbone)
┌─────────────────────────┐
│                         │
[R1] ─── S0/0/0 ─── [R2] ─── S0/0/1 ─── [R3]
 │ Fa0/0              │ Fa0/0              │ Fa0/0
 [PC1]          (Area 0)(Area 1)      [PC3]
             Area 0 (Backbone)
             Other Areas
```

### EIGRP Single AS
```
        AS 100
[PC1]         [PC2]         [PC3]
 │             │             │
[R1]────[R2]────[R3]
 EIGRP Network 10.0.0.0/8
```

## Key Commands Summary

### OSPF
```
router ospf 1                    # Enable OSPF process 1
router-id 1.1.1.1              # Set router ID
network 192.168.1.0 0.0.0.255 area 0  # Add network to OSPF
show ip ospf neighbors          # Verify neighbors
show ip route ospf              # View OSPF routes
```

### EIGRP
```
router eigrp 100               # Enable EIGRP AS 100
network 10.0.0.0              # Add network
no auto-summary                # Disable auto-summarization
show ip eigrp neighbors        # Verify neighbors
show ip route eigrp            # View EIGRP routes
```

## Next Steps

Start with Static Routing to understand basics, then progress to dynamic protocols.

After completing this module, proceed to **04-Access-Control** to learn about ACLs.