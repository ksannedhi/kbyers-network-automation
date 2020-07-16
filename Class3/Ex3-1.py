import json
from pprint import pprint

with open("Ex3.json") as f:
    intf_data = json.load(f)

ipv4_list = []
ipv6_list = []

for intf_name, intf_det in intf_data.items():
    for ip_ver, ip_data in intf_det.items():
        for ip_addr, pref_len in ip_data.items():
            prefix_len = pref_len['prefix_length']
            if ip_ver == "ipv4":
                ipv4_list.append(f'{ip_addr}/{prefix_len}')
            else:
                ipv6_list.append(f'{ip_addr}/{prefix_len}')

pprint(ipv4_list)
pprint(ipv6_list)

