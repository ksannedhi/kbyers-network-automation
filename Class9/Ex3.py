'''3a. Using your existing functions and the my_devices.py file, create a NAPALM connection to both cisco3 and arista1.

3b. Create two new text files `arista1.lasthop.io-loopbacks` and `cisco3.lasthop.io-loopbacks`. In each of these files, create two new loopback interfaces with a description.
Your files should be similar to the following:
interface loopback100
  description loopback100
!
interface loopback101
  description loopback101

For both cisco3 and arista1, use the load_merge_candidate() method to stage the candidate configuration.
In other words, use load_merge_candidate() and your loopback configuration file to stage a configuration change.
Use the NAPALM compare_config() method to print out the pending differences (i.e. the differences between the running configuration and the candidate configuration).

3c. Commit the pending changes to each device, and check the diff once again (after the commit_config).'''

from Ex2_functions import open_napalm_connection
from Ex1_devices import my_devices

for dev_dict in my_devices:
    dev_dict_copy = dev_dict.copy()
    device_type = dev_dict_copy.pop("device_type")
    
    device = open_napalm_connection(dev_dict)
    
    if device_type == "ios":
        device.load_merge_candidate(filename = "Ex3_ios_loopbacks")
        print(device.compare_config())
        input("Press 'Enter' key if you are OK to apply this configuration to the ios platform.")
    else:
        device.load_merge_candidate(filename = "Ex3_eos_loopbacks")
        print(device.compare_config())
        input(f"Press 'Enter' key if you are OK to apply this configuration to the eos platform.")

    device.commit_config()
    print("Following changes are committed successfully.")
