'''1a. As you have done in previous classes, create a Python file named "my_devices.py".
In this file, define the connection information for: 'cisco3', 'arista1', 'arista2', and 'srx2'.
This file should contain all the necessary information to create a Netmiko connection. Use getpass() for the password handling.
Use a global_delay_factor of 4 for both the arista1 device and the arista2 device.
This Python module should be used to store the connection information for all of the exercises in this lesson.

1b. Create a Python script that executes "show version" on each of the network devices defined in my_devices.py.
This script should execute serially i.e. one SSH connection after the other. Record the total execution time for the script.
Print the "show version" output and the total execution time to standard output.
As part of this exercise, you should create a function that both establishes a Netmiko connection and that executes a single show command that you pass in as argument.
This function's arguments should be the Netmiko device dictionary and the "show-command" argument. The function should return the result from the show command.'''

from Ex1_devices import device_list
from datetime import datetime
from netmiko import ConnectHandler

start_time = datetime.now()

def sh_ver_output(dev_dict, sh_ver):
    device = ConnectHandler(**dev_dict)
   
    dev_type = dev_dict.pop("device_type")
    print(f"Printing 'show version' output for the {dev_type}:")
    
    output = device.send_command(sh_ver)
    print(output)
    device.disconnect()

sh_ver_cmd = "show version"
for device in device_list:
    sh_ver_output(device, sh_ver_cmd)

end_time = datetime.now()

total_processing_time = end_time - start_time

print("#" * 53)
print(f"This all took a total time of {total_processing_time} seconds.")
print("#" * 53)

