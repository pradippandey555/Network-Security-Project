# Security Best Practices for Network Administration

## 1. Access Control

### Authentication

✅ **Do:**
- Use strong passwords (12+ characters, mixed case, numbers, symbols)
- Change default credentials immediately
- Implement Multi-Factor Authentication (MFA)
- Use SSH instead of Telnet
- Implement certificate-based authentication
- Regular password rotation policy

```cisco
! Cisco Router SSH Configuration
Router(config)# crypto key generate rsa modulus 2048
Router(config)# ip ssh version 2
Router(config)# username admin privilege 15 secret StrongPass123!
Router(config)# line vty 0 4
Router(config-line)# transport input ssh
Router(config-line)# login local
Router(config-line)# exec-timeout 10
Router(config-line)# exit
Router(config)# ip ssh authentication retries 2
Router(config)# ip ssh time-out 60
```

❌ **Don't:**
- Use Telnet (unencrypted)
- Use default vendor passwords
- Write passwords on sticky notes
- Use same password for multiple devices
- Allow weak passwords

### Authorization

✅ **Do:**
- Implement RADIUS/TACACS+ for centralized authentication
- Use role-based access control (RBAC)
- Apply principle of least privilege
- Grant temporary access when needed
- Revoke access immediately when user leaves
- Implement command authorization

```cisco
! RADIUS Configuration
Router(config)# radius server RADIUS_SERVER
Router(config-radius-server)# address ipv4 192.168.1.100 auth-port 1812 acct-port 1813
Router(config-radius-server)# key RadiusSecretKey123
Router(config-radius-server)# exit

! Use RADIUS for AAA
Router(config)# aaa new-model
Router(config)# aaa authentication login default group radius local
Router(config)# aaa authorization exec default group radius local
Router(config)# aaa accounting exec default start-stop group radius
```

❌ **Don't:**
- Use local authentication for large networks
- Grant unnecessary administrator privileges
- Leave terminated user accounts active
- Use generic shared accounts

### Accounting

✅ **Do:**
- Enable comprehensive logging
- Log all administrative actions
- Log authentication attempts (success and failure)
- Monitor logs regularly
- Retain logs for 90+ days
- Use centralized syslog server

```cisco
! Syslog Configuration
Router(config)# logging 192.168.1.100
Router(config)# logging trap informational
Router(config)# logging source-interface FastEthernet0/0
Router(config)# logging facility local7
Router(config)# service timestamps log datetime msec
Router(config)# no logging console
```

❌ **Don't:**
- Disable logging to save storage
- Ignore authentication failures
- Log sensitive data (passwords)
- Forget to rotate logs

---

## 2. Network Security

### Firewall Rules

✅ **Do:**
- Default deny-all policy
- Explicitly permit necessary traffic
- Log all denied connections
- Regular policy review
- Document firewall rules
- Implement geofencing if applicable
- Use application layer filtering

```cisco
! Basic Firewall Policy
access-list 101 remark === Internet Traffic ===
access-list 101 permit tcp 192.168.1.0 0.0.0.255 any eq 80
access-list 101 permit tcp 192.168.1.0 0.0.0.255 any eq 443
access-list 101 permit tcp 192.168.1.0 0.0.0.255 any eq 25
access-list 101 deny ip any any log

interface Serial0/0/0
  ip access-group 101 in
end
```

❌ **Don't:**
- Permit all and try to deny bad traffic
- Use overly broad rules
- Forget to log denied traffic
- Neglect application-layer threats

### VLANs and Segmentation

✅ **Do:**
- Separate sensitive departments
- Isolate guest networks
- Use separate VLAN for management
- Don't put devices on VLAN 1
- Implement inter-VLAN access control
- Monitor VLAN hopping attempts

```cisco
! VLAN Best Practices
Switch(config)# no vlan 1
Switch(config)# vlan 99
Switch(config-vlan)# name Management
Switch(config-vlan)# exit

Switch(config)# interface vlan 99
Switch(config-if)# ip address 192.168.99.1 255.255.255.0
Switch(config-if)# exit

! Shutdown VLAN 1
Switch(config)# interface vlan 1
Switch(config-if)# shutdown
Switch(config-if)# exit
```

❌ **Don't:**
- Use VLAN 1 for data traffic
- Mix administrative and user VLANs
- Leave unnecessary VLANs active

