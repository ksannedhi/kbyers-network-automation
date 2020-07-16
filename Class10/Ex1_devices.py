from getpass import getpass
password = getpass()

arista1 = {"host": "arista1.lasthop.io", "username": "pyclass", "password": password, "device_type": "arista_eos", "global_delay_factor": 4}
arista2 = {"host": "arista2.lasthop.io", "username": "pyclass", "password": password, "device_type": "arista_eos", "global_delay_factor": 4}
cisco3 = {"host": "cisco3.lasthop.io", "username": "pyclass", "password": password, "device_type": "cisco_ios"}
srx1 = {"host": "srx1.lasthop.io", "username": "pyclass", "password": password, "device_type": "juniper_junos"}

device_list = [arista1, arista2, cisco3, srx1]
