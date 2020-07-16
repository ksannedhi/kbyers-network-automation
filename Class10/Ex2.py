'''Create a new file named my_functions.py. Move your function from exercise1 to this file. Name this function "ssh_command".
Reuse functions from this file for the rest of the exercises. Complete the same task as Exercise 1b except this time use "legacy" threads to create a solution.
Launch a separate thread for each device's SSH connection. Print the time required to complete the task for all of the devices.
Move all of the device specific output printing to the called function (i.e. to the child thread).'''

from Ex1_devices import device_list
from Ex2_functions import ssh_command
from datetime import datetime
import threading

start_time = datetime.now()

threads = []

for device in device_list:
    t = threading.Thread(target = ssh_command, args = (device, "show version"))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_time = datetime.now()

print(f"Total time taken to generate the 'show version'output from all the devices: {end_time - start_time}")
