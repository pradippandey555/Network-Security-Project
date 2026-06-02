# CCNA Study Guide and Certification Path

## Exam Overview

**Official Name:** Cisco Certified Network Associate (CCNA)
**Exam Code:** 200-301
**Duration:** 120 minutes
**Format:** 55-65 questions (mix of multiple choice, drag-and-drop, fill-the-blank)
**Passing Score:** 825-875 out of 1000
**Cost:** $330 USD
**Validity:** 3 years
**Registration:** Pearson VUE Testing Center

---

## Exam Blueprint

### 1. Network Fundamentals (15%)

**Topics:**
- Explain the role and function of network components (router, switch, firewall, load balancer)
- Describe network topology architectures (3-tier, spine-leaf, WAN, small office/home office)
- Compare physical interface and routing interface terminology
- Identify interface and cable types (SFP, copper, fiber)
- Identify commonly used networking terms (uplink, backbone, autonomous system)
- Compare network speeds (bits per second vs bytes per second)
- Describe standards associated with numbers in networking (30dB loss, 3dB rule, 10% Ethernet)
- Explain Low Latency Queuing concept
- Describe the purpose of models (conceptual or theoretical)
- Describe the purpose of the Open Systems Interconnection (OSI) model
- Compare the Open Systems Interconnection (OSI) model layers
- Describe the purpose of the TCP/IP model
- Compare the OSI model and the TCP/IP model
- Describe the purpose and basics of inside and outside addresses on the packet
- Identify the parts of an IPv4 address (network vs. host, public vs. private)
- Describe IPv6 main improvements over IPv4
- Describe IPv6 address types (global unicast, link-local, loopback, multicast, link-local unicast, unspecified, anycast)
- Verify IP parameters for Client OS (Windows, Mac OS, Linux)
- Describe wireless principles
- Describe small office/home office (SOHO) principles

**Skills to Practice:**
- Binary conversion
- Subnet calculations
- IP address classification
- OSI model layer identification
- TCP/IP model understanding

---

### 2. Network Access (20%)

**Topics:**
- Configure and verify VLANs (normal range)
- Configure and verify interVLAN routing (router on a stick)
- Configure and verify Spanning Tree Protocol
- Configure portfast and BPDU guard
- Explain DHCP (v4 and v6) concepts
- Configure and verify DHCP on a router
- Troubleshoot DHCP on a client and router
- Configure switch security (PVLAN, port security, SSH, device access)
- Configure and verify RSTP operation
- Describe common access layer threat mitigation techniques
- Describe the purpose of AAA
- Describe wireless security protocols (WPA, WPA2, WPA3)
- Describe AP and WLC management access connections (HTTPS, SSH, Telnet, HTTP)
- Interpret waveform graphs to identify 802.11 wireless signal issues
- Describe the purpose of SNMP v2c and v3

**Labs to Complete:**
- VLAN creation and assignment
- Inter-VLAN routing
- STP configuration
- Port security setup
- DHCP troubleshooting

---

### 3. IP Connectivity (25%)

**Topics:**
- Interpret the components of routing table
- Determine how a router makes a forwarding decision
- Distinguish between connected and remote routes
- Verify the routing table
- Configure and verify IPv4 and IPv6 static routing
- Configure and verify single area OSPF (v2)
- Explain OSPF areas and the purpose of the area border router (ABR)
- Configure and verify OSPF interface parameters
- Configure and verify OSPF route redistribution
- Configure and verify EIGRP
- Configure and verify EIGRP for IPv6
- Describe static and dynamic routing protocol concepts
- Describe administrative distance
- Troubleshoot basic connectivity issues (client to client in the same VLAN and across different VLANs)
- Compare OSPF and EIGRP routing protocols

**Key Concepts:**
- Administrative distance
- Metric calculation
- Neighbor formation
- Route selection
- Protocol comparison

---

### 4. IP Services (10%)

**Topics:**
- Configure and verify inside source NAT using static and dynamic
- Configure and verify NTP operating in a client and server mode
- Explain the role of DHCP and DNS within the network
- Explain the function of SNMP in network operations
- Describe and verify SNMP v2c and v3

**Skills:**
- NAT configuration
- NTP synchronization
- DNS resolution
- SNMP configuration

---

### 5. Security Fundamentals (20%)

**Topics:**
- Describe the function of a firewall
- Describe the purpose of access control lists
- Configure and verify access control lists
- Describe the concepts of threat defense
- Describe methods to mitigate common Layer 2 attacks (MAC address spoofing, STP manipulation)
- Configure and verify device access control
- Explain the purpose of VPN and tunneling
- Configure and verify site-to-site VPN and remote access VPN
- Identify the basic parameters of a crypto map
- Describe IKE Phase 1 and Phase 2 concepts
- Describe the purpose of the service password encryption command
- Configure and verify 802.1X port-based authentication
- Describe TACACS+ and RADIUS concepts
- Configure and verify AAA on Cisco devices

**Hands-on Practice:**
- ACL configuration (standard and extended)
- Firewall rules
- VPN tunnels
- AAA setup
- Port security

