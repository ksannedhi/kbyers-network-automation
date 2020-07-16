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
