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

