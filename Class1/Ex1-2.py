'''Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices.
Additionally, use a for-loop to accomplish the Netmiko connection creation
Once again print the prompt back from the devices that you connected to.'''

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
nxos1_dict = {"host": "nxos1.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_nxos"}
nxos2_dict = {"host": "nxos2.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_nxos"}

for nxos_router in (nxos1_dict, nxos2_dict):
    nxos_connect = ConnectHandler(**nxos_router)
    print(nxos_connect.find_prompt())
    nxos_connect.disconnect()
