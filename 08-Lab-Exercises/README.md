# Lab Exercises - Module 8

Comprehensive hands-on exercises to apply all learned concepts.

## Contents

1. **Exercise-01-Basic-Topology/** - Simple 2-router network setup
2. **Exercise-02-Secure-Network/** - Multi-VLAN network with security
3. **Exercise-03-Complex-Setup/** - Full enterprise network integration

## Lab Exercise 1: Basic Topology Setup

### Objective
Create a simple network with two routers and verify basic connectivity.

### Requirements
- 2 Routers
- 2 Switches
- 4 PCs
- 1 Serial connection between routers

### Network Design
```
Network 1: 192.168.1.0/24
[PC1] → [Switch1] → [Router1] ←Serial→ [Router2] ← [Switch2] ← [PC2]
                    (Fa0/0)  (S0/0/0) (S0/0/0)   (Fa0/0)
                  192.168.1.1  203.0.113.1-2   10.0.0.1
Network 2: 10.0.0.0/24
```

### Configuration Checklist
- [ ] Configure Router1 Fa0/0: 192.168.1.1/24
- [ ] Configure Router1 S0/0/0: 203.0.113.1/30
- [ ] Configure Router2 S0/0/0: 203.0.113.2/30
- [ ] Configure Router2 Fa0/0: 10.0.0.1/24
- [ ] Add static route on Router1: 10.0.0.0/24 via 203.0.113.2
- [ ] Add static route on Router2: 192.168.1.0/24 via 203.0.113.1
- [ ] Configure PC1: IP 192.168.1.10, GW 192.168.1.1
- [ ] Configure PC2: IP 10.0.0.10, GW 10.0.0.1
- [ ] Test ping PC1 → PC2
- [ ] Test ping PC2 → PC1

### Verification
```
PC1# ping 10.0.0.10
PC2# ping 192.168.1.10
Router1# show ip route
Router2# show ip route
Router1# show interfaces Serial 0/0/0
```

---

## Lab Exercise 2: Secure Enterprise Network

### Objective
Build a multi-VLAN network with firewall and security policies.

### Network Requirements
- 3 Departments (Sales, IT, Accounting)
- 1 DMZ with Web Server
- 1 Firewall
- 2 Routers (for redundancy)
- VLANs for segmentation
- ACLs for access control

### Network Diagram
```
                    Internet
                       │
              ┌────────▼─────────┐
              │   Firewall (ASA) │
              └────────┬─────────┘
                       │
              ┌────────▼─────────┐
              │   DMZ (VLAN 40)  │
              │  172.16.0.0/24   │
              │  [Web Server]    │
              └────────┬─────────┘
                       │
         ┌─────────────┼─────────────┐
         │             │             │
    ┌────▼───┐    ┌────▼───┐   ┌────▼───┐
    │Router1 │    │Router2 │   │Switch  │
    │(Active)│    │(Backup)│   │(Core)  │
    └────┬───┘    └────┬───┘   └────┬───┘
         │             │             │
    ┌────▼──────────────▼─────────────▼────┐
    │         Internal Network              │
    │  (VLAN 10, 20, 30, 99)               │
    └────┬───────────┬──────────┬──────────┘
         │           │          │
    ┌────▼──┐  ┌─────▼───┐  ┌──▼─────┐
    │VLAN10 │  │VLAN 20  │  │VLAN 30 │
    │Sales  │  │   IT    │  │Account │
    │DHCP   │  │  DHCP   │  │ DHCP   │
    └────┬──┘  └─────┬───┘  └──┬─────┘
         │           │          │
    [PC1]...[PC5] [PC6]...[PC10] [PC11..PC15]
```

### Implementation Steps

#### Step 1: Create VLANs
```
Switch(config)# vlan 10
Switch(config-vlan)# name Sales
Switch(config-vlan)# exit

Switch(config)# vlan 20
Switch(config-vlan)# name IT
Switch(config-vlan)# exit

Switch(config)# vlan 30
Switch(config-vlan)# name Accounting
Switch(config-vlan)# exit

Switch(config)# vlan 40
Switch(config-vlan)# name DMZ
Switch(config-vlan)# exit

Switch(config)# vlan 99
Switch(config-vlan)# name Management
Switch(config-vlan)# exit
```

#### Step 2: Assign Ports to VLANs
```
Switch(config)# interface range Fa0/1-5
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 10
Switch(config-if-range)# exit

!--- Repeat for other VLANs (20, 30, 40, 99)
```

#### Step 3: Configure Trunk Ports
```
Switch(config)# interface Fa0/24
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20,30,40,99
Switch(config-if)# exit
```

#### Step 4: Configure Router for Inter-VLAN Routing
```
Router(config)# interface Fa0/0
Router(config-if)# no shutdown
Router(config-if)# exit

!--- Create subinterfaces
Router(config)# interface Fa0/0.10
Router(config-subif)# encapsulation dot1Q 10
Router(config-subif)# ip address 192.168.10.1 255.255.255.0
Router(config-subif)# exit

!--- Repeat for VLANs 20, 30, 40, 99
```

#### Step 5: Configure ACLs
```
!--- Block IT from accessing Accounting
Router(config)# access-list 101 deny ip 192.168.20.0 0.0.0.255 192.168.30.0 0.0.0.255
Router(config)# access-list 101 permit ip any any
Router(config)# interface vlan 20
Router(config-if)# ip access-group 101 out
Router(config-if)# exit
```

#### Step 6: Configure DHCP
```
!--- DHCP for Sales (VLAN 10)
Router(config)# ip dhcp pool Sales
Router(dhcp-config)# network 192.168.10.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.10.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# exit

!--- DHCP for IT (VLAN 20)
Router(config)# ip dhcp pool IT
Router(dhcp-config)# network 192.168.20.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.20.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# exit

!--- DHCP for Accounting (VLAN 30)
Router(config)# ip dhcp pool Accounting
Router(dhcp-config)# network 192.168.30.0 255.255.255.0
Router(dhcp-config)# default-router 192.168.30.1
Router(dhcp-config)# dns-server 8.8.8.8
Router(dhcp-config)# exit
```

### Verification Tasks
- [ ] All PCs receive DHCP addresses
- [ ] PCs in same VLAN can ping each other
- [ ] PCs in different VLANs can ping router interface
- [ ] Blocked traffic generates no response
- [ ] Show running-config saved

---

## Lab Exercise 3: Complex Enterprise Integration

### Objective
Design and implement a complete enterprise network with all learned concepts.

### Requirements
- Multiple sites (HQ and Remote Office)
- VLANs and subnetting
- Dynamic routing (OSPF)
- VPN connectivity
- Firewall and DMZ
- ACLs and security policies
- NAT and PAT
- VoIP support (optional)

### Complete Network Architecture
```
                        Internet
                           │
                    ┌──────▼──────┐
                    │ ISP Router  │
                    └──────┬──────┘
                           │
           ┌───────────────┼───────────────┐
           │               │               │
       [HQ Firewall]   [Remote FW]   [Backup ISP]
           │               │
      [HQ Router]     [Remote Router]
      OSPF Area 0     OSPF Area 1
           │               │
      [HQ Switch]     [Remote Switch]
        VLANs 10-30      VLANs 40-50
           │               │
      [HR,Finance      [Sales,Support
        Engineering]      Operations]
```

### Implementation Outline

1. **Layer 1: Physical Setup**
   - 2 sites with routers and switches
   - Serial/Frame-Relay links between sites
   - Firewall on each site

2. **Layer 2: VLAN Segmentation**
   - HQ: VLANs 10 (HR), 20 (Finance), 30 (Engineering)
   - Remote: VLANs 40 (Sales), 50 (Operations)
   - Shared: VLAN 99 (Management)

3. **Layer 3: IP Addressing**
   - HQ: 10.1.0.0/16
   - Remote: 10.2.0.0/16
   - Inter-site: 203.0.113.0/24

4. **Layer 4: Routing**
   - OSPF dynamic routing
   - Area 0 (backbone)
   - Area 1 (remote)
   - Default routes

5. **Layer 5: Security**
   - Firewalls with DMZ
   - Site-to-Site VPN
   - ACLs between zones
   - NAT for internet access

6. **Layer 6: Services**
   - DHCP on each VLAN
   - DNS resolution
   - VoIP (optional)
   - Backup services

### Testing Checklist
- [ ] HQ PC ↔ Remote PC connectivity
- [ ] OSPF neighbors established
- [ ] VPN tunnel online
- [ ] VLANs isolated by ACL
- [ ] Internet access via NAT
- [ ] DHCP working on all VLANs
- [ ] Redundancy tested (link failure)
- [ ] Logs and monitoring active

---

## Grading Rubric

### Exercise 1: Basic Topology (20 points)
- Topology correctly created (5 pts)
- Routing configured correctly (7 pts)
- Connectivity verified (5 pts)
- Configuration saved (3 pts)

### Exercise 2: Secure Network (35 points)
- VLANs created and assigned (7 pts)
- Routing configured (7 pts)
- ACLs implemented (7 pts)
- DHCP working (7 pts)
- Documentation (7 pts)

### Exercise 3: Complex Integration (45 points)
- Network design (10 pts)
- Routing (OSPF) (10 pts)
- Security (VPN, Firewall) (10 pts)
- Troubleshooting and optimization (10 pts)
- Documentation and presentation (5 pts)

---

## Tips for Success

✅ **Do:**
- Document each configuration step
- Test after each change
- Keep configurations organized
- Save backups frequently
- Reference templates and guides

❌ **Don't:**
- Skip basic setup steps
- Forget default routes
- Apply ACLs without testing
- Change multiple things at once
- Leave configuration unsaved

## Submission

For each exercise submit:
1. Network diagram
2. Complete configuration files
3. Screenshots of verification commands
4. Lab report (observations, issues, solutions)
5. Lessons learned

## Progression

Start with Exercise 1, only move to Exercise 2 after Exercise 1 is working perfectly. Similarly for Exercise 3.

**Estimated Time:**
- Exercise 1: 2-3 hours
- Exercise 2: 4-5 hours
- Exercise 3: 6-8 hours

**Total Lab Time: 12-16 hours**