---

### 6. Automation and Programmability (10%)

**Topics:**
- Define the concepts of APIs
- Construct API requests (URI, method, headers, payload)
- Describe Cisco DNA Center workflows
- Describe benefits of network automation and management
- Compare traditional networks with controller-based networking
- Describe the use of Cisco DNA Center to manage Cisco DNA Spaces
- Describe Python basics relevant to network programmers (data types, conditionals, functions, regular expressions)

**Skills:**
- Python basics
- API concepts
- REST principles
- JSON/XML understanding

---

## 12-Week Study Plan

### Week 1-2: Network Fundamentals
**Time Allocation:** 14-16 hours

- Day 1-2: OSI and TCP/IP models
  - Watch videos, take notes
  - Practice quiz
  
- Day 3-4: IP addressing and subnetting
  - Binary conversion practice
  - Subnet calculator exercises
  - 30+ subnetting problems
  
- Day 5-6: Routing basics
  - Understand routing tables
  - Learn metric concepts
  - Compare routing protocols
  
- Day 7: Review and practice test
  - Quiz 20-30 questions
  - Review weak areas

**Deliverables:**
- ✅ Complete subnetting practice (target: 95%+ accuracy)
- ✅ Pass practice quiz (70%+)
- ✅ Understand all OSI layer functions

---

### Week 3-4: Network Access (VLANs and STP)
**Time Allocation:** 16-18 hours

- Day 1-2: VLAN fundamentals
  - VLAN creation
  - Trunk configuration
  - Inter-VLAN routing (router on a stick)
  
- Day 3-4: Spanning Tree Protocol
  - STP concepts
  - Root bridge election
  - PortFast and BPDU Guard
  - RSTP operation
  
- Day 5-6: Switch security
  - Port security configuration
  - SSH setup
  - DHCP snooping
  
- Day 7: Lab exercises
  - Create VLAN topology
  - Configure STP
  - Implement port security

**Deliverables:**
- ✅ Working VLAN and inter-VLAN routing setup
- ✅ STP configured with optimal topology
- ✅ Port security and SSH enabled

---

### Week 5-6: IP Connectivity - Routing Protocols
**Time Allocation:** 18-20 hours

- Day 1-2: Static routing
  - Basic static routes
  - Default routes
  - Floating static routes
  - Multi-router topologies
  
- Day 3-4: OSPF v2
  - Single area OSPF
  - OSPF neighbors
  - Cost/metric calculation
  - Network types
  
- Day 5-6: EIGRP
  - EIGRP configuration
  - Metric calculation (K values)
  - Unequal cost load balancing
  - Feasible successors
  
- Day 7: Comparison and labs
  - OSPF vs EIGRP
  - Complete routing labs

**Deliverables:**
- ✅ Static routing setup (3+ routers)
- ✅ OSPF single area (3+ routers, neighbor formation)
- ✅ EIGRP fully functional (load balancing working)

---

### Week 7: Access Control Lists (ACLs)
**Time Allocation:** 12-14 hours

- Day 1-2: Standard ACLs
  - ACL numbering
  - Permit/deny logic
  - Wildcard masks
  - Application to interfaces
  
- Day 3-4: Extended ACLs
  - Protocol filtering
  - Port-based filtering
  - Complex filtering rules
  - ACL logging
  
- Day 5-6: Named ACLs and best practices
  - Named ACL configuration
  - ACL editing
  - Performance optimization
  
- Day 7: Practice and labs
  - Create 10+ ACL configurations
  - Troubleshoot blocked traffic

**Deliverables:**
- ✅ Standard ACL configured and verified
- ✅ Extended ACL with multiple rules
- ✅ Named ACL with proper documentation

---

### Week 8: IP Services (NAT, DHCP, DNS, NTP)
**Time Allocation:** 12-14 hours

- Day 1-2: NAT configuration
  - Static NAT
  - Dynamic NAT
  - PAT (overload)
  - Troubleshooting NAT
  
- Day 3: DHCP
  - DHCP configuration
  - DHCP troubleshooting
  - DHCP options
  
- Day 4: DNS and NTP
  - DNS concepts
  - NTP configuration
  - Time synchronization
  
- Day 5-7: Labs and practice
  - Complete NAT labs
  - DHCP server setup
  - Troubleshooting exercises

**Deliverables:**
- ✅ All three NAT types working
- ✅ DHCP operational
- ✅ NTP synchronized across network

---

### Week 9-10: Security Fundamentals
**Time Allocation:** 20-22 hours

- Day 1-2: Firewall and threat defense
  - Firewall concepts
  - DMZ setup
  - Stateful inspection
  - Common layer 2 attacks
  
- Day 3-4: VPN and encryption
  - IPSec VPN concepts
  - IKE Phase 1 and 2
  - Site-to-site VPN
  - Remote access VPN
  
- Day 5-6: AAA and authentication
  - RADIUS and TACACS+
  - Local authentication
  - 802.1X
  - Device access control
  
