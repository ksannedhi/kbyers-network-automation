import textfsm
from pprint import pprint
import csv

template = open("sh_inventory.textfsm")
with open("sh_inventory.txt") as f:
    raw_data = f.read()

re_table = textfsm.TextFSM(template)
sh_inventory_data = re_table.ParseText(raw_data)
template.close()

print(re_table.header)
pprint(sh_inventory_data)

