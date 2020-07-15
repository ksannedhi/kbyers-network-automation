'''Create a list where each of the list elements is a dictionary representing one of the network devices in the lab. Do this for at least four of the lab devices.
The dictionary should have keys corresponding to the device_name, host (i.e. FQDN), username, and password.
Use a fictional username/password to avoid checking the lab password into GitHub.'''

import yaml
from pprint import pprint

dev_list = [{"device_name": "Cisco3", "host": "cisco3.lasthop.io"},
            {"device_name": "Cisco4", "host": "cisco4.lasthop.io"},
            {"device_name": "NXOS1", "host": "nxos1.lasthop.io"},
            {"device_name": "NXOS2", "host": "nxos2.lasthop.io"},
            {"device_name": "Arista1", "host": "arista1.lasthop.io"}]

for dev in dev_list:
    dev["username"] = "pyplus"
    dev["password"] = "pyplus"
    dev["secret"] = "pyplus"

pprint(dev_list)

with open('Ex2.yml', 'w') as f:
    yaml.dump(dev_list, f, default_flow_style = False)
