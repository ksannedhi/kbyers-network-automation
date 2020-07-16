from napalm import get_network_driver
from getpass import getpass
from pprint import pprint

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

password = getpass()

dev_list = [
{"hostname": "nxos1.lasthop.io", "username": "pyclass", "password": password, "device_type": "nxos", "optional_args": {"port": 8443}},
{"hostname": "cisco3.lasthop.io", "username": "pyclass", "password": password, "device_type": "ios"},
{"hostname": "srx1.lasthop.io", "username": "pyclass", "password": password, "device_type": "junos"}]

for dev_dict in dev_list:
    device_type = dev_dict.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**dev_dict)
    device.open()

    lldp_nei = device.get_lldp_neighbors()
    pprint(lldp_nei)
