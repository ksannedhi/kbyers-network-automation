'''1a. Create a Python file named "my_devices.py" that defines the NAPALM connection information for both the 'cisco3' device and the 'arista1' device.
Use getpass() for the password handling. This Python module should be used to store the device connection information for all of the exercises in this lesson.

1b. Create a simple function that accepts the NAPALM device information from the my_devices.py file and creates a NAPALM connection object.
This function should open the NAPALM connection to the device and should return the NAPALM connection object.

1c. Using your "my_devices.py" file and your NAPALM connection function, create a list of NAPALM connection objects to 'cisco3' and 'arista1'.

1d. Iterate through the connection objects, print out the device's connection object itself.
Additionally, pretty print the facts for each device and also print out the device's NAPALM platform type (ios, eos, et cetera).'''

from napalm import get_network_driver
from Ex1_devices import my_devices
from pprint import pprint

def open_napalm_connection(dev_dict):
    dev_type = dev_dict.pop("device_type")
    driver = get_network_driver(dev_type)
    device = driver(**dev_dict)
    device.open()
    return dev_type, device

for dev_dict in my_devices:
    (device_type, device) = open_napalm_connection(dev_dict)
    print(f"For device running on {device_type} platform, below are the basic device details:")
    print("=" * 79)
    pprint(device.get_facts())
    print("=" * 79)
