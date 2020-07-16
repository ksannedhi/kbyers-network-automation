'''2a. Create a new file named "my_functions.py" that will store a set of reusable functions. Move the "open_napalm_connection" function from exercise1 into this Python file.
Import the network devices once again from my_devices.py and create a list of connection objects (once again with connections to both cisco3 and arista1).

2b. Pretty print the arp table for each of these devices. Gather this information using the appropriate NAPALM Getter.

2c. Attempt to use the get_ntp_peers() method against both of the devices. Does this method work? Your code should gracefully handle any exceptions that occur.
In other words, an exception that occurs due to this get_ntp_peers() method, should not cause the program to crash.

2d. Create another function in "my_functions.py". This function should be named "create_backup" and should accept a NAPALM connection object as an argument.
Using the NAPALM get_config() method, the function should retrieve and write the current running configuration to a file. The filename should be unique for each device.
In other words, "cisco3" and "arista1" should each have a separate file that stores their running configuration.
Note, get_config() returns a dictionary where the running-config is referenced using the "running" key.
Call this function as part of your main exercise2 and ensure that the configurations from both cisco3 and arista1 are backed up properly.'''

from Ex1_devices import my_devices
from Ex2_functions import open_napalm_connection, create_backup
from pprint import pprint

for dev_dict in my_devices:
    dev_dict_copy = dev_dict.copy()
    device_type = dev_dict_copy.pop("device_type")

    device = open_napalm_connection(dev_dict)

    print(f"ARP table for device on plaform {device_type}:")
    print("=" * 56)
    pprint(device.get_arp_table())
    print("=" * 56)
 
    print(f"NTP peers of device on plaform {device_type}:")
    print("=" * 56)
    try:
        pprint(device.get_ntp_peers())
    except NotImplementedError:
        print(f"Looks like get_ntp_peers support is not available on {device_type}.")
    print("=" * 56)

    if create_backup(device):
        print(f"Backup successfully created for {device.hostname}")
        print("=" * 56)
