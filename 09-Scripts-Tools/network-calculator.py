#!/usr/bin/env python3
"""
Network Calculator Tool
For IP addressing calculations

Usage:
  python3 network-calculator.py 192.168.1.5 255.255.255.0
  python3 network-calculator.py 10.0.0.0/8
"""

import sys
import ipaddress
from ipaddress import IPv4Network, IPv4Address

def analyze_address(ip_str):
    """Analyze IP address and subnet"""
    try:
        if '/' in ip_str:
            net = IPv4Network(ip_str, strict=False)
            ip = net.network_address
        else:
            ip = IPv4Address(ip_str)
            net = IPv4Network(f"{ip}/32")
        
        # Determine IP class
        first_octet = int(str(ip).split('.')[0])
        if first_octet < 128:
            ip_class = 'A'
        elif first_octet < 192:
            ip_class = 'B'
        elif first_octet < 224:
            ip_class = 'C'
        elif first_octet < 240:
            ip_class = 'D (Multicast)'
        else:
            ip_class = 'E (Reserved)'
        
        # Check if private
        is_private = ip.is_private
        is_loopback = ip.is_loopback
        is_reserved = ip.is_reserved
        
        print(f"\n{'='*50}")
        print(f" IP ADDRESS ANALYSIS: {ip}")
        print(f"{'='*50}")
        print(f"IP Address:     {ip}")
        print(f"IP Class:       {ip_class}")
        print(f"Private:        {'Yes' if is_private else 'No'}")
        print(f"Loopback:       {'Yes' if is_loopback else 'No'}")
        print(f"Reserved:       {'Yes' if is_reserved else 'No'}")
        print(f"Binary:         {'.'.join([bin(int(x))[2:].zfill(8) for x in str(ip).split('.')])}")
        print(f"Hex:            {'.'.join([hex(int(x))[2:].upper() for x in str(ip).split('.')])}")
        print(f"{'='*50}\n")
        
    except ValueError as e:
        print(f"Invalid IP address: {e}")

def calculate_hosts_needed():
    """Determine subnet mask needed for N hosts"""
    print(f"\n{'='*50}")
    print(" DETERMINE SUBNET MASK")
    print(f"{'='*50}")
    
    try:
        hosts = int(input("Number of hosts needed: "))
        
        # Calculate required bits
        import math
        bits_needed = math.ceil(math.log2(hosts + 2))  # +2 for network and broadcast
        prefix = 32 - bits_needed
        
        # Create network with calculated prefix
        test_net = IPv4Network(f"192.168.0.0/{prefix}")
        
        print(f"\nHosts needed:   {hosts}")
        print(f"Prefix length:  /{prefix}")
        print(f"Subnet mask:    {test_net.netmask}")
        print(f"Usable hosts:   {test_net.num_addresses - 2}")
        print(f"Total addresses: {test_net.num_addresses}")
        print(f"{'='*50}\n")
        
    except ValueError:
        print("Invalid input")

def main():
    if len(sys.argv) < 2:
        print("Network Calculator")
        print("\nUsage:")
        print("  python3 network-calculator.py <ip-address> [netmask]")
        print("  python3 network-calculator.py <ip-address>/<prefix>")
        print("  python3 network-calculator.py --help-needed")
        print("\nExamples:")
        print("  python3 network-calculator.py 192.168.1.1 255.255.255.0")
        print("  python3 network-calculator.py 10.0.0.0/8")
        print("  python3 network-calculator.py 172.16.0.1 255.255.0.0")
        return
    
    if sys.argv[1] == "--help-needed":
        calculate_hosts_needed()
        return
    
    ip_input = sys.argv[1]
    
    # If mask provided separately
    if len(sys.argv) > 2:
        mask = sys.argv[2]
        try:
            # Convert mask to prefix
            mask_ip = IPv4Address(mask)
            net = IPv4Network(f"{ip_input}/{mask_ip}")
            ip_input = f"{ip_input}/{net.prefixlen}"
        except:
            pass
    
    analyze_address(ip_input)

if __name__ == "__main__":
    main()