### Port Security

✅ **Do:**
- Limit MAC addresses per port
- Use sticky mode for dynamic learning
- Shut down port on violation
- Document allowed MAC addresses
- Monitor for unauthorized devices

```cisco
! Port Security Configuration
Switch(config)# interface FastEthernet0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 1
Switch(config-if)# switchport port-security mac-address sticky
Switch(config-if)# switchport port-security violation shutdown
Switch(config-if)# exit
```

❌ **Don't:**
- Leave port security disabled
- Allow unlimited MAC addresses
- Use restrict mode without planning

---

## 3. Encryption

### Data at Rest

✅ **Do:**
- Encrypt sensitive configuration files
- Use AES-256 for encryption
- Protect backup media
- Encrypt database files
- Implement FDE (Full Disk Encryption)

```cisco
! Enable Configuration Encryption
Router(config)# service password-encryption
Router(config)# exit
Router# copy running-config startup-config
```

❌ **Don't:**
- Store clear-text passwords
- Leave backups unencrypted
- Share encryption keys insecurely

### Data in Transit

✅ **Do:**
- Use TLS 1.2+ for HTTPS
- Implement IPSec for VPN
- Use PFS (Perfect Forward Secrecy)
- Rotate certificates regularly
- Use strong DH groups (14+)

```cisco
! VPN Security Parameters
Router(config)# crypto isakmp policy 10
Router(config-isakmp)# encryption aes 256
Router(config-isakmp)# hash sha512
Router(config-isakmp)# authentication pre-share
Router(config-isakmp)# group 20
Router(config-isakmp)# lifetime 86400
Router(config-isakmp)# exit

Router(config)# crypto ipsec transform-set VPN-SET esp-aes 256 esp-sha512-hmac
Router(config-crypto-trans)# mode tunnel
Router(config-crypto-trans)# exit
```

❌ **Don't:**
- Use unencrypted management connections
- Use weak encryption (DES, MD5)
- Reuse VPN keys
- Ignore certificate expiration

---

## 4. Device Hardening

### Disable Unnecessary Services

✅ **Do:**
- Disable HTTP (use HTTPS)
- Disable CDP if not needed
- Disable unused protocols
- Minimize attack surface

```cisco
! Disable Unnecessary Services
Router(config)# no ip http server
Router(config)# no ip http secure-server
Router(config)# no cdp run
Router(config)# no ip source-route
Router(config)# no service udp-small-servers
Router(config)# no service tcp-small-servers
Router(config)# no ip mask-reply
Router(config)# no ip redirect
```

❌ **Don't:**
- Leave services running you don't use
- Enable protocols you won't use

### Banner and Warnings

✅ **Do:**
- Display legal warning banner
- Indicate authorized access only
- Set execution timeout
- Log all access

```cisco
! Banner Configuration
Router(config)# banner motd ^C
WARNING: This system is for authorized use only.
All activity is monitored and logged.
Unauthorized access attempts are prosecuted to the fullest extent of the law.
^C

Router(config)# line vty 0 4
Router(config-line)# exec-timeout 15
Router(config-line)# absolute-timeout 120
Router(config-line)# exit
```

### Updates and Patches

✅ **Do:**
- Keep IOS/firmware updated
- Test patches in lab first
- Plan maintenance windows
- Document all changes
- Keep configuration backups

❌ **Don't:**
- Delay security patches
- Update without testing
- Skip backups before update

---

## 5. Monitoring and Logging

### SNMP Security

✅ **Do:**
- Use SNMPv3 only (not v1/v2)
- Disable SNMP if not needed
- Use authentication and encryption
- Restrict SNMP access with ACL

```cisco
! SNMPv3 Configuration
Router(config)# snmp-server group AdminGroup v3 auth
Router(config)# snmp-server user AdminUser AdminGroup v3 auth sha AuthPassword priv aes EncryptPassword
Router(config)# snmp-server host 192.168.1.100 version 3 AdminUser
Router(config)# access-list 10 permit 192.168.1.100
Router(config)# snmp-server community [disabled]
```

### Log Management

✅ **Do:**
- Centralize logging (syslog, SIEM)
- Monitor for security events
- Alert on suspicious activity
- Review logs regularly
- Archive logs long-term
- Protect log integrity

