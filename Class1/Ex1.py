from netmiko import ConnectHandler
from getpass import getpass

cisco_nxos1 = {"host": "nxos1.lasthop.io",
                "username": "pyclass",
                "password": getpass(),
                "device_type": "cisco_nxos"}

print(ConnectHandler(**cisco_nxos1).find_prompt())
