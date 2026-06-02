# Security Implementation - Module 6

This module covers Firewalls, VPN Configuration, AAA Services, IDS/IPS, and DDoS Mitigation.

## Contents

1. **01-Firewall-Setup/** - Stateful firewall configuration
2. **02-VPN-Configuration/** - Site-to-Site and Remote Access VPN
3. **03-AAA-Services/** - Authentication, Authorization, and Accounting
4. **04-IDS-IPS-Setup/** - Intrusion Detection and Prevention Systems
5. **05-DDoS-Mitigation/** - Distributed Denial of Service protection

## Learning Objectives

By the end of this module, you will:
- ✅ Configure stateful firewalls
- ✅ Implement site-to-site VPN
- ✅ Setup remote access VPN
- ✅ Deploy AAA infrastructure
- ✅ Configure IDS/IPS detection
- ✅ Implement DDoS mitigation strategies
- ✅ Monitor security events

## Duration
**Weeks 9-10** of the project timeline

## Prerequisites
- Complete Modules 1-5
- Understanding of ACLs
- Basic knowledge of encryption
- Familiarity with VPN concepts

## Security Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│ Internet / Untrusted Networks                           │
└──────────────────────┬──────────────────────────────────┘
                       │
               ┌───────▼────────┐
               │ DDoS Mitigation│ (Rate limiting, Geo-blocking)
               └────────┬────────┘
                        │
               ┌────────▼────────┐
               │   Firewall      │ (Stateful inspection)
               │  Fa0/0(outside) │
               └────────┬────────┘
                        │
               ┌────────▼────────┐
               │   IDS/IPS       │ (Threat detection)
               └────────┬────────┘
                        │
               ┌────────▼────────┐
               │   DMZ Zone      │ (Web servers, proxy)
               │  Fa0/1(dmz)     │
               └────────┬────────┘
                        │
               ┌────────▼────────┐
               │   Firewall      │ (DMZ to Inside rules)
               └────────┬────────┘
                        │
               ┌────────▼────────┐
               │  Inside Zone    │ (Corporate network)
               │  Fa0/2(inside)  │
               └────────┬────────┘
                        │
         ┌──────────────┼──────────────┐
         │              │              │
    ┌────▼────┐  ┌─────▼─────┐  ┌────▼────┐
    │ VLAN 10 │  │  VLAN 20  │  │ VLAN 30 │
    │ (Sales) │  │   (IT)    │  │(Account)│
    └────┬────┘  └─────┬─────┘  └────┬────┘
         │             │             │
    ┌────▼────┐  ┌─────▼─────┐  ┌────▼────┐
    │   AAA   │  │   AAA     │  │   AAA  │
    │ Server  │  │  Server   │  │ Server │
    └─────────┘  └───────────┘  └────────┘
```

## Firewall Architecture

### DMZ (Demilitarized Zone)
- Separates untrusted (internet) from trusted (internal) networks
- Contains public-facing servers (web, mail, DNS)
- Limited access to internal resources
- Monitored by IDS/IPS

### Security Zones
1. **Untrusted (Outside)** - Internet, Level 0
2. **DMZ** - Web/Mail servers, Level 50
3. **Trusted (Inside)** - Corporate network, Level 100
4. **Management** - Admin access only, Highest security

## Firewall Rule Direction

```
Outside → DMZ: Permit HTTP/HTTPS only
Outside → Inside: Deny all (except VPN)
DMZ → Inside: Permit database queries only
Inside → DMZ: Permit all (return traffic automatic)
Inside → Outside: Permit all with PAT
```

## VPN Types

### Site-to-Site VPN
- Connects two office networks
- Always-on connection
- Encrypts traffic between sites
- IPSec is standard

**Example:**
```
Main Office (192.168.1.0/24) ←VPN→ Remote Office (10.0.0.0/24)
```

### Remote Access VPN
- Connects individual users
- On-demand connections
- SSL/TLS encryption
- Provides company access from home/travel

**Example:**
```
Home PC ←VPN→ VPN Server ←Network Access→ Corporate Resources
```

## AAA Framework

### Authentication
- Verify user identity (username/password, certificate, token)
- Methods: RADIUS, TACACS+, Active Directory

### Authorization
- Determine what user can do
- Define privilege levels
- Control command execution

### Accounting
- Track user activity
- Log all actions
- Generate audit reports
- Enable compliance

## IDS vs IPS

### IDS (Intrusion Detection System)
- **Monitors** traffic for threats
- **Detects** malicious activity
- **Alerts** administrators
- Passive mode (doesn't block)

### IPS (Intrusion Prevention System)
- **Monitors and blocks** threats
- **Active** protection
- Drops malicious packets
- Prevents attack execution

## DDoS Mitigation Techniques

1. **Rate Limiting** - Limit connections per source
2. **Traffic Filtering** - Block known attack sources
3. **Geo-blocking** - Block countries not in business
4. **Blackhole Routing** - Drop traffic to null route
5. **Anycast Networks** - Distribute traffic across nodes
6. **ISP DDoS Service** - Upstream filtering

## Common Attack Types

### Layer 4 DDoS
- SYN floods
- UDP floods
- Mitigation: Rate limiting, SYN cookies

### Layer 7 DDoS
- HTTP floods
- DNS floods
- Mitigation: WAF, CAPTCHA, rate limiting

## Packet Tracer Limitations

Note: Packet Tracer has limited security simulation capabilities:
- ✅ Can configure firewall rules
- ✅ Can create VPN tunnels
- ✅ Can configure AAA
- ❌ Limited actual IDS/IPS simulation
- ❌ Limited DDoS attack simulation

For real IDS/IPS testing, use:
- GNS3 with Snort/Suricata
- Virtual machines with pfSense/Fortinet
- Cloud labs (AWS, Azure security labs)

## Security Configuration Checklist

- [ ] Firewall installed and enabled
- [ ] All interfaces assigned security levels
- [ ] Default deny-all policy configured
- [ ] DMZ created with appropriate rules
- [ ] VPN configured (site-to-site and/or remote access)
- [ ] AAA server configured
- [ ] IDS/IPS enabled on all interfaces
- [ ] Threat database updated
- [ ] Logging enabled
- [ ] Syslog server configured
- [ ] DDoS protection enabled
- [ ] Rate limiting configured
- [ ] Geo-blocking rules set (if applicable)
- [ ] Regular backups scheduled
- [ ] Security audit performed

## Best Practices

### Firewall
✅ **Do:**
- Deny all by default, permit exceptions
- Log all denied connections
- Review logs regularly
- Keep firewall updated
- Use SSL/TLS inspection

❌ **Don't:**
- Allow unnecessary ports
- Use default credentials
- Disable logging
- Ignore security alerts
- Mix security zones poorly

### VPN
✅ **Do:**
- Use strong encryption (AES-256)
- Implement PFS (Perfect Forward Secrecy)
- Rotate certificates regularly
- Monitor VPN connections
- Use split tunneling carefully

❌ **Don't:**
- Use weak encryption
- Reuse certificates
- Allow unlimited split tunneling
- Ignore failed connection attempts
- Use default pre-shared keys

### AAA
✅ **Do:**
- Use RADIUS/TACACS+ (not local)
- Implement MFA (Multi-Factor Authentication)
- Enforce strong passwords
- Review access regularly
- Revoke promptly when leaving

❌ **Don't:**
- Store passwords locally
- Use shared accounts
- Forget to revoke access
- Allow weak passwords
- Ignore privilege escalation

## Summary

A complete security implementation requires:
1. **Network perimeter** - Firewall with DMZ
2. **Encrypted communication** - VPN for remote and inter-office
3. **User access control** - AAA for authentication
4. **Threat detection** - IDS/IPS monitoring
5. **Attack prevention** - DDoS mitigation
6. **Logging & monitoring** - Track all activity
7. **Regular updates** - Patch vulnerabilities

## Progression Path

1. Start with basic firewall rules
2. Add DMZ for public services
3. Implement VPN for remote access
4. Deploy AAA for centralized auth
5. Add IDS/IPS monitoring
6. Implement DDoS protection

## Next Steps

After completing this module, proceed to **07-Network-Segmentation** to learn about Zero Trust Architecture and microsegmentation.