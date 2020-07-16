import yaml

dev_dict = [{"device_name": "cisco_ios_3", "host": "cisco3.lasthop.io", "username": "pyplus", "password": "pyplus", "device_type": "cisco_ios"},
            {"device_name": "jun_srx_2", "host": "srx2.lasthop.io", "username": "pyplus", "password": "pyplus", "device_type": "juniper_junos"},
            {"device_name": "arista_eos_1", "host": "arista1.lasthop.io", "username": "pyplus", "password": "pyplus", "device_type": "arista_eos"},
            {"device_name": "cisco_nxos_1", "host": "nxos1.lasthop.io", "username": "pyplus", "password": "pyplus", "device_type": "cisco_nxos"},
            {"device_name": "cisco_nxos_2", "host": "nxos2.lasthop.io", "username": "pyplus", "password": "pyplus", "device_type": "cisco_nxos"}]

for dev in dev_dict:
    dev["secret"] = "pyplus"

with open("Ex2-1.yml", "w") as f:
    yaml.dump(dev_dict, f)

