from netmiko import ConnectHandler
from getpass import getpass
import time
password = getpass()

device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output.txt"
}

dev_connect  = ConnectHandler(**device)
print(dev_connect.find_prompt())

dev_connect.config_mode()
print(dev_connect.find_prompt())

dev_connect.exit_config_mode()
print(dev_connect.find_prompt())

dev_connect.write_channel("disable\n")
time.sleep(2)
print(dev_connect.read_channel())

dev_connect.enable()
print(dev_connect.find_prompt())

dev_connect.disconnect()

