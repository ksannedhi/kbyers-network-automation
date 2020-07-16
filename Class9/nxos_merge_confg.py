from napalm import get_network_driver
from getpass import getpass

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

nxos1_dict = {"hostname": "nxos1.lasthop.io",
            "username": "pyclass",
            "password": getpass(),
            "optional_args": {"port": 8443}}

driver = get_network_driver("nxos")
device = driver(**nxos1_dict)
device.open()

device.load_merge_candidate(filename = "nxos-add-vlans.conf")

def hit_enter():
    input("If you are OK with the above config, hit Enter to proceed")

print(device.compare_config())
hit_enter() #Alternaterly, simply write input("Hit Enter") line diretly here.
device.commit_config()

