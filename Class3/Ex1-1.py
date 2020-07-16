from pprint import pprint

arp_data = '''Protocol  Address      Age  Hardware Addr   Type  Interface
Internet  10.220.88.1   67  0062.ec29.70fe  ARPA  Gi0/0/0
Internet  10.220.88.20  29  c89c.1dea.0eb6  ARPA  Gi0/0/0
Internet  10.220.88.22   -  a093.5141.b780  ARPA  Gi0/0/0
Internet  10.220.88.37 104  0001.00ff.0001  ARPA  Gi0/0/0
Internet  10.220.88.38 161  0002.00ff.0001  ARPA  Gi0/0/0'''

arp_data_lines = arp_data.splitlines()
arp_data_lines.pop(0)

final_arp_data = []
for arp_entry in arp_data_lines:
    (_, ip_address, _, mac_address, _, intf) = arp_entry.split()
    arp_dict = {}
    arp_dict["mac_addr"] = mac_address
    arp_dict["ip_addr"] = ip_address
    arp_dict["interface"] = intf
    final_arp_data.append(arp_dict)

pprint(final_arp_data)

