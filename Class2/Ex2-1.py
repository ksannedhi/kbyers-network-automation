'''Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2.
Execute 'show lldp neighbors detail' and print the returned output to standard output.
Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. Print the output of this command to standard output.
Use the Python datetime library to record the execution time of both of these commands.
Print these execution times to standard output.'''

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

nxos2_dict = {"host": "nxos2.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_nxos", "global_delay_factor": 2}
nxos2_connect = ConnectHandler(**nxos2_dict)

time1_before = datetime.now()
output1 = nxos2_connect.send_command("sh lldp nei det")
print(output1)
time1_after = datetime.now()
print(f"Time taken for command execution with the global delay factor: {time1_after - time1_before}")

print("=" *60)

time2_before = datetime.now()
output2 = nxos2_connect.send_command("sh lldp nei det", delay_factor = 8)
print(output2)
time2_after = datetime.now()
print(f"Time taken for command execution with the local delay factor: {time2_after - time2_before}")
