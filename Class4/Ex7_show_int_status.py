import textfsm
from pprint import pprint

template = open("Ex2_sh_int_status.textfsm")

with open("Ex1_sh_int_status.txt") as f:
    raw_data = f.read()

re_table = textfsm.TextFSM(template)
sh_int_status_op = re_table.ParseText(raw_data)
template.close()

sh_int_status_list = []

for intf_entry in sh_int_status_op:
    intf_dict = {}
    port_name = intf_entry[0]
    intf_dict["PORT_NAME"] = port_name
    status = intf_entry[1]
    intf_dict["STATUS"] = status
    vlan = intf_entry[2]
    intf_dict["VLAN"] = vlan
    duplex = intf_entry[3]
    intf_dict["DUPLEX"] = duplex
    speed = intf_entry[4]
    intf_dict["SPEED"] = speed
    port_type = intf_entry[5]
    intf_dict["PORT_TYPE"] = port_type
    
    sh_int_status_list.append(intf_dict)

pprint(sh_int_status_list)

