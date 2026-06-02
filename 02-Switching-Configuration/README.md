# Switching Configuration - Module 2

This module covers VLAN setup, Spanning Tree Protocol, port security, and trunk configuration.

## Contents

1. **01-VLAN-Setup/** - Virtual LAN configuration for network segmentation
2. **02-STP-Configuration/** - Spanning Tree Protocol for loop prevention
3. **03-Port-Security/** - MAC address filtering and port security
4. **04-Trunk-Configuration/** - Inter-switch link configuration

## Learning Objectives

By the end of this module, you will:
- ✅ Create and configure VLANs on switches
- ✅ Configure trunk ports for inter-VLAN communication
- ✅ Implement Spanning Tree Protocol to prevent loops
- ✅ Secure switch ports with MAC address filtering
- ✅ Configure inter-VLAN routing

## Duration
**Weeks 3-4** of the project timeline

## Prerequisites
- Complete Module 1 (Network Fundamentals)
- Understanding of IP addressing and subnetting
- Basic knowledge of Packet Tracer

## Key Concepts

### VLANs (Virtual Local Area Networks)
- Logical network segmentation
- Multiple broadcast domains on single switch
- Improved security and performance

### Spanning Tree Protocol (STP)
- Prevents switching loops
- Provides redundant paths
- Automatic failover

### Port Security
- Controls which MAC addresses can access port
- Prevents unauthorized access
- Protects against MAC floods

### Trunk Ports
- Carry traffic for multiple VLANs
- Use VLAN tags (802.1Q) to identify traffic
- Connect switches together

## Packet Tracer Lab Topology

```
        [PC1] ──────────────────────────── [PC2]
         │                                   │
      VLAN 10                            VLAN 10
         │                                   │
      [Switch1] ──── Trunk ──── [Switch2] ──────── [Router]
         │                         │
      [PC3]                      [PC4]
      VLAN 20                   VLAN 20
```

## Next Steps

Start with VLAN-Setup and work through each section sequentially.

## Getting Help

Each section includes:
- Step-by-step configuration guides
- Verification commands
- Troubleshooting tips
- Lab exercises

After completing this module, proceed to **03-Routing-Protocols** to learn about dynamic routing.