# Network Segmentation - Module 7

This module covers DMZ Setup, Zero Trust Architecture, and Microsegmentation.

## Contents

1. **01-DMZ-Setup/** - Creating demilitarized zones
2. **02-Zero-Trust-Architecture/** - Never trust, always verify
3. **03-Micro-Segmentation/** - Network isolation at scale

## Learning Objectives

By the end of this module, you will:
- ✅ Design and implement DMZ networks
- ✅ Understand Zero Trust security model
- ✅ Implement microsegmentation
- ✅ Create isolated security zones
- ✅ Control inter-zone traffic
- ✅ Monitor zone boundaries

## Duration
**Week 11** of the project timeline

## Prerequisites
- Complete Modules 1-6
- Understanding of VLANs and ACLs
- Firewall knowledge
- Network design concepts

## DMZ (Demilitarized Zone)

### Definition
A **DMZ** is a network segment that contains and exposes external-facing services while shielding the internal network from direct exposure.

### Why DMZ?

```
Without DMZ (BAD):
Internet → [Firewall] → All servers on internal network
                        (If breached, attacker inside)

With DMZ (GOOD):
Internet → [Firewall] → DMZ [Web, Mail, DNS]
                         ↓ [Firewall]
                       Internal Network
                       (Multiple layers)
```

### DMZ Architecture

```
                    Internet
                       │
              ┌────────▼────────┐
              │ External Firewall│
              │   (Stateful)     │
              └────────┬────────┘
                       │ Fa0/0 (Outside)
                ┌──────▼──────┐
                │   DMZ VLAN  │
                │  172.16.0/24│
                └──────┬──────┘
          ┌────────────┼────────────┐
          │            │            │
      ┌───▼──┐    ┌────▼────┐ ┌───▼──┐
      │ Web  │    │  Mail   │ │ DNS  │
      │Server│    │ Server  │ │Server│
      └───┬──┘    └────┬────┘ └───┬──┘
          │            │          │
              ┌────────▼──────────┐
              │ Internal Firewall │
              └────────┬──────────┘
                       │ Fa0/1 (Inside)
                ┌──────▼──────────┐
                │ Corporate LAN  │
                │ 192.168.0/16   │
                └────────────────┘
```

### DMZ Rules

**Outside → DMZ:**
- ✅ HTTP (80) to Web Server
- ✅ HTTPS (443) to Web Server
- ✅ SMTP (25) to Mail Server
- ✅ DNS (53) to DNS Server
- ❌ Everything else denied

**DMZ → Outside:**
- ✅ All return traffic
- ✅ SMTP (25) to external servers
- ✅ NTP (123) for time sync
- ❌ Unsolicited outbound blocked

**DMZ → Inside:**
- ✅ Database queries (3306 for MySQL, 1433 for MSSQL)
- ✅ LDAP (389) for authentication
- ❌ Remote access blocked
- ❌ File sharing blocked
- ❌ Administrative access blocked

**Inside → DMZ:**
- ✅ All return traffic
- ✅ Management traffic (SSH 22, Telnet 23)
- ✅ Updates and patches

## Zero Trust Architecture

### Principles

1. **Never Trust, Always Verify**
   - No implicit trust based on location
   - Every access request must be authenticated
   - Continuous verification

2. **Assume Breach**
   - Assume adversary is inside network
   - Design for containment
   - Segment by default

3. **Principle of Least Privilege**
   - Users/devices get minimal required access
   - Remove unnecessary permissions
   - Grant time-limited access

4. **Verify Explicitly**
   - Use all data points for authentication
   - Device health, user identity, location
   - Behavioral analysis

### Zero Trust Model

```
┌──────────────┐
│   User/Device│  → Verify identity (MFA)
└──────┬───────┘     Verify device (health check)
       │              Verify location (geo-fencing)
       │              Verify time (access hours)
       ▼
┌──────────────────────────────┐
│   Authentication System       │
│   (Identity Provider)         │
│   - MFA                       │
│   - Device compliance check   │
│   - Behavioral analysis       │
└──────────────┬───────────────┘
               │
          ┌────▼────┐
          │ Approved?│
          └────┬────┘
          Yes /│\ No
              │ │
        ┌─────▼─┴─────┐
        │             │
    ┌───▼────┐  ┌────▼────┐
    │ Grant  │  │  Deny   │
    │ Access │  │ & Alert │
    │ Token  │  │         │
    └───┬────┘  └────────┘
        │
    ┌───▼──────────────────┐
    │ Access Resource      │
    │ with encrypted token │
    │ (continuous monitor) │
    └────────────────────┘
```

## Microsegmentation

### Definition
Microsegmentation divides networks into small, secure zones to maintain separate access for different parts of the network.

### Implementation Levels

**Level 1: VLAN Segmentation**
```
┌──────────────────────────────┐
│       Network Switch         │
├──────────────────────────────┤
│ VLAN 10 │ VLAN 20 │ VLAN 30│
│ (Sales) │  (IT)   │(Account)│
└──────────────────────────────┘

Traffic between VLANs controlled by router ACLs
```

**Level 2: Subnet Segmentation**
```
10.0.0.0/16
├─ 10.1.0.0/24 (Finance Department)
├─ 10.2.0.0/24 (HR Department)
├─ 10.3.0.0/24 (Engineering)
└─ 10.4.0.0/24 (Guest Network)

Each subnet has firewall rules
```

**Level 3: Application Segmentation**
```
Finance Department Subnet
├─ Group 1: Accounting Software (specific ports)
├─ Group 2: CRM System (specific ports)
├─ Group 3: Workstations (limited internet)
└─ Group 4: Printers (LPD port only)

Each group has different access rules
```

**Level 4: Individual Host Segmentation**
```
Host-based Firewalls on Each Computer
├─ Firewall profiles per user
├─ Firewall rules per application
├─ Outbound filtering
└─ Process monitoring
```

### Microsegmentation Benefits

```
┌─────────────────────────────────────────┐
│   If one system is compromised...       │
└─────────────────────────────────────────┘

Without Segmentation:
  Breach → Internal network access → Company-wide disaster

With Microsegmentation:
  Breach → Contained to segment → Limited lateral movement
           → Firewall rules block access → System isolated
           → Alert triggered → Incident response
           → Business continues
```

## Implementation Guide

### Step 1: Map Network Assets
```
Document:
- All servers and their functions
- User groups and departments
- Data classifications
- Trust relationships
- Communication requirements
```

### Step 2: Define Security Zones
```
Zone 1: Untrusted (Internet)
Zone 2: DMZ (Public Services)
Zone 3: Corporate (Internal Users)
Zone 4: Sensitive (Finance, HR)
Zone 5: Critical (Database, Backup)
Zone 6: Management (Admin Access)
```

### Step 3: Define Traffic Flows
```
Document:
- Which zones communicate
- What protocols/ports
- In which direction
- Under what conditions
```

### Step 4: Implement Firewall Rules
```
For each zone boundary:
- Default deny
- Explicit permit statements
- Logging enabled
- Regular review schedule
```

### Step 5: Monitor and Adjust
```
Continuous:
- Monitor traffic patterns
- Alert on anomalies
- Review logs weekly
- Adjust rules as needed
- Test failover scenarios
```

## Segmentation in Packet Tracer

```
                    Router1 (Gateway)
                  /      |       \      \
                 /       |        \      \
            Fa0/0   Fa0/1    Fa0/2   Fa0/3
             |        |        |        |
          [SW1]    [SW2]    [SW3]    [SW4]
         VLAN 10  VLAN 20  VLAN 30  VLAN 99
         (Sales) (IT)    (Account) (Mgmt)
             |       |        |        |
          [PC1]   [PC2]    [PC3]   [Admin]

Firewall rules between VLANs:
- Sales ←→ IT: Permit specific ports
- Sales → Accounting: Deny
- IT ↔ Accounting: Database only (port 3306)
- All → Management: Deny (direct access only to management VLAN devices)
```

## Verification Commands

```
# View VLAN configuration
Switch# show vlan brief
Switch# show ip interface brief

# Check ACLs
Router# show access-lists
Router# show ip interface Fa0/0 | include access list

# Test connectivity
PC1# ping 10.2.0.10 (should fail if blocked)
Router# ping 192.168.1.1 (test from router)

# Trace packet path
Router# tracert 10.2.0.10

# Check firewall rules
Firewall# show access-group
Firewall# show policy-map
```

## Summary

**DMZ:**
- Isolates public-facing services
- Reduces exposure of internal network
- First line of defense

**Zero Trust:**
- No implicit trust
- Always verify
- Continuous monitoring

**Microsegmentation:**
- Divides network into small zones
- Limits lateral movement
- Improves visibility
- Enables rapid response

## Progression

1. Start with DMZ (separate public/private)
2. Add VLAN segmentation (department-level)
3. Implement subnet segmentation (team-level)
4. Add application segmentation (service-level)
5. Deploy host-based controls (individual-level)
6. Implement Zero Trust principles (continuous verification)

## Next Steps

After completing this module, proceed to **08-Lab-Exercises** for comprehensive hands-on practice.