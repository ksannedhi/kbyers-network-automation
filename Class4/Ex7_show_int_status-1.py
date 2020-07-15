'''Using your TextFSM template and the 'show interface status' data from exercise2, create a Python program that uses TextFSM to parse this data.
In this Python program, read the show interface status data from a file and process it using the TextFSM template.
From this parsed-output, create a list of dictionaries. The program output should look as follows:
$ python ex7_show_int_status.py 

[{'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/0',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/1',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/2',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'},
 {'DUPLEX': 'auto',
  'PORT_NAME': 'Gi0/1/3',
  'PORT_TYPE': '10/100/1000BaseTX',
  'SPEED': 'auto',
  'STATUS': 'notconnect',
  'VLAN': '1'}]'''

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
