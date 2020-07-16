from napalm import get_network_driver
from getpass import getpass
from pprint import pprint

cisco3_dict = {"hostname": "cisco3.lasthop.io",
                "username": "pyclass",
                "password": getpass(),
                "device_type": "ios",
                "optional_args": {}}

device_type = cisco3_dict.pop("device_type")
driver = get_network_driver(device_type)
device = driver(**cisco3_dict)
device.open()

pprint(device.get_facts())
print(device.hostname)

