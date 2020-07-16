from napalm import get_network_driver
from getpass import getpass
from pprint import pprint

cisco3_dict = {"hostname": "cisco3.lasthop.io", "username": "pyclass", "password": getpass()}

driver = get_network_driver("ios")
device = driver(**cisco3_dict)
device.open()

pprint(device.get_config()['running'])

