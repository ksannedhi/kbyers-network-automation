'''On both the NXOS1 and NXOS2 switches configure five VLANs including VLAN names (just pick 5 VLAN numbers between 100 - 999).
Use Netmiko's send_config_from_file() method to accomplish this.
Also use Netmiko's save_config() method to save the changes to the startup-config.'''

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
    
