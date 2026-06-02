# VLAN Setup - Step-by-Step Guide for Packet Tracer

## What is a VLAN?

A **Virtual Local Area Network (VLAN)** is a logical network that groups devices together regardless of physical location. It:
- Creates multiple broadcast domains on one switch
- Improves network performance and security
- Allows logical organization of departments
- Works with IP subnetting

## Why Use VLANs?

1. **Security** - Isolate sensitive departments
2. **Performance** - Reduce broadcast traffic
3. **Management** - Organize by department, function, or security level
4. **Flexibility** - Move devices without re-cabling
5. **Cost** - Use existing switches instead of separate hardware

---

## Packet Tracer VLAN Lab Setup

### Step 1: Create VLANs on Switch1

```
Switch1> enable
Switch1# configure terminal
Switch1(config)# vlan 10
Switch1(config-vlan)# name Sales
Switch1(config-vlan)# exit

Switch1(config)# vlan 20
Switch1(config-vlan)# name IT
Switch1(config-vlan)# exit

Switch1(config)# vlan 30
Switch1(config-vlan)# name Accounting
Switch1(config-vlan)# exit

Switch1(config)# vlan 99
Switch1(config-vlan)# name Management
Switch1(config-vlan)# exit
```

**Verify VLANs created:**
```
Switch1# show vlan brief

VLAN Name                             Status    Ports
---- -------------------------------- --------- -------------------------------
1    default                          active    Fa0/1, Fa0/2, Fa0/3, Fa0/4
10   Sales                            active    
20   IT                               active    
30   Accounting                       active    
99   Management                       active    
```

### Step 2: Assign Ports to VLANs

```
!--- Ports 1-8 assigned to VLAN 10 (Sales)
Switch1(config)# interface range FastEthernet 0/1-8
Switch1(config-if-range)# switchport mode access
Switch1(config-if-range)# switchport access vlan 10
Switch1(config-if-range)# exit

!--- Ports 9-16 assigned to VLAN 20 (IT)
Switch1(config)# interface range FastEthernet 0/9-16
Switch1(config-if-range)# switchport mode access
Switch1(config-if-range)# switchport access vlan 20
Switch1(config-if-range)# exit

!--- Ports 17-24 assigned to VLAN 30 (Accounting)
Switch1(config)# interface range FastEthernet 0/17-24
Switch1(config-if-range)# switchport mode access
Switch1(config-if-range)# switchport access vlan 30
Switch1(config-if-range)# exit
```

### Step 3: Configure Trunk Port to Router

```
!--- Port 24 is trunk port connecting to router
Switch1(config)# interface FastEthernet 0/24
Switch1(config-if)# switchport mode trunk
Switch1(config-if)# switchport trunk native vlan 99
Switch1(config-if)# switchport trunk allowed vlan 10,20,30,99
Switch1(config-if)# description Link to Router
Switch1(config-if)# no shutdown
Switch1(config-if)# exit
```

### Step 4: Configure VLAN SVI (Switched Virtual Interface)

```
!--- VLAN 10 SVI (Gateway for Sales)
Switch1(config)# interface vlan 10
Switch1(config-if)# ip address 192.168.10.250 255.255.255.0
Switch1(config-if)# description Sales VLAN Gateway
Switch1(config-if)# no shutdown
Switch1(config-if)# exit

!--- VLAN 20 SVI (Gateway for IT)
Switch1(config)# interface vlan 20
Switch1(config-if)# ip address 192.168.20.250 255.255.255.0
Switch1(config-if)# description IT VLAN Gateway
Switch1(config-if)# no shutdown
Switch1(config-if)# exit

!--- VLAN 30 SVI (Gateway for Accounting)
Switch1(config)# interface vlan 30
Switch1(config-if)# ip address 192.168.30.250 255.255.255.0
Switch1(config-if)# description Accounting VLAN Gateway
Switch1(config-if)# no shutdown
Switch1(config-if)# exit
```

### Step 5: Configure Router for Inter-VLAN Routing

**Router Configuration (Router-on-a-Stick):**

