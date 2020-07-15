'''NAPALM using nxos_ssh has the following data structure in one of its unit tests (the below data is in JSON format). 
{
    "Ethernet2/1": {
        "ipv4": {
            "1.1.1.1": {
                "prefix_length": 24
            }
        }
    },
    "Ethernet2/2": {
        "ipv4": {
            "2.2.2.2": {
                "prefix_length": 27
            }, 
            "3.3.3.3": {
                "prefix_length": 25
            }
        }
    }, 
    "Ethernet2/3": {
        "ipv4": {
            "4.4.4.4": {
                "prefix_length": 16
            }
        }, 
        "ipv6": {
            "fe80::2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }, 
            "2001:db8::1": {
                "prefix_length": 10
            }
        }
    }, 
    "Ethernet2/4": {
        "ipv6": {
            "fe80::2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }, 
            "2001:11:2233::a1": {
                "prefix_length": 24
            }, 
            "2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2": {
                "prefix_length": 64
            }
        }
    } 
}
Read this JSON data in from a file <-- This is written to Ex3.json as an input to the following script.

From this data structure extract all of the IPv4 and IPv6 addresses that are used on this NXOS device.
From this data create two lists: 'ipv4_list' and 'ipv6_list'.
The 'ipv4_list' should be a list of all of the IPv4 addresses including prefixes; the 'ipv6_list' should be a list of all of the IPv6 addresses including prefixes.'''

import json

with open("Ex3.json") as f:
    ip_data = json.load(f)

ipv4_list = []
ipv6_list = []

for intf_name, ip_det in ip_data.items():
    for ip_ver, ip_and_prefix in ip_det.items():
        for ip_addr, pref_len in ip_and_prefix.items():
            prefix_len = pref_len["prefix_length"]
            if ip_ver == "ipv4":
               ipv4_list.append("{}/{}".format(ip_addr, prefix_len))
            if ip_ver == "ipv6":
                ipv6_list.append("{}/{}".format(ip_addr, prefix_len))

print(ipv4_list)
print(ipv6_list)

