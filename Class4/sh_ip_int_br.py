import textfsm
from pprint import pprint

template = open("sh_ip_int_br_ks.textfsm")

with open("sh_ip_int_br.txt") as f:
    raw_data = f.read()

re_table = textfsm.TextFSM(template)
output = re_table.ParseText(raw_data)
template.close()

print(re_table.header)
pprint(output)

