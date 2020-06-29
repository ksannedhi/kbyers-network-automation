from netmiko import ConnectHandler
from getpass import getpass

xe_dict = {"host": "nxos2.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_nxos"}

xe_connect = ConnectHandler(**xe_dict)

ver_op = xe_connect.send_command("sh ver", use_textfsm = True)
print(ver_op)

print("*" * 75)

lldp_op = xe_connect.send_command("sh lldp nei", use_textfsm = True)
print(lldp_op)

print(f'Data structure type: {type(lldp_op[-1])}')

neigh_int = lldp_op[-1]['neighbor_interface']
print("Neighbor's interface to which the router is connected to is", neigh_int)

xe_connect.disconnect()
