"""Use the extended 'ping' command and Netmiko on the 'cisco4' router. This should prompt you for additional information as follows:

cisco4#ping
Protocol [ip]: 
Target IP address: 8.8.8.8
Repeat count [5]: 
Datagram size [100]: 
Timeout in seconds [2]: 
Extended commands [n]: 
Sweep range of sizes [n]: 
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 8.8.8.8, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/1/4 ms

Use send_command_timing() to handle the additional prompting from this 'ping' command. Specify a target IP address of '8.8.8.8'"""

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
