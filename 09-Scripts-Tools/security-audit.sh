#!/bin/bash

# Security Audit Script for Network Devices
# Run on routers/switches to check security configurations
# Usage: bash security-audit.sh

echo "========================================"
echo "  NETWORK SECURITY AUDIT SCRIPT"
echo "========================================"
echo ""

# Color codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Counters
passed=0
failed=0

# Function to print results
check_result() {
    local check_name="$1"
    local result="$2"
    local severity="$3"
    
    if [ "$result" -eq 0 ]; then
        echo -e "${GREEN}✓${NC} PASS: $check_name"
        ((passed++))
    else
        echo -e "${RED}✗${NC} FAIL: $check_name"
        if [ "$severity" = "CRITICAL" ]; then
            echo "    Severity: ${RED}CRITICAL${NC}"
        elif [ "$severity" = "HIGH" ]; then
            echo "    Severity: ${YELLOW}HIGH${NC}"
        fi
        ((failed++))
    fi
}

echo "1. CHECKING SSH CONFIGURATION"
echo "   Checking if SSH is enabled..."
# In real Cisco device, would check 'show ip ssh'
echo -e "${YELLOW}[i]${NC} Manual verification required on actual device"
echo ""

echo "2. CHECKING PASSWORD ENCRYPTION"
echo "   Checking if password encryption is enabled..."
echo -e "${YELLOW}[i]${NC} Run 'show run | include service password-encryption'"
echo ""

echo "3. CHECKING UNUSED SERVICES"
echo "   Recommended disabled services:"
echo "   - HTTP server (use HTTPS)"
echo "   - CDP (Cisco Discovery Protocol)"
echo "   - Telnet (use SSH)"
echo ""

echo "4. CHECKING ACLs"
echo "   Verifying access control lists..."
echo -e "${YELLOW}[i]${NC} Run 'show ip access-lists'"
echo ""

echo "5. CHECKING LOGGING"
echo "   Verifying syslog configuration..."
echo -e "${YELLOW}[i]${NC} Run 'show logging'"
echo ""

echo "6. CHECKING AUTHENTICATION"
echo "   Verifying TACACS+/RADIUS configuration..."
echo -e "${YELLOW}[i]${NC} Run 'show aaa servers'"
echo ""

echo "========================================"
echo "  SECURITY AUDIT CHECKLIST"
echo "========================================"
echo ""
echo "Physical Security:"
echo "  [ ] Device is in a locked cabinet"
echo "  [ ] Console port is protected"
echo "  [ ] Management interfaces are on secure network"
echo ""
echo "Access Control:"
echo "  [ ] SSH is enabled (not Telnet)"
echo "  [ ] SSH uses strong encryption (AES-256)"
echo "  [ ] Default credentials are changed"
echo "  [ ] No unnecessary user accounts"
echo ""
echo "Network Configuration:"
echo "  [ ] Unused interfaces are disabled"
echo "  [ ] ACLs are configured on borders"
echo "  [ ] CDP is disabled if not needed"
echo "  [ ] SNMP uses SNMPv3 (not v1/v2)"
echo ""
echo "Monitoring:"
echo "  [ ] Syslog is configured"
echo "  [ ] All access is logged"
echo "  [ ] NTP is configured for time sync"
echo "  [ ] RADIUS/TACACS+ is deployed"
echo ""
echo "Maintenance:"
echo "  [ ] Configuration is backed up"
echo "  [ ] Backups are stored securely"
echo "  [ ] Change log is maintained"
echo "  [ ] Regular security reviews scheduled"
echo ""
echo "========================================"
echo "  REMEDIATION RECOMMENDATIONS"
echo "========================================"
echo ""
echo "High Priority:"
echo "  1. Disable Telnet - Use SSH instead"
echo "  2. Configure strong passwords (12+ chars)"
echo "  3. Enable service password-encryption"
echo "  4. Implement RADIUS/TACACS+"
echo ""
echo "Medium Priority:"
echo "  1. Disable CDP on edge interfaces"
echo "  2. Configure NTP for time sync"
echo "  3. Enable comprehensive logging"
echo "  4. Configure syslog server"
echo ""
echo "Low Priority:"
echo "  1. Disable HTTP server"
echo "  2. Configure banner text"
echo "  3. Setup email alerts"
echo "  4. Configure device redundancy"
echo ""
echo "========================================"
