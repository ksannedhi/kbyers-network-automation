'''Using a context manager, the ProcessPoolExecutor, and the map() method, create a solution that executes "show ip arp" on all of the devices defined in my_devices.py.
Note, the Juniper device will require "show arp" instead of "show ip arp" so your solution will have to properly account for this.'''

from concurrent.futures import ProcessPoolExecutor
from Ex1_devices import device_list
from Ex2_functions import ssh_command2
from datetime import datetime

start_time = datetime.now()
max_procs = 5

with ProcessPoolExecutor(max_procs) as pool:
    cmd_list = []
    
    for device in device_list:
        if device["device_type"] == "juniper_junos":
            cmd_list.append("show arp")
        else:
            cmd_list.append("show ip arp")

    results = pool.map(ssh_command2, device_list, cmd_list)

    for result in results:
        print(result)

    end_time = datetime.now()

    print(f"Total time taken to execute 'show version' on all the devices: {end_time - start_time}")
