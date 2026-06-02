# NAT Configuration - Module 5

This module covers Network Address Translation (Static NAT, Dynamic NAT, and PAT).

## Contents

1. **01-Static-NAT/** - One-to-one IP address mapping
2. **02-Dynamic-NAT/** - Many-to-many address mapping
3. **03-PAT-Configuration/** - Port Address Translation (overload)
4. **04-NAT-Troubleshooting/** - Debugging and verification

## Learning Objectives

By the end of this module, you will:
- ✅ Understand NAT concepts and terminology
- ✅ Configure Static NAT for server access
- ✅ Implement Dynamic NAT for internal networks
- ✅ Setup PAT for efficient IP usage
- ✅ Troubleshoot NAT issues
- ✅ Verify NAT translations

## Duration
**Week 8** of the project timeline

## Prerequisites
- Complete Modules 1-4
- Understanding of IP addressing
- Knowledge of inside/outside networks
- Basic router configuration

## What is NAT?

Network Address Translation:
- **Translates private IPs to public IPs** for internet access
- **Hides internal network** from external view
- **Enables IP address reuse** (many devices share one public IP)
- **Provides basic security** through address hiding
- **Required for internet access** in most corporate networks

## NAT Terminology

### Inside and Outside
- **Inside Local**: Private IP address (10.0.0.0, 172.16.0.0, 192.168.0.0)
- **Inside Global**: Public IP used to represent inside address
- **Outside Local**: Address of outside host as seen from inside
- **Outside Global**: Real address of outside host

## NAT Types

### Static NAT (1:1 Mapping)
- One private IP → One public IP
- Always same translation
- Used for servers accessed from internet
- Example: Web server at 192.168.1.50 → 203.0.113.50

### Dynamic NAT (Many:Many)
- Multiple private IPs → Pool of public IPs
- Translation allocated from pool
- IP released when connection closes
- Used for large networks

### Port Address Translation (PAT)
- Multiple private IPs → One public IP
- Uses different ports for each connection
- Most efficient ("overload")
- Used in most home/small business routers
- Example: 10 PCs all use 203.0.113.1 with different ports

## Key Concepts

### Inside Interface
```
router(config)# interface FastEthernet 0/0
router(config-if)# ip nat inside
```

### Outside Interface
```
router(config)# interface Serial 0/0/0
router(config-if)# ip nat outside
```

### NAT Configuration Steps
1. Define inside and outside interfaces
2. Create access list (what to translate)
3. Define translation (static, dynamic, or PAT)
4. Apply to interfaces

## Packet Tracer Lab Topology

```
Internal Network          NAT Router          Internet
192.168.1.0/24           (Router)            203.0.113.0/24

[PC1]                                        [Server1]
10.1.1.10      ┌──────────────┐            203.0.113.100
[PC2]          │ Fa0/0 │ S0/0/0│           [Server2]
10.1.1.11      │  (in) │(out) │            203.0.113.101
[PC3]          │              │
10.1.1.12      └──────────────┘

Static NAT: PC1 (10.1.1.10) ↔ 203.0.113.10
Dynamic NAT: PC2,PC3 use pool 203.0.113.50-203.0.113.60
PAT: All IPs can use 203.0.113.1 with different ports
```

## Common NAT Scenarios

### Scenario 1: Small Office Remote Access
```
Inside: 192.168.1.0/24
Outside: ISP-assigned IP (changes)
Solution: Use PAT for all outbound traffic
```

### Scenario 2: Web Server Access
```
Inside: 192.168.1.100 (web server)
Outside: 203.0.113.50
Solution: Static NAT for consistent external access
```

### Scenario 3: Large Enterprise Internet Access
```
Inside: 10.0.0.0/8 (many networks)
Outside: Pool 203.0.113.0/28 (16 addresses)
Solution: Dynamic NAT or PAT
```

## Verification Commands

```
show ip nat statistics              # NAT status
show ip nat translations            # Active translations
show ip nat translations verbose    # Detailed translations
debug ip nat                        # Real-time NAT activity
clear ip nat translations *         # Clear all translations
```

## Troubleshooting Tips

### Inside devices can't reach outside
1. Check interfaces marked as inside/outside
2. Verify ACL permits traffic to be translated
3. Confirm default route to outside network
4. Check NAT translation table

### Outside can't reach inside server
1. Verify static NAT is configured
2. Check return route on outside network
3. Verify firewall isn't blocking
4. Ensure static NAT has correct mapping

### Translation performance issues
1. Monitor CPU usage during translations
2. Check if insufficient pool addresses
3. Verify ACL isn't too broad (translating unnecessary traffic)
4. Consider PAT instead of dynamic NAT

## Summary

NAT enables:
- Private networks to use internet
- Address hiding for security
- Efficient IP address usage
- Multiple devices behind one public IP

Choose NAT type based on:
- **Static**: Need consistent external IP
- **Dynamic**: Need multiple external IPs
- **PAT**: Want to maximize address efficiency

## Next Steps

After completing NAT configuration, proceed to **06-Security-Implementation** to learn about firewalls, VPNs, and intrusion detection.