- Day 7: Security labs
  - Configure VPN tunnel
  - Setup AAA
  - Implement firewall rules

**Deliverables:**
- ✅ Site-to-site VPN operational
- ✅ AAA configured with RADIUS
- ✅ Firewall rules documented

---

### Week 11: Automation and Programmability
**Time Allocation:** 10-12 hours

- Day 1-2: Python basics
  - Data types
  - Conditionals and loops
  - Functions
  - Regular expressions
  
- Day 3-4: APIs and REST
  - API concepts
  - REST principles
  - JSON/XML
  - Postman testing
  
- Day 5-6: Network automation
  - Ansible basics
  - Configuration templating
  - Script writing
  
- Day 7: Review
  - Complete automation examples

**Deliverables:**
- ✅ Write Python script for IP calculations
- ✅ Make REST API calls
- ✅ Understand automation concepts

---

### Week 12: Final Review and Practice Exams
**Time Allocation:** 16-18 hours

- Day 1-3: Full-length practice exams
  - Boson ExSim practice exams (minimum 2)
  - Measure weak areas
  - Review explanations
  
- Day 4-5: Weak area reinforcement
  - Re-study failing topics
  - Complete more labs
  - Practice questions
  
- Day 6: Final review
  - Review notes
  - Key concepts checklist
  - Comfortable with command syntax
  
- Day 7: Exam preparation
  - Get good sleep
  - Review schedule/directions
  - Mental preparation

**Deliverables:**
- ✅ Pass practice exams with 80%+
- ✅ Identify remaining weak areas
- ✅ Ready for real exam

---

## Practice Resources

### Official Cisco Resources
- Cisco Learning Network
- Cisco Official Exam Guides
- Cisco Command References
- Cisco Online Learning Library

### Third-Party Resources
- **Udemy** - CCNA courses by Messer, Lammle
- **Boson** - ExSim practice exams (highly recommended)
- **CompTIA** - Network+ foundation
- **Pluralsight** - Video training
- **Professor Messer** - Free YouTube videos

### Hands-On Practice
- **Cisco Packet Tracer** - Free simulation software
- **GNS3** - Advanced network simulator
- **This Repository** - Network-Security-Project
- **Cisco DevNet Sandbox** - Real equipment access
- **CCNA labs** - Netacad lab modules

---

## Exam Day Tips

✅ **Do:**
- Arrive 15 minutes early
- Read questions carefully (twice if needed)
- Answer easier questions first
- Mark difficult questions for review
- Manage time (average 2 min per question)
- Review marked questions at end
- Stay calm and focused
- Verify answer before moving on
- Trust your preparation

❌ **Don't:**
- Guess without analysis
- Spend too long on one question
- Change answers without good reason
- Leave questions blank
- Second-guess yourself constantly
- Panic if unsure

---

## Post-Exam

After passing CCNA:

### Specialization Options
1. **CCNP Enterprise** - Advanced routing/switching
2. **CCNP Security** - Network security focus
3. **CCNP Service Provider** - ISP and carrier focus
4. **Other vendor certs** - Juniper, Palo Alto, AWS, etc.

### Career Paths
- Network Administrator
- Network Engineer
- Security Engineer
- Systems Engineer
- Solutions Architect
- Network Consultant

---

## Success Metrics

| Metric | Target | How to Measure |
|--------|--------|----------------|
| Subnetting accuracy | 95%+ | Practice tests |
| Routing lab completion | 100% | All labs working |
| Security understanding | 80%+ | Practice questions |
| VPN configuration | Working | Test tunnel |
| Python basics | Functional | Write scripts |
| Practice exam score | 80%+ | Boson, NetAcad |
| Command fluency | Complete | Configuration speed |

---

## Common Mistakes to Avoid

1. **Neglecting hands-on practice**
   - Theory alone isn't enough
   - Lab 40%, Study 60%

2. **Skipping weak areas**
   - Focus on difficult topics
   - Don't just review strengths

3. **Memorizing without understanding**
   - Understand the WHY
   - Can then figure out the HOW

4. **Not practicing with actual commands**
   - Learn exact syntax
   - Understand command options

5. **Leaving review until last week**
   - Review throughout course
   - Space out study

6. **Only doing multiple choice**
   - Practice drag-and-drop
   - Practice fill-in-the-blank
   - Practice simulations

---

## Final Checklist Before Exam

- [ ] Completed all 12 weeks of study
- [ ] Passed 2+ practice exams with 80%+
- [ ] Understand all exam blueprint topics
- [ ] Can configure all major services
- [ ] Know command syntax well
- [ ] Comfortable troubleshooting
- [ ] Reviewed weak areas
- [ ] Got good sleep night before
- [ ] Know testing center location
- [ ] Have valid ID and reservation
- [ ] Mentally prepared and confident

---

## Good Luck!

You've got this. The CCNA is achievable with consistent effort and proper preparation. Follow this guide, complete the labs in this repository, and you'll be well-prepared for exam success.

**Remember:** The goal isn't just to pass the exam, but to actually understand networking so you can build secure, scalable networks in the real world.

Good luck! 🚀