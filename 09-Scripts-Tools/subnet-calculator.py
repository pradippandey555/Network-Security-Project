#!/usr/bin/env python3
"""
Subnet Calculator Tool
For Packet Tracer Network Planning

Usage:
  python3 subnet-calculator.py 192.168.1.0 24
  python3 subnet-calculator.py 10.0.0.0/8
"""

import sys
import ipaddress
from ipaddress import IPv4Network, IPv4Address

def get_subnet_info(ip_input, prefix=None):
    """Calculate subnet information from IP and prefix"""
    try:
        if '/' in ip_input:
            network = IPv4Network(ip_input, strict=False)
        elif prefix:
            network = IPv4Network(f"{ip_input}/{prefix}", strict=False)
        else:
            print("Error: Please provide CIDR notation (e.g., 192.168.1.0/24)")
            print("   or IP and prefix (e.g., 192.168.1.0 24)")
            return None
        
        return {
            'network_address': str(network.network_address),
            'broadcast_address': str(network.broadcast_address),
            'first_usable': str(network.network_address + 1),
            'last_usable': str(network.broadcast_address - 1),
            'subnet_mask': str(network.netmask),
            'prefix_length': network.prefixlen,
            'total_addresses': network.num_addresses,
            'usable_hosts': network.num_addresses - 2 if network.num_addresses > 2 else 0,
            'wildcard_mask': str(IPv4Address(int(network.netmask) ^ 0xffffffff))
        }
    except ValueError as e:
        print(f"Error: Invalid IP address or prefix - {e}")
        return None

def print_subnet_info(info):
    """Print formatted subnet information"""
    print("\n" + "="*50)
    print(" SUBNET CALCULATOR RESULTS")
    print("="*50)
    print(f"Network Address:    {info['network_address']}")
    print(f"Subnet Mask:        {info['subnet_mask']}")
    print(f"Prefix Length:      /{info['prefix_length']}")
    print(f"Wildcard Mask:      {info['wildcard_mask']}")
    print(f"\nBroadcast Address:  {info['broadcast_address']}")
    print(f"First Usable IP:    {info['first_usable']}")
    print(f"Last Usable IP:     {info['last_usable']}")
    print(f"\nTotal Addresses:    {info['total_addresses']}")
    print(f"Usable Hosts:       {info['usable_hosts']}")
    print("="*50 + "\n")

def subnetting_drill():
    """Interactive subnetting practice"""
    questions = [
        ("192.168.1.0/24", "What is the broadcast address?", "192.168.1.255"),
        ("10.0.0.0/8", "How many usable hosts?", "16777214"),
        ("172.16.0.0/12", "What is the subnet mask?", "255.240.0.0"),
        ("192.168.1.128/25", "What is the first usable IP?", "192.168.1.129"),
    ]
    
    print("\n" + "="*50)
    print(" SUBNETTING DRILL MODE")
    print("="*50)
    
    score = 0
    for network, question, answer in questions:
        print(f"\nNetwork: {network}")
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer.lower() == answer.lower():
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Incorrect. Answer: {answer}")
    
    print(f"\nScore: {score}/{len(questions)}")
    print("="*50 + "\n")

def main():
    if len(sys.argv) < 2:
        print("Subnet Calculator for Packet Tracer")
        print("\nUsage:")
        print("  python3 subnet-calculator.py 192.168.1.0/24")
        print("  python3 subnet-calculator.py 192.168.1.0 24")
        print("  python3 subnet-calculator.py --drill")
        print("\nExamples:")
        print("  Class A Private: python3 subnet-calculator.py 10.0.0.0/8")
        print("  Class B Private: python3 subnet-calculator.py 172.16.0.0/12")
        print("  Class C Private: python3 subnet-calculator.py 192.168.1.0/24")
        return
    
    if sys.argv[1] == "--drill":
        subnetting_drill()
        return
    
    ip_input = sys.argv[1]
    prefix = sys.argv[2] if len(sys.argv) > 2 else None
    
    info = get_subnet_info(ip_input, prefix)
    if info:
        print_subnet_info(info)

if __name__ == "__main__":
    main()
