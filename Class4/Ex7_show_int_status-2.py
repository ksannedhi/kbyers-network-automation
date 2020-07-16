from pprint import pprint

sh_int_status = """Port      Name  Status       Vlan  Duplex Speed Type
Gi0/1/0         notconnect   1     auto   auto  10/100/1000BaseTX
Gi0/1/1         notconnect   1     auto   auto  10/100/1000BaseTX
Gi0/1/2         notconnect   1     auto   auto  10/100/1000BaseTX
Gi0/1/3         notconnect   1     auto   auto  10/100/1000BaseTX
"""

sh_int_status_lines = sh_int_status.splitlines()
sh_int_status_lines.pop(0)

int_status_list = []
for int_line in sh_int_status_lines:
    intf_id, intf_status, vlan_id, duplex, speed, intf_type = int_line.split()
    int_status_dict = {}
    int_status_dict["DUPLEX"] = duplex
    int_status_dict["PORT_NAME"] = intf_id
    int_status_dict["PORT_TYPE"] = intf_type
    int_status_dict["SPEED"] = speed
    int_status_dict["STATUS"] = intf_status
    int_status_dict["VLAN"] = vlan_id
    int_status_list.append(int_status_dict)

pprint(int_status_list)
