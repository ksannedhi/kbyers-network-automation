'''Add a second NX-OS device to your first exercise. Make sure you are using dictionaries to represent the two NX-OS devices.
Additionally, use a for-loop to accomplish the Netmiko connection creation
Once again print the prompt back from the devices that you connected to.'''

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
