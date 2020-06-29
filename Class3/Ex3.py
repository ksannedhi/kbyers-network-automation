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

