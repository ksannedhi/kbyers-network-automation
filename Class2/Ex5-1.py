from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

nxos1_dict = {"host": "nxos1.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_nxos"}
nxos2_dict = {"host": "nxos2.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_nxos"}

for nxos_dev in (nxos1_dict, nxos2_dict):
    nxos_connect = ConnectHandler(**nxos_dev)
    cmd_op = nxos_connect.send_config_from_file("vlans.txt")
    print(cmd_op)
    nxos_connect.disconnect()

