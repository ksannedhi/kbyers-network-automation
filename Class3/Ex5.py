'''In your lab environment, there is a file located at ~/.netmiko.yml.
This file contains all of the devices used in the lab. Create a Python program that processes this YAML file and then uses Netmiko to connect to the Cisco3 router.
Print out the router prompt from this device.

Note, the device dictionaries in the .netmiko.yml file use key-value pairs designed to work directly with Netmiko.
The .netmiko.yml also contains group definitions for: cisco, arista, juniper, and nxos groups.
These group definitions are lists of devices.'''

import yaml
from netmiko import ConnectHandler
from os import path

hw_dir = path.expanduser("~")
file_name = path.join(hw_dir, ".netmiko.yml")

with open(file_name) as f:
    dev_data = yaml.load(f)

cisco3_dict = dev_data["cisco3"]
cisco3_connect = ConnectHandler(**cisco3_dict)
print(cisco3_connect.find_prompt())

