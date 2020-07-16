'''In the lab environment use Netmiko to connect to one of the Cisco NX-OS devices.
You can find the IP addresses and username/passwords of the Cisco devices in the 'Lab Environment' email or alternatively in the ~/.netmiko.yml file.
Simply print the router prompt back from this device to verify you are connecting to the device properly.'''

from netmiko import ConnectHandler

nxos1_dict = {"host": "nxos1.lasthop.io", "username": "pyclass", "password": "88newclass", "device_type": "cisco_nxos"}
nxos1_connect = ConnectHandler(**nxos1_dict)

print(nxos1_connect.find_prompt())
nxos1_connect.disconnect()
