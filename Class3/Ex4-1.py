import json

with open("Ex4.json") as f:
    arp_data = json.load(f)

ip_data = arp_data["ipV4Neighbors"]

ip_mac_list = {}
for arp_entry in ip_data:
    mac_addr = arp_entry["hwAddress"]
    ip_addr = arp_entry['address']
    ip_mac_list[ip_addr] = mac_addr

print(ip_mac_list)

