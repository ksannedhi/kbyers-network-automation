"""Now use send_command() and the expect_string argument to handle the additional prompting. Once again specify a target IP address of '8.8.8.8'."""

from netmiko import ConnectHandler
from getpass import getpass

cisco_dict = {"host": "cisco4.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_ios"}
ios_connect = ConnectHandler(**cisco_dict)

output = ios_connect.find_prompt()
output += ios_connect.send_command("ping", strip_command = False, expect_string = "Protocol")
output += ios_connect.send_command("\n", strip_command = False, expect_string = "address")
output += ios_connect.send_command("8.8.8.8", strip_command = False, expect_string = "count")
output += ios_connect.send_command("\n", strip_command = False, expect_string = "Datag")
output += ios_connect.send_command("\n", strip_command = False, expect_string = "seconds")
output += ios_connect.send_command("\n", strip_command = False, expect_string = "commands")
output += ios_connect.send_command("\n", strip_command = False, expect_string = "Sweep")
output += ios_connect.send_command("\n", strip_command = False, expect_string = "cisco4", strip_prompt = False)

ios_connect.disconnect()
print(output)
