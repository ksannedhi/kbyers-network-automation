import textfsm
from pprint import pprint

template = open("Ex2_sh_int_status.textfsm")

with open("Ex1_sh_int_status.txt") as f:
    raw_data = f.read()

re_table = textfsm.TextFSM(template)
sh_int_status_op = re_table.ParseText(raw_data)
template.close()

intf_status_header = re_table.header

intf_status_list = []

for intf_entry in sh_int_status_op:
    intf_dict = dict(zip(intf_status_header, intf_entry))
    intf_status_list.append(intf_dict)

pprint(intf_status_list)
