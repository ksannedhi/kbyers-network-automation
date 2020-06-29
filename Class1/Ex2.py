from netmiko import ConnectHandler
from getpass import getpass

nxos_dev_list = [{"host": "nxos1.lasthop.io",
            "username": "pyclass",
            "password": getpass(),
            "device_type": "cisco_nxos"},
            {"host": "nxos2.lasthop.io",
            "username": "pyclass",
            "password": getpass(),
            "device_type": "cisco_nxos"}]

for dev in nxos_dev_list:
    prompt = ConnectHandler(**dev).find_prompt()
    print(prompt)
    print("=" * 12)