```
Router(config)# interface FastEthernet 0/0
Router(config-if)# no shutdown
Router(config-if)# exit

!--- Create subinterfaces for each VLAN
Router(config)# interface FastEthernet 0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0
Router(config-subif)# description Sales VLAN Router Gateway
Router(config-subif)# exit

Router(config)# interface FastEthernet 0/0.20
Router(config-subif)# encapsulation dot1Q 20
Router(config-subif)# ip address 192.168.20.1 255.255.255.0
Router(config-subif)# description IT VLAN Router Gateway
Router(config-subif)# exit

Router(config)# interface FastEthernet 0/0.30
Router(config-subif)# encapsulation dot1Q 30
Router(config-subif)# ip address 192.168.30.1 255.255.255.0
Router(config-subif)# description Accounting VLAN Router Gateway
Router(config-subif)# exit
```

### Step 6: Configure PCs with VLAN IP Addresses

**PC1 in VLAN 10 (Sales):**
- IP Address: 192.168.10.10
- Subnet Mask: 255.255.255.0
- Default Gateway: 192.168.10.1 (Router)
- DNS Server: 8.8.8.8

**PC2 in VLAN 20 (IT):**
- IP Address: 192.168.20.10
- Subnet Mask: 255.255.255.0
- Default Gateway: 192.168.20.1 (Router)
- DNS Server: 8.8.8.8

**PC3 in VLAN 30 (Accounting):**
- IP Address: 192.168.30.10
- Subnet Mask: 255.255.255.0
- Default Gateway: 192.168.30.1 (Router)
- DNS Server: 8.8.8.8

---

## Verification Commands

### Check VLAN Configuration
```
Switch# show vlan brief
Switch# show vlan id 10
Switch# show interfaces vlan 10
```

### Check Port Assignments
```
Switch# show interfaces FastEthernet 0/1 switchport
Switch# show port-security
```

### Check Trunk Status
```
Switch# show interfaces trunk
Switch# show interfaces FastEthernet 0/24 trunk
```

### Test Inter-VLAN Connectivity
```
PC1# ping 192.168.20.10  (Should succeed - router routes between VLANs)
PC1# ping 192.168.30.10  (Should succeed)
PC2# ping 192.168.10.10  (Should succeed)
```

---

## Troubleshooting VLAN Issues

### Problem: PCs in same VLAN can't communicate
**Solution:**
```
1. Verify port is assigned to correct VLAN
   Switch# show interfaces Fa0/1 switchport | include Access VLAN

2. Check if port is in err-disabled state
   Switch# show interfaces Fa0/1 status

3. Verify IP addressing on both PCs
   (Should be same subnet)
```

### Problem: PCs in different VLANs can't communicate
**Solution:**
```
1. Verify trunk port is configured
   Switch# show interfaces trunk

2. Check if all VLANs are allowed on trunk
   Switch# show interfaces Fa0/24 trunk | include allowed

3. Verify router subinterfaces are configured
   Router# show interfaces brief | include 0/0

4. Test with ping
   PC1# ping 192.168.20.1 (Router interface)
```

### Problem: Trunk not forming
**Solution:**
```
1. Verify both sides are configured as trunk
   Switch1# show interfaces Fa0/24 switchport | include Operational Mode
   Switch2# show interfaces Fa0/24 switchport | include Operational Mode

2. Check if native VLAN matches
   Switch# show interfaces Fa0/24 trunk | include Native

3. Verify encapsulation (should be 802.1Q)
   Switch# show interfaces Fa0/24 trunk | include Encapsulation
```

---

## VLAN Best Practices

✅ **Do:**
- Create separate VLANs for different departments
- Use descriptive VLAN names
- Document VLAN assignments
- Use VLAN 1 only for management (not data)
- Implement VLAN access control lists (VACLs)

❌ **Don't:**
- Mix too many devices in one VLAN
- Use VLAN 1 for data traffic
- Forget to configure default gateway on PC
- Mix static and dynamic VLAN assignment

---

## Summary

VLANs are essential for:
- Network segmentation and security
- Performance optimization
- Logical organization
- Scalability

With proper VLAN configuration, you can:
- Isolate broadcast domains
- Control inter-VLAN traffic with ACLs
- Improve network performance
- Simplify network management

## Next: Spanning Tree Protocol
Move to `02-STP-Configuration/` to learn loop prevention.