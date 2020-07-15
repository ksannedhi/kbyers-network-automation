'''Create a Netmiko connection to the 'nxos2' device using a global_delay_factor of 2.
Execute 'show lldp neighbors detail' and print the returned output to standard output.
Execute 'show lldp neighbors detail' a second time using send_command() with a delay_factor of 8. Print the output of this command to standard output.
Use the Python datetime library to record the execution time of both of these commands.
Print these execution times to standard output.'''

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

nxos_dict = {"host": "nxos2.lasthop.io", "username": "pyclass", "password": getpass(), "device_type": "cisco_nxos", "global_delay_factor": 2}

nxos_connect = ConnectHandler(**nxos_dict)

print("*" * 75)
print("Using Global Delay Factor:")
print("-" * 26)
start_time1 = datetime.now()
print(f'Starting execution at {start_time1}')
output = nxos_connect.send_command("show lldp nei det")
print(output)
end_time1 = datetime.now()
print(f'End execution at {end_time1}')
exec_time1 = end_time1 - start_time1
print(f'Total execution time: {exec_time1}')

print("*" * 75)
print("Using Local Delay Factor:")
print("-" * 25)
start_time2 = datetime.now()
print(f'Starting execution at {start_time2}')
output2 = nxos_connect.send_command("show lldp nei det", delay_factor = 8)
print(output2)
end_time2 = datetime.now()
print(f'End execution at {end_time2}')
exec_time2 = end_time2 - start_time2
print(f'Total execution time: {exec_time2}')

print("*" * 75)
print(f'Delay factor 8 caused {exec_time2 - exec_time1} more delay than a delay factor of 2.')
print("*" * 75)

nxos_connect.disconnect()
