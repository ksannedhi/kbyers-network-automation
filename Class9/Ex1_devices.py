from getpass import getpass
password = getpass()
cisco3_dict = {"hostname": "cisco3.lasthop.io", "username": "pyclass", "password": password, "device_type": "ios"}
arista1_dict = {"hostname": "arista1.lasthop.io", "username": "pyclass", "password": password, "device_type": "eos"}
srx1_dict = {"hostname": "srx1.lasthop.io", "username": "pyclass", "password": password, "device_type": "junos"}
nxos1_dict = {"hostname": "nxos1.lasthop.io", "username": "pyclass", "password": password, "device_type": "nxos", "optional_args": {"port": 8443}}

my_devices = [cisco3_dict, arista1_dict]
