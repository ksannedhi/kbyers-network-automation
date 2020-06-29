from netmiko import ConnectHandler
from getpass import getpass
password = getpass()

nxos1_dict = {"host": "nxos1.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_nxos"}
nxos2_dict = {"host": "nxos2.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_nxos"}

for dev in (nxos1_dict, nxos2_dict):
    dev_conn = ConnectHandler(**dev)
    op = dev_conn.find_prompt()
    op += dev_conn.send_config_from_file("vlans.txt")
    dev_conn.save_config()
    print(op)
    print("*" * 60)
    dev_conn.disconnect()
    
