'''You have the following JSON ARP data from an Arista switch:

{
    "dynamicEntries": 2,
    "ipV4Neighbors": [
        {
            "hwAddress": "dc38.e111.97cf",
            "address": "172.17.17.1",
            "interface": "Ethernet45",
            "age": 0
        },
        {
            "hwAddress": "90e2.ba5c.25fd",
            "address": "172.17.16.1",
            "interface": "Ethernet36",
            "age": 0
        }
    ],
    "notLearnedEntries": 0,
    "totalEntries": 2,
    "staticEntries": 0
} <-- This is written to Ex4.json as an input to the following script.

From a file, read this JSON data into your Python program.
Process this ARP data and return a dictionary where the dictionary keys are the IP addresses and the dictionary values are the MAC addresses.
Print this dictionary to standard output.'''

import json

with open("Ex4.json") as f:
    arp_data = json.load(f)

ip_mac_data = arp_data["ipV4Neighbors"]
ip_mac_dict = {}

for neighbor_entry in ip_mac_data:
    ip_addr = neighbor_entry["address"]
    mac_addr = neighbor_entry["hwAddress"]
    ip_mac_dict[neighbor_entry["address"]] = neighbor_entry["hwAddress"]

print(ip_mac_dict)

