'''On your AWS lab server, look at the ntc-templates index file (at ~/ntc-templates/templates/index).
Look at some of the commands available for cisco_ios (you can use 'cat ~/ntc-templates/templates/index | grep cisco_ios' to see this).
Also look at some of the abbreviated forms of Cisco IOS commands that are supported in the index file.

Create a script using Netmiko that executes 'show version' and 'show lldp neighbors' against the Cisco4 device with use_textfsm=True.

What is the outermost data structure that is returned from 'show lldp neighbors' (dictionary, list, string, something else)? 
The Cisco4 device should only have one LLDP entry (the HPE switch that this router connects to). From this LLDP data, print out the remote device's interface.
In other words, print out the port number on the HPE switch that Cisco4 connects into.'''

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
