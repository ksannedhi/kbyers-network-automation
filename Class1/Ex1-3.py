'''For one of the Cisco IOS devices, use Netmiko and the send_command() method to retrieve 'show version'.
Save this output to a file in the current working directory.'''

from netmiko import ConnectHandler

nxos1_dict = {"host": "nxos1.lasthop.io", "username": "pyclass", "password": "88newclass", "device_type": "cisco_nxos"}
nxos1_connect = ConnectHandler(**nxos1_dict)
sh_ver_op = nxos1_connect.send_command("sh ver")
nxos1_connect.disconnect()

with open("show_ver-1.txt", "w") as f:
    f.write(sh_ver_op)