```cisco
! Logging Configuration
Router(config)# logging 192.168.1.100
Router(config)# logging trap warnings
Router(config)# service timestamps log datetime
Router(config)# logging facility local3
Router(config)# logging queue-limit 500
```

---

## 6. Backup and Disaster Recovery

### Configuration Backups

✅ **Do:**
- Backup configurations regularly (daily)
- Store backups securely and encrypted
- Test restore procedures
- Keep offline backups
- Document backup process
- Automate backups if possible

```bash
# Backup Script Example
#!/bin/bash
DATE=$(date +%Y%m%d)
DEVICE="Router1"
IP="192.168.1.1"

echo "Backing up $DEVICE..."
expect <<EOF
  spawn ssh admin@$IP
  expect "Password:"
  send "password\r"
  expect "$"
  send "copy running-config startup-config\r"
  expect "OK"
  send "exit\r"
EOF

echo "Backup completed: ${DEVICE}_${DATE}.cfg"
```

### Disaster Recovery

✅ **Do:**
- Have recovery plan documented
- Test recovery procedures quarterly
- Maintain spare equipment
- Document network design
- Keep installation media
- Plan for different failure scenarios

❌ **Don't:**
- Assume recovery will work without testing
- Keep single backup location
- Leave recovery plan undocumented

---

## 7. Change Management

### Configuration Changes

✅ **Do:**
- Submit change request before modifying
- Get approval from management
- Test in lab/staging first
- Document all changes
- Maintain change log
- Have rollback plan
- Notify affected users

```
Change Request Template:

Change ID: CHG-2026-0001
Date Requested: 2026-06-02
Requested By: Network Admin
Approved By: Network Manager

What: Update OSPF cost for WAN links
Why: Optimize traffic flow
When: 2026-06-03 02:00-03:00 UTC
How: Modify OSPF cost values on Router1, Router2
Rollback: Restore previous configuration if issues
Impact: Minimal - routing optimization
Testing: Tested in lab - no issues
```

❌ **Don't:**
- Make changes without approval
- Change multiple things at once
- Modify production without testing
- Forget rollback plan

---

## 8. Compliance and Auditing

### Regular Audits

✅ **Do:**
- Quarterly security audit
- Annual penetration testing
- Monitor compliance with policies
- Audit user access regularly
- Review firewall rules quarterly
- Check for rogue devices

### Compliance Standards

- **NIST Cybersecurity Framework**
- **ISO/IEC 27001** (Information Security)
- **PCI-DSS** (Payment Card Industry)
- **HIPAA** (Healthcare)
- **GDPR** (European data protection)
- **SOC 2** (Service Organization Controls)

---

## 9. Incident Response

### Detection

✅ **Do:**
- Monitor logs 24/7
- Set up alerts for anomalies
- Use IDS/IPS systems
- Monitor bandwidth usage
- Track failed login attempts
- Alert on privilege escalation

### Response

✅ **Do:**
- Have incident response plan
- Isolate affected systems
- Preserve evidence
- Document timeline
- Communicate appropriately
- Conduct post-incident review

---

## 10. Security Checklist

- [ ] All default credentials changed
- [ ] SSH enabled, Telnet disabled
- [ ] Strong passwords enforced
- [ ] Password encryption enabled
- [ ] ACLs implemented on all edges
- [ ] VLANs segmented by function
- [ ] Port security enabled
- [ ] SNMP v3 configured
- [ ] Logging centralized
- [ ] Firewall policies documented
- [ ] VPN encryption strong (AES-256)
- [ ] Unnecessary services disabled
- [ ] Certificates valid and not self-signed
- [ ] Backups automated and tested
- [ ] Change management process in place
- [ ] Audit logs reviewed weekly
- [ ] Incident response plan documented
- [ ] Training completed for admin staff
- [ ] Network diagram documented
- [ ] Disaster recovery plan tested

---

## Summary

Network security is not a one-time setup but an ongoing process:

1. **Plan** - Design secure network
2. **Implement** - Configure security controls
3. **Monitor** - Watch for threats
4. **Review** - Audit security regularly
5. **Improve** - Update based on findings

The defense-in-depth approach uses multiple layers:
- Physical security
- Access control
- Encryption
- Monitoring
- Incident response

Consistently applying these best practices will significantly improve your network's security posture.