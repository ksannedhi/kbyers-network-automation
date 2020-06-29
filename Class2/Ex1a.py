from netmiko import ConnectHandler
from getpass import getpass

xe_dict = {"host": "cisco4.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_xe"}

xe_connect = ConnectHandler(**xe_dict)

output = xe_connect.find_prompt()
output += xe_connect.send_command_timing("ping", strip_command = False, strip_prompt = False)
output += xe_connect.send_command_timing("\n", strip_command = False, strip_prompt = False)
output += xe_connect.send_command_timing("8.8.8.8", strip_command = False, strip_prompt = False)
output += xe_connect.send_command_timing("\n", strip_command = False, strip_prompt = False)
output += xe_connect.send_command_timing("\n", strip_command = False, strip_prompt = False)
output += xe_connect.send_command_timing("\n", strip_command = False, strip_prompt = False)
output += xe_connect.send_command_timing("\n", strip_command = False, strip_prompt = False)
output += xe_connect.send_command_timing("\n", strip_command = False, strip_prompt = False)

xe_connect.disconnect()
print(output)

