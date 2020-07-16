from netmiko import ConnectHandler
from getpass import getpass
import time

password = getpass()
cisco4_dict = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output-1.txt"}

cisco4_connect = ConnectHandler(**cisco4_dict)
print(cisco4_connect.find_prompt())

cisco4_connect.config_mode()
print(cisco4_connect.find_prompt())

cisco4_connect.send_command("exit", expect_string = "#")
print(cisco4_connect.find_prompt())

cisco4_connect.write_channel("disable\n") #Without \n, >cisco4 is not being displayed.
time.sleep(2)
print(cisco4_connect.read_channel())

cisco4_connect.enable()
print(cisco4_connect.find_prompt())

cisco4_connect.disconnect()
