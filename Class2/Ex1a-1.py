from netmiko import ConnectHandler
from getpass import getpass

cisco_dict = {"host": "cisco4.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_ios"}
ios_connect = ConnectHandler(**cisco_dict)

output = ios_connect.find_prompt()
output += ios_connect.send_command_timing("ping", strip_command = False, strip_prompt = False)
output += ios_connect.send_command_timing("\n", strip_command = False)
output += ios_connect.send_command_timing("8.8.8.8", strip_command = False, strip_prompt = False)
output += ios_connect.send_command_timing("\n", strip_command = False)
output += ios_connect.send_command_timing("\n", strip_command = False)
output += ios_connect.send_command_timing("\n", strip_command = False)
output += ios_connect.send_command_timing("\n", strip_command = False)
output += ios_connect.send_command_timing("\n", strip_command = False, strip_prompt = False)

ios_connect.disconnect()
print(output)

