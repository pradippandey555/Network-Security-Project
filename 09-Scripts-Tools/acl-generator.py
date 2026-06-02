#!/usr/bin/env python3
"""
ACL Generator Tool
Generates Cisco ACLs from JSON configuration

Example usage:
  python3 acl-generator.py --help
  python3 acl-generator.py --example
"""

import json
import sys

def generate_standard_acl(name, rules):
    """Generate standard ACL configuration"""
    config = f"ip access-list standard {name}\n"
    for idx, rule in enumerate(rules):
        action = rule['action'].lower()  # permit/deny
        source = rule['source']
        if '/' in source:
            # Convert CIDR to IP and wildcard
            parts = source.split('/')
            config += f" {idx+1} {action} {parts[0]} {calculate_wildcard(int(parts[1]))}\n"
        else:
            config += f" {idx+1} {action} {source}\n"
    config += "exit\n"
    return config

def generate_extended_acl(number, rules):
    """Generate extended ACL configuration"""
    config = f"access-list {number} remark Extended ACL\n"
    for idx, rule in enumerate(rules):
        action = rule['action'].lower()
        protocol = rule.get('protocol', 'ip').lower()
        source = rule.get('source', 'any')
        dest = rule.get('destination', 'any')
        port_info = ""
        
        if 'port' in rule:
            port_info = f" eq {rule['port']}"
        elif 'port_range' in rule:
            start, end = rule['port_range'].split('-')
            port_info = f" range {start} {end}"
        
        config += f"access-list {number} {action} {protocol} {source} {dest}{port_info}\n"
    
    return config

def calculate_wildcard(prefix_length):
    """Convert prefix length to wildcard mask"""
    wildcard = (1 << (32 - prefix_length)) - 1
    return f"{(wildcard >> 24) & 0xFF}.{(wildcard >> 16) & 0xFF}.{(wildcard >> 8) & 0xFF}.{wildcard & 0xFF}"

def print_example():
    """Print example ACL configuration"""
    print("""
Example ACL Configuration (Standard):
{
  "type": "standard",
  "name": "ALLOW_SALES",
  "rules": [
    {"action": "permit", "source": "192.168.10.0/24"},
    {"action": "deny", "source": "192.168.20.0/24"},
    {"action": "permit", "source": "any"}
  ]
}

Example ACL Configuration (Extended):
{
  "type": "extended",
  "number": 100,
  "rules": [
    {"action": "permit", "protocol": "tcp", "source": "192.168.1.0/24", "destination": "any", "port": 80},
    {"action": "permit", "protocol": "tcp", "source": "192.168.1.0/24", "destination": "any", "port": 443},
    {"action": "deny", "protocol": "tcp", "source": "192.168.1.0/24", "destination": "any", "port": 23},
    {"action": "permit", "protocol": "icmp", "source": "any", "destination": "any"}
  ]
}
""")

def main():
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        print("ACL Generator for Cisco Routers")
        print("\nUsage:")
        print("  python3 acl-generator.py <json-file>")
        print("  python3 acl-generator.py --example")
        return
    
    if sys.argv[1] == "--example":
        print_example()
        return
    
    try:
        with open(sys.argv[1], 'r') as f:
            config = json.load(f)
        
        if config['type'] == 'standard':
            output = generate_standard_acl(config['name'], config['rules'])
        elif config['type'] == 'extended':
            output = generate_extended_acl(config['number'], config['rules'])
        else:
            print(f"Unknown ACL type: {config['type']}")
            return
        
        print("\n" + "="*50)
        print(" GENERATED ACL CONFIGURATION")
        print("="*50)
        print(output)
        print("="*50 + "\n")
        
    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in '{sys.argv[1]}'")

if __name__ == "__main__":
    main